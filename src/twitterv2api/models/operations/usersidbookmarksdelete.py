import dataclasses
from typing import Optional
from ..shared import security as shared_security
from ..shared import bookmarkmutationresponse as shared_bookmarkmutationresponse
from ..shared import error as shared_error
from ..shared import problem as shared_problem


@dataclasses.dataclass
class UsersIDBookmarksDeletePathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    tweet_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tweet_id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class UsersIDBookmarksDeleteSecurity:
    o_auth2_user_token: shared_security.SchemeOAuth2UserToken = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    

@dataclasses.dataclass
class UsersIDBookmarksDeleteRequest:
    path_params: UsersIDBookmarksDeletePathParams = dataclasses.field()
    security: UsersIDBookmarksDeleteSecurity = dataclasses.field()
    

@dataclasses.dataclass
class UsersIDBookmarksDeleteResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    bookmark_mutation_response: Optional[shared_bookmarkmutationresponse.BookmarkMutationResponse] = dataclasses.field(default=None)
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
