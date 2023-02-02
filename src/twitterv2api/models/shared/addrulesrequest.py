import dataclasses
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import rulenoid as shared_rulenoid


@dataclass_json
@dataclasses.dataclass
class AddRulesRequest:
    r"""AddRulesRequest
    A request to add a user-specified stream filtering rule.
    """
    
    add: list[shared_rulenoid.RuleNoID] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('add') }})
    
