import dataclasses
from typing import Optional
from enum import Enum
from ..shared import listexpansionsparameter_enum as shared_listexpansionsparameter_enum
from ..shared import listfieldsparameter_enum as shared_listfieldsparameter_enum
from ..shared import userfieldsparameter_enum as shared_userfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2listsidresponse as shared_get2listsidresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class ListIDGetPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class ListIDGetQueryParams:
    expansions: Optional[list[shared_listexpansionsparameter_enum.ListExpansionsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'expansions', 'style': 'form', 'explode': False }})
    list_fields: Optional[list[shared_listfieldsparameter_enum.ListFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'list.fields', 'style': 'form', 'explode': False }})
    user_fields: Optional[list[shared_userfieldsparameter_enum.UserFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user.fields', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class ListIDGetSecurity:
    bearer_token: Optional[shared_security.SchemeBearerToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    user_token: Optional[shared_security.SchemeUserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'basic' }})
    

@dataclasses.dataclass
class ListIDGetRequest:
    path_params: ListIDGetPathParams = dataclasses.field()
    query_params: ListIDGetQueryParams = dataclasses.field()
    security: ListIDGetSecurity = dataclasses.field()
    

@dataclasses.dataclass
class ListIDGetResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_lists_id_response: Optional[shared_get2listsidresponse.Get2ListsIDResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
