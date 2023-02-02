import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import problem as shared_problem
from ..shared import tweetdeleteresponse as shared_tweetdeleteresponse


@dataclasses.dataclass
class DeleteTweetByIDPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteTweetByIDSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class DeleteTweetByIDRequest:
    path_params: DeleteTweetByIDPathParams = dataclasses.field()
    security: DeleteTweetByIDSecurity = dataclasses.field()
    

@dataclasses.dataclass
class DeleteTweetByIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    tweet_delete_response: Optional[shared_tweetdeleteresponse.TweetDeleteResponse] = dataclasses.field(default=None)
    
