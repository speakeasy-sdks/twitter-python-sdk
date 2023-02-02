import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import listpinnedrequest as shared_listpinnedrequest
from ..shared import error as shared_error
from ..shared import listpinnedresponse as shared_listpinnedresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class ListUserPinPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListUserPinSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class ListUserPinRequest:
    path_params: ListUserPinPathParams = dataclasses.field()
    request: shared_listpinnedrequest.ListPinnedRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    security: ListUserPinSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ListUserPinResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    list_pinned_response: Optional[shared_listpinnedresponse.ListPinnedResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
