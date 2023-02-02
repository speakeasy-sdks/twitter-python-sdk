import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import userprofilemodificationobjectschema as shared_userprofilemodificationobjectschema


@dataclass_json
@dataclasses.dataclass
class UserProfileModificationComplianceSchema:
    user_profile_modification: shared_userprofilemodificationobjectschema.UserProfileModificationObjectSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('user_profile_modification') }})
    
