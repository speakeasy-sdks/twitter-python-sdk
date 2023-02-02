import dataclasses
from enum import Enum

class DmEventFieldsParameterEnum(str, Enum):
    ATTACHMENTS = "attachments"
    CREATED_AT = "created_at"
    DM_CONVERSATION_ID = "dm_conversation_id"
    EVENT_TYPE = "event_type"
    ID = "id"
    PARTICIPANT_IDS = "participant_ids"
    REFERENCED_TWEETS = "referenced_tweets"
    SENDER_ID = "sender_id"
    TEXT = "text"

