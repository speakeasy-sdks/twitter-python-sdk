import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class DeleteRulesRequestDelete:
    r"""DeleteRulesRequestDelete
    IDs and values of all deleted user-specified stream filtering rules.
    """
    
    ids: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ids') }})
    values: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('values') }})
    

@dataclass_json
@dataclasses.dataclass
class DeleteRulesRequest:
    r"""DeleteRulesRequest
    A response from deleting user-specified stream filtering rules.
    """
    
    delete: DeleteRulesRequestDelete = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('delete') }})
    
