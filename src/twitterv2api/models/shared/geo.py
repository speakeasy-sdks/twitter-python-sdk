import dataclasses
from typing import Any,Optional
from enum import Enum
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import point as shared_point

class GeoTypeEnum(str, Enum):
    FEATURE = "Feature"


@dataclass_json
@dataclasses.dataclass
class Geo:
    bbox: list[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('bbox') }})
    properties: dict[str, Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('properties') }})
    type: GeoTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    geometry: Optional[shared_point.Point] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('geometry') }})
    
