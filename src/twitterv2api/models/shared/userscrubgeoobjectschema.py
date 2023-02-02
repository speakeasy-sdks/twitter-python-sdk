import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class UserScrubGeoObjectSchemaUser:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    

@dataclass_json
@dataclasses.dataclass
class UserScrubGeoObjectSchema:
    event_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('event_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    up_to_tweet_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('up_to_tweet_id') }})
    user: UserScrubGeoObjectSchemaUser = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('user') }})
    
