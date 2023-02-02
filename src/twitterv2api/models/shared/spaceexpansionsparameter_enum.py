import dataclasses
from enum import Enum

class SpaceExpansionsParameterEnum(str, Enum):
    CREATOR_ID = "creator_id"
    HOST_IDS = "host_ids"
    INVITED_USER_IDS = "invited_user_ids"
    SPEAKER_IDS = "speaker_ids"
    TOPIC_IDS = "topic_ids"

