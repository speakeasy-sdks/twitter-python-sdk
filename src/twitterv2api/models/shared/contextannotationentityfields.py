import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from twitterv2api import utils


@dataclass_json
@dataclasses.dataclass
class ContextAnnotationEntityFields:
    r"""ContextAnnotationEntityFields
    Represents the data for the context annotation entity.
    """
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('description') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    
