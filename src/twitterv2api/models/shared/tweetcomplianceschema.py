import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class TweetComplianceSchemaTweet:
    author_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('author_id') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetComplianceSchema:
    event_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    tweet: TweetComplianceSchemaTweet = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('tweet') }})
    quote_tweet_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('quote_tweet_id') }})
    
