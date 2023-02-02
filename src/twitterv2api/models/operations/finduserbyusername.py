import dataclasses
from typing import Optional
from enum import Enum
from ..shared import userexpansionsparameter_enum as shared_userexpansionsparameter_enum
from ..shared import tweetfieldsparameter_enum as shared_tweetfieldsparameter_enum
from ..shared import userfieldsparameter_enum as shared_userfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2usersbyusernameusernameresponse as shared_get2usersbyusernameusernameresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class FindUserByUsernamePathParams:
    username: str = dataclasses.field(metadata={'path_param': { 'field_name': 'username', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FindUserByUsernameQueryParams:
    expansions: Optional[list[shared_userexpansionsparameter_enum.UserExpansionsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'expansions', 'style': 'form', 'explode': False }})
    tweet_fields: Optional[list[shared_tweetfieldsparameter_enum.TweetFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'tweet.fields', 'style': 'form', 'explode': False }})
    user_fields: Optional[list[shared_userfieldsparameter_enum.UserFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user.fields', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class FindUserByUsernameSecurity:
    bearer_token: Optional[shared_security.SchemeBearerToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class FindUserByUsernameRequest:
    path_params: FindUserByUsernamePathParams = dataclasses.field()
    query_params: FindUserByUsernameQueryParams = dataclasses.field()
    security: FindUserByUsernameSecurity = dataclasses.field()
    

@dataclasses.dataclass
class FindUserByUsernameResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_users_by_username_username_response: Optional[shared_get2usersbyusernameusernameresponse.Get2UsersByUsernameUsernameResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
