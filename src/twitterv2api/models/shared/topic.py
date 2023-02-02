import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class Topic:
    r"""Topic
    The topic of a Space, as selected by its creator.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    
