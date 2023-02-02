import dataclasses
from typing import Optional
from enum import Enum
from dataclasses_json import dataclass_json
from twitterv2api import utils
from ..shared import geo as shared_geo
from ..shared import placetype_enum as shared_placetype_enum


@dataclass_json
@dataclasses.dataclass
class Place:
    full_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('full_name') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    contained_within: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('contained_within') }})
    country: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('country') }})
    country_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('country_code') }})
    geo: Optional[shared_geo.Geo] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('geo') }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    place_type: Optional[shared_placetype_enum.PlaceTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('place_type') }})
    
