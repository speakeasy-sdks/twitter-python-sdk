import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import listmutateresponse as shared_listmutateresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class ListRemoveMemberPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'user_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListRemoveMemberSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class ListRemoveMemberRequest:
    path_params: ListRemoveMemberPathParams = dataclasses.field()
    security: ListRemoveMemberSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ListRemoveMemberResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    list_mutate_response: Optional[shared_listmutateresponse.ListMutateResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
