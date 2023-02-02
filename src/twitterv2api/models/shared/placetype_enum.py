import dataclasses
from enum import Enum

class PlaceTypeEnum(str, Enum):
    POI = "poi"
    NEIGHBORHOOD = "neighborhood"
    CITY = "city"
    ADMIN = "admin"
    COUNTRY = "country"
    UNKNOWN = "unknown"

