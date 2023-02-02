import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import userslikescreaterequest as shared_userslikescreaterequest
from ..shared import error as shared_error
from ..shared import problem as shared_problem
from ..shared import userslikescreateresponse as shared_userslikescreateresponse


@dataclasses.dataclass
class UsersIDLikePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDLikeSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class UsersIDLikeRequest:
    path_params: UsersIDLikePathParams = dataclasses.field()
    security: UsersIDLikeSecurity = dataclasses.field()
    request: Optional[shared_userslikescreaterequest.UsersLikesCreateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UsersIDLikeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    users_likes_create_response: Optional[shared_userslikescreateresponse.UsersLikesCreateResponse] = dataclasses.field(default=None)
    
