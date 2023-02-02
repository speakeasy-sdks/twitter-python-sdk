import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import point as shared_point
from ..shared import contextannotation as shared_contextannotation
from ..shared import fulltextentities as shared_fulltextentities
from ..shared import replysettings_enum as shared_replysettings_enum
from ..shared import tweetwithheld as shared_tweetwithheld


@dataclass_json
@dataclasses.dataclass
class TweetAttachments:
    r"""TweetAttachments
    Specifies the type of attachments (if any) present in this Tweet.
    """
    
    media_keys: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('media_keys') }})
    poll_ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('poll_ids') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetEditControls:
    editable_until: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('editable_until'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    edits_remaining: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('edits_remaining') }})
    is_edit_eligible: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('is_edit_eligible') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetGeo:
    r"""TweetGeo
    The location tagged on the Tweet, if the user provided one.
    """
    
    coordinates: Optional[shared_point.Point] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('coordinates') }})
    place_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('place_id') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetNonPublicMetrics:
    r"""TweetNonPublicMetrics
    Nonpublic engagement metrics for the Tweet at the time of the request.
    """
    
    impression_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('impression_count') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetOrganicMetrics:
    r"""TweetOrganicMetrics
    Organic nonpublic engagement metrics for the Tweet at the time of the request.
    """
    
    impression_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('impression_count') }})
    like_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('like_count') }})
    reply_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('reply_count') }})
    retweet_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('retweet_count') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetPromotedMetrics:
    r"""TweetPromotedMetrics
    Promoted nonpublic engagement metrics for the Tweet at the time of the request.
    """
    
    impression_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('impression_count') }})
    like_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('like_count') }})
    reply_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reply_count') }})
    retweet_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('retweet_count') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetPublicMetrics:
    r"""TweetPublicMetrics
    Engagement metrics for the Tweet at the time of the request.
    """
    
    impression_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('impression_count') }})
    like_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('like_count') }})
    reply_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('reply_count') }})
    retweet_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('retweet_count') }})
    quote_count: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quote_count') }})
    
class TweetReferencedTweetsTypeEnum(str, Enum):
    RETWEETED = "retweeted"
    QUOTED = "quoted"
    REPLIED_TO = "replied_to"


@dataclass_json
@dataclasses.dataclass
class TweetReferencedTweets:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    type: TweetReferencedTweetsTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    

@dataclass_json
@dataclasses.dataclass
class Tweet:
    edit_history_tweet_ids: list[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('edit_history_tweet_ids') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('text') }})
    attachments: Optional[TweetAttachments] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attachments') }})
    author_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('author_id') }})
    context_annotations: Optional[list[shared_contextannotation.ContextAnnotation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('context_annotations') }})
    conversation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('conversation_id') }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    edit_controls: Optional[TweetEditControls] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('edit_controls') }})
    entities: Optional[shared_fulltextentities.FullTextEntities] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entities') }})
    geo: Optional[TweetGeo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('geo') }})
    in_reply_to_user_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('in_reply_to_user_id') }})
    lang: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('lang') }})
    non_public_metrics: Optional[TweetNonPublicMetrics] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('non_public_metrics') }})
    organic_metrics: Optional[TweetOrganicMetrics] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('organic_metrics') }})
    possibly_sensitive: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('possibly_sensitive') }})
    promoted_metrics: Optional[TweetPromotedMetrics] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('promoted_metrics') }})
    public_metrics: Optional[TweetPublicMetrics] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('public_metrics') }})
    referenced_tweets: Optional[list[TweetReferencedTweets]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('referenced_tweets') }})
    reply_settings: Optional[shared_replysettings_enum.ReplySettingsEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('reply_settings') }})
    source: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('source') }})
    withheld: Optional[shared_tweetwithheld.TweetWithheld] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('withheld') }})
    
