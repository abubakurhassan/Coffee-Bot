active_invites = {}

def set_waiting(channel_id: int, invitee_id: int):
    active_invites[channel_id] = {
        "invitee_id": invitee_id,
    }

def clear_waiting(channel_id: int):
    active_invites.pop(channel_id, None)

def get_waiting(channel_id: int):
    return active_invites.get(channel_id)