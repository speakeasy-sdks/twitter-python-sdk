import dataclasses
from enum import Enum

class ComplianceJobFieldsParameterEnum(str, Enum):
    CREATED_AT = "created_at"
    DOWNLOAD_EXPIRES_AT = "download_expires_at"
    DOWNLOAD_URL = "download_url"
    ID = "id"
    NAME = "name"
    RESUMABLE = "resumable"
    STATUS = "status"
    TYPE = "type"
    UPLOAD_EXPIRES_AT = "upload_expires_at"
    UPLOAD_URL = "upload_url"

