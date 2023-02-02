import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class TweetUnviewableTweet:
    author_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('author_id') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class TweetUnviewable:
    application: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('application') }})
    event_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    tweet: TweetUnviewableTweet = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('tweet') }})
    
