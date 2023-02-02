import dataclasses
from enum import Enum

class ReplySettingsEnum(str, Enum):
    EVERYONE = "everyone"
    MENTIONED_USERS = "mentionedUsers"
    FOLLOWING = "following"
    OTHER = "other"

