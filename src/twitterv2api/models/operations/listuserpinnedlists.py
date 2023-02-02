import dataclasses
from typing import Optional
from enum import Enum
from ..shared import listexpansionsparameter_enum as shared_listexpansionsparameter_enum
from ..shared import listfieldsparameter_enum as shared_listfieldsparameter_enum
from ..shared import userfieldsparameter_enum as shared_userfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2usersidpinnedlistsresponse as shared_get2usersidpinnedlistsresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class ListUserPinnedListsPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListUserPinnedListsQueryParams:
    expansions: Optional[list[shared_listexpansionsparameter_enum.ListExpansionsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'expansions', 'style': 'form', 'explode': False }})
    list_fields: Optional[list[shared_listfieldsparameter_enum.ListFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'list.fields', 'style': 'form', 'explode': False }})
    user_fields: Optional[list[shared_userfieldsparameter_enum.UserFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user.fields', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class ListUserPinnedListsSecurity:
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class ListUserPinnedListsRequest:
    path_params: ListUserPinnedListsPathParams = dataclasses.field()
    query_params: ListUserPinnedListsQueryParams = dataclasses.field()
    security: ListUserPinnedListsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ListUserPinnedListsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_users_id_pinned_lists_response: Optional[shared_get2usersidpinnedlistsresponse.Get2UsersIDPinnedListsResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
