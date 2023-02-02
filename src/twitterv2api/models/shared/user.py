import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import urlentity as shared_urlentity
from ..shared import fulltextentities as shared_fulltextentities
from ..shared import userwithheld as shared_userwithheld


@dataclass_json
@dataclasses.dataclass
class UserEntitiesURL:
    r"""UserEntitiesURL
    Expanded details for the URL specified in the User's profile, with start and end indices.
    """
    
    urls: Optional[list[shared_urlentity.URLEntity]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('urls') }})
    

@dataclass_json
@dataclasses.dataclass
class UserEntities:
    r"""UserEntities
    A list of metadata found in the User's profile description.
    """
    
    description: Optional[shared_fulltextentities.FullTextEntities] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    url: Optional[UserEntitiesURL] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('url') }})
    

@dataclass_json
@dataclasses.dataclass
class UserPublicMetrics:
    r"""UserPublicMetrics
    A list of metrics for this User.
    """
    
    followers_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('followers_count') }})
    following_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('following_count') }})
    listed_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('listed_count') }})
    tweet_count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('tweet_count') }})
    

@dataclass_json
@dataclasses.dataclass
class User:
    r"""User
    The Twitter User object.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('username') }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    entities: Optional[UserEntities] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('entities') }})
    location: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('location') }})
    pinned_tweet_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('pinned_tweet_id') }})
    profile_image_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('profile_image_url') }})
    protected: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('protected') }})
    public_metrics: Optional[UserPublicMetrics] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('public_metrics') }})
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('url') }})
    verified: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('verified') }})
    verified_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('verified_type') }})
    withheld: Optional[shared_userwithheld.UserWithheld] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('withheld') }})
    
