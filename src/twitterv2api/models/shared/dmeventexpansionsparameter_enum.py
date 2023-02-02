import dataclasses
from enum import Enum

class DmEventExpansionsParameterEnum(str, Enum):
    ATTACHMENTS_MEDIA_KEYS = "attachments.media_keys"
    PARTICIPANT_IDS = "participant_ids"
    REFERENCED_TWEETS_ID = "referenced_tweets.id"
    SENDER_ID = "sender_id"

