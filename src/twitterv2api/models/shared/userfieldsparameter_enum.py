import dataclasses
from enum import Enum

class UserFieldsParameterEnum(str, Enum):
    CREATED_AT = "created_at"
    DESCRIPTION = "description"
    ENTITIES = "entities"
    ID = "id"
    LOCATION = "location"
    NAME = "name"
    PINNED_TWEET_ID = "pinned_tweet_id"
    PROFILE_IMAGE_URL = "profile_image_url"
    PROTECTED = "protected"
    PUBLIC_METRICS = "public_metrics"
    URL = "url"
    USERNAME = "username"
    VERIFIED = "verified"
    VERIFIED_TYPE = "verified_type"
    WITHHELD = "withheld"

