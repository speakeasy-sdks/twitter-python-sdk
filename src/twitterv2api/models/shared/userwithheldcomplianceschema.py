import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import usertakedowncomplianceschema as shared_usertakedowncomplianceschema


@dataclass_json
@dataclasses.dataclass
class UserWithheldComplianceSchema:
    user_withheld: shared_usertakedowncomplianceschema.UserTakedownComplianceSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('user_withheld') }})
    
