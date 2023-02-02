import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import userscrubgeoobjectschema as shared_userscrubgeoobjectschema


@dataclass_json
@dataclasses.dataclass
class UserScrubGeoSchema:
    scrub_geo: shared_userscrubgeoobjectschema.UserScrubGeoObjectSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('scrub_geo') }})
    
