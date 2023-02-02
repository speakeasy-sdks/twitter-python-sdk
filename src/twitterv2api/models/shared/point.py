import dataclasses
from enum import Enum
from dataclasses_json import dataclass_json
from twitterv2api import utils

class PointTypeEnum(str, Enum):
    POINT = "Point"


@dataclass_json
@dataclasses.dataclass
class Point:
    r"""Point
    A [GeoJson Point](https://tools.ietf.org/html/rfc7946#section-3.1.2) geometry object.
    """
    
    coordinates: list[float] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('coordinates') }})
    type: PointTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('type') }})
    
