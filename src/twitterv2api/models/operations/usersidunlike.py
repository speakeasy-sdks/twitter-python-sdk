import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import problem as shared_problem
from ..shared import userslikesdeleteresponse as shared_userslikesdeleteresponse


@dataclasses.dataclass
class UsersIDUnlikePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    tweet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tweet_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDUnlikeSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class UsersIDUnlikeRequest:
    path_params: UsersIDUnlikePathParams = dataclasses.field()
    security: UsersIDUnlikeSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UsersIDUnlikeResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    users_likes_delete_response: Optional[shared_userslikesdeleteresponse.UsersLikesDeleteResponse] = dataclasses.field(default=None)
    
