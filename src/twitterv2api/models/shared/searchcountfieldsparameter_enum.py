import dataclasses
from enum import Enum

class SearchCountFieldsParameterEnum(str, Enum):
    END = "end"
    START = "start"
    TWEET_COUNT = "tweet_count"

