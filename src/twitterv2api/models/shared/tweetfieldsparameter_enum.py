import dataclasses
from enum import Enum

class TweetFieldsParameterEnum(str, Enum):
    ATTACHMENTS = "attachments"
    AUTHOR_ID = "author_id"
    CONTEXT_ANNOTATIONS = "context_annotations"
    CONVERSATION_ID = "conversation_id"
    CREATED_AT = "created_at"
    EDIT_CONTROLS = "edit_controls"
    EDIT_HISTORY_TWEET_IDS = "edit_history_tweet_ids"
    ENTITIES = "entities"
    GEO = "geo"
    ID = "id"
    IN_REPLY_TO_USER_ID = "in_reply_to_user_id"
    LANG = "lang"
    NON_PUBLIC_METRICS = "non_public_metrics"
    ORGANIC_METRICS = "organic_metrics"
    POSSIBLY_SENSITIVE = "possibly_sensitive"
    PROMOTED_METRICS = "promoted_metrics"
    PUBLIC_METRICS = "public_metrics"
    REFERENCED_TWEETS = "referenced_tweets"
    REPLY_SETTINGS = "reply_settings"
    SOURCE = "source"
    TEXT = "text"
    WITHHELD = "withheld"

