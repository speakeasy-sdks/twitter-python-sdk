import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import problem as shared_problem
from ..shared import usersfollowingdeleteresponse as shared_usersfollowingdeleteresponse


@dataclasses.dataclass
class UsersIDUnfollowPathParams:
    source_user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'source_user_id', 'style': 'simple', 'explode': False }})
    target_user_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'target_user_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDUnfollowSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class UsersIDUnfollowRequest:
    path_params: UsersIDUnfollowPathParams = dataclasses.field()
    security: UsersIDUnfollowSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UsersIDUnfollowResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    users_following_delete_response: Optional[shared_usersfollowingdeleteresponse.UsersFollowingDeleteResponse] = dataclasses.field(default=None)
    
