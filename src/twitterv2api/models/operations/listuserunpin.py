import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import listunpinresponse as shared_listunpinresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class ListUserUnpinPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    list_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'list_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListUserUnpinSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class ListUserUnpinRequest:
    path_params: ListUserUnpinPathParams = dataclasses.field()
    security: ListUserUnpinSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ListUserUnpinResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    list_unpin_response: Optional[shared_listunpinresponse.ListUnpinResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
