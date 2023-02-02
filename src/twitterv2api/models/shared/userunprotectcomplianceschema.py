import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import usercomplianceschema as shared_usercomplianceschema


@dataclass_json
@dataclasses.dataclass
class UserUnprotectComplianceSchema:
    user_unprotect: shared_usercomplianceschema.UserComplianceSchema = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('user_unprotect') }})
    
