import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from enum import Enum

class SpaceFieldsParameterEnum(str, Enum):
    CREATED_AT = "created_at"
    CREATOR_ID = "creator_id"
    ENDED_AT = "ended_at"
    HOST_IDS = "host_ids"
    ID = "id"
    INVITED_USER_IDS = "invited_user_ids"
    IS_TICKETED = "is_ticketed"
    LANG = "lang"
    PARTICIPANT_COUNT = "participant_count"
    SCHEDULED_START = "scheduled_start"
    SPEAKER_IDS = "speaker_ids"
    STARTED_AT = "started_at"
    STATE = "state"
    SUBSCRIBER_COUNT = "subscriber_count"
    TITLE = "title"
    TOPIC_IDS = "topic_ids"
    UPDATED_AT = "updated_at"

