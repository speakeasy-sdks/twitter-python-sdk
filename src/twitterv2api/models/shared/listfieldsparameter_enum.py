import dataclasses
from enum import Enum

class ListFieldsParameterEnum(str, Enum):
    CREATED_AT = "created_at"
    DESCRIPTION = "description"
    FOLLOWER_COUNT = "follower_count"
    ID = "id"
    MEMBER_COUNT = "member_count"
    NAME = "name"
    OWNER_ID = "owner_id"
    PRIVATE = "private"

