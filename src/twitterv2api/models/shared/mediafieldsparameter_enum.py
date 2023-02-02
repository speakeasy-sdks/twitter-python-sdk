import dataclasses
from enum import Enum

class MediaFieldsParameterEnum(str, Enum):
    ALT_TEXT = "alt_text"
    DURATION_MS = "duration_ms"
    HEIGHT = "height"
    MEDIA_KEY = "media_key"
    NON_PUBLIC_METRICS = "non_public_metrics"
    ORGANIC_METRICS = "organic_metrics"
    PREVIEW_IMAGE_URL = "preview_image_url"
    PROMOTED_METRICS = "promoted_metrics"
    PUBLIC_METRICS = "public_metrics"
    TYPE = "type"
    URL = "url"
    VARIANTS = "variants"
    WIDTH = "width"

