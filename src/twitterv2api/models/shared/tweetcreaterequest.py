import dataclasses
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class TweetCreateRequestGeo:
    r"""TweetCreateRequestGeo
    Place ID being attached to the Tweet for geo location.
    """
    
    place_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('place_id') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetCreateRequestMedia:
    r"""TweetCreateRequestMedia
    Media information being attached to created Tweet. This is mutually exclusive from Quote Tweet Id, Poll, and Card URI.
    """
    
    media_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('media_ids') }})
    tagged_user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tagged_user_ids') }})
    
class TweetCreateRequestPollReplySettingsEnum(str, Enum):
    FOLLOWING = "following"
    MENTIONED_USERS = "mentionedUsers"


@dataclass_json
@dataclasses.dataclass
class TweetCreateRequestPoll:
    r"""TweetCreateRequestPoll
    Poll options for a Tweet with a poll. This is mutually exclusive from Media, Quote Tweet Id, and Card URI.
    """
    
    duration_minutes: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('duration_minutes') }})
    options: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('options') }})
    reply_settings: Optional[TweetCreateRequestPollReplySettingsEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reply_settings') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetCreateRequestReply:
    r"""TweetCreateRequestReply
    Tweet information of the Tweet being replied to.
    """
    
    in_reply_to_tweet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('in_reply_to_tweet_id') }})
    exclude_reply_user_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('exclude_reply_user_ids') }})
    
class TweetCreateRequestReplySettingsEnum(str, Enum):
    FOLLOWING = "following"
    MENTIONED_USERS = "mentionedUsers"


@dataclass_json
@dataclasses.dataclass
class TweetCreateRequest:
    card_uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('card_uri') }})
    direct_message_deep_link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('direct_message_deep_link') }})
    for_super_followers_only: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('for_super_followers_only') }})
    geo: Optional[TweetCreateRequestGeo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('geo') }})
    media: Optional[TweetCreateRequestMedia] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('media') }})
    nullcast: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('nullcast') }})
    poll: Optional[TweetCreateRequestPoll] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('poll') }})
    quote_tweet_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quote_tweet_id') }})
    reply: Optional[TweetCreateRequestReply] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reply') }})
    reply_settings: Optional[TweetCreateRequestReplySettingsEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reply_settings') }})
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('text') }})
    
