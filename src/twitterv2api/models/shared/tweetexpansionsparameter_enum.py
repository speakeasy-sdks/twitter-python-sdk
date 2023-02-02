import dataclasses
from enum import Enum

class TweetExpansionsParameterEnum(str, Enum):
    ATTACHMENTS_MEDIA_KEYS = "attachments.media_keys"
    ATTACHMENTS_POLL_IDS = "attachments.poll_ids"
    AUTHOR_ID = "author_id"
    EDIT_HISTORY_TWEET_IDS = "edit_history_tweet_ids"
    ENTITIES_MENTIONS_USERNAME = "entities.mentions.username"
    GEO_PLACE_ID = "geo.place_id"
    IN_REPLY_TO_USER_ID = "in_reply_to_user_id"
    REFERENCED_TWEETS_ID = "referenced_tweets.id"
    REFERENCED_TWEETS_ID_AUTHOR_ID = "referenced_tweets.id.author_id"

