import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import problem as shared_problem
from ..shared import usersretweetsdeleteresponse as shared_usersretweetsdeleteresponse


@dataclasses.dataclass
class UsersIDUnretweetsPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    source_tweet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'source_tweet_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDUnretweetsSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class UsersIDUnretweetsRequest:
    path_params: UsersIDUnretweetsPathParams = dataclasses.field()
    security: UsersIDUnretweetsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UsersIDUnretweetsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    users_retweets_delete_response: Optional[shared_usersretweetsdeleteresponse.UsersRetweetsDeleteResponse] = dataclasses.field(default=None)
    
