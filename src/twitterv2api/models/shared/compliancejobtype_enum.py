import dataclasses
from enum import Enum

class ComplianceJobTypeEnum(str, Enum):
    TWEETS = "tweets"
    USERS = "users"

