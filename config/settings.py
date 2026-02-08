import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file in parent directory
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Get the allowed channel ID from environment variables
ALLOWED_CHANNEL_ID = int(os.getenv('COFFEE_CHANNEL_ID'))

# Optional: Add validation to ensure the variable is set
if not os.getenv('COFFEE_CHANNEL_ID'):
    raise ValueError("COFFEE_CHANNEL_ID is not set in the .env file")



# --- Invite times out after 1 hour --- #
INVITE_TIMEOUT_SECONDS = 3600 

# --- Status constants --- #
STATUS_PENDING = "pending"
STATUS_ACCEPTED = "accepted"
STATUS_DECLINED = "declined"
STATUS_EXPIRED = "expired"