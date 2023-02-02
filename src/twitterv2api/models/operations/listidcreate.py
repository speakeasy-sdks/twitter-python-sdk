import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import listcreaterequest as shared_listcreaterequest
from ..shared import error as shared_error
from ..shared import listcreateresponse as shared_listcreateresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class ListIDCreateSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class ListIDCreateRequest:
    security: ListIDCreateSecurity = dataclasses.field()
    request: Optional[shared_listcreaterequest.ListCreateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class ListIDCreateResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    list_create_response: Optional[shared_listcreateresponse.ListCreateResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
