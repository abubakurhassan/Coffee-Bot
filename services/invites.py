active_invites = {}

def set_waiting(channel_id: int, invitee_id: int, wait_type: str):
    active_invites[channel_id] = {
        "invitee_id": invitee_id,
        "type": wait_type
    }

def clear_waiting(channel_id: int):
    active_invites.pop(channel_id, None)

def get_waiting(channel_id: int):
    return active_invites.get(channel_id)