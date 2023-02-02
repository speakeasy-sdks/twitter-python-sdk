import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from enum import Enum

class PollFieldsParameterEnum(str, Enum):
    DURATION_MINUTES = "duration_minutes"
    END_DATETIME = "end_datetime"
    ID = "id"
    OPTIONS = "options"
    VOTING_STATUS = "voting_status"

