import sqlite3
from datetime import datetime
from pathlib import Path

Path("database").mkdir(exist_ok=True)

DB_PATH = "database/coffee.db"

def init_db():
    """Initialize the database with the coffee_interactions table"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS coffee_interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            inviter_id INTEGER NOT NULL,
            inviter_name TEXT NOT NULL,
            invitee_id INTEGER NOT NULL,
            invitee_name TEXT NOT NULL,
            channel_id INTEGER NOT NULL,
            guild_id INTEGER NOT NULL,
            response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def record_interaction(inviter_id: int, inviter_name: str, invitee_id: int, invitee_name: str, channel_id: int, guild_id: int, response: str):
    """Record a coffee request in the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO coffee_interactions 
        (inviter_id, inviter_name, invitee_id, invitee_name, channel_id, guild_id, response)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (inviter_id, inviter_name, invitee_id, invitee_name, channel_id, guild_id, response))
    
    conn.commit()
    conn.close()

def get_user_stats(user_id: int):
    """Get statistics for a specific user"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # --- Times they invited --- #
    cursor.execute('''
        SELECT COUNT(*) FROM coffee_interactions 
        WHERE inviter_id = ?
    ''', (user_id,))
    invites_sent = cursor.fetchone()[0]
    
    # --- Times they accepted --- #
    cursor.execute('''
        SELECT COUNT(*) FROM coffee_interactions 
        WHERE invitee_id = ? AND response = 'accepted'
    ''', (user_id,))
    invites_accepted = cursor.fetchone()[0]
    
    # --- Times they declined --- #
    cursor.execute('''
        SELECT COUNT(*) FROM coffee_interactions 
        WHERE invitee_id = ? AND response = 'declined'
    ''', (user_id,))
    invites_declined = cursor.fetchone()[0]
    
    conn.close()
    
    return {
        'invites_sent': invites_sent,
        'invites_accepted': invites_accepted,
        'invites_declined': invites_declined
    }

def get_all_interactions(limit: int = 10):
    """Get recent coffee interactions"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT inviter_name, invitee_name, response, timestamp 
        FROM coffee_interactions 
        ORDER BY timestamp DESC 
        LIMIT ?
    ''', (limit,))
    
    results = cursor.fetchall()
    conn.close()
    
    return results

def get_leaderboard():
    """Get users ranked by most coffee invites sent"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT inviter_name, COUNT(*) as invite_count 
        FROM coffee_interactions 
        GROUP BY inviter_id 
        ORDER BY invite_count DESC 
        LIMIT 10
    ''')
    
    results = cursor.fetchall()
    conn.close()
    
    return results