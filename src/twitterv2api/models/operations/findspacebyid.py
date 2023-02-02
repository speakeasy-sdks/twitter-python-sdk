import dataclasses
from typing import Optional
from enum import Enum
from ..shared import spaceexpansionsparameter_enum as shared_spaceexpansionsparameter_enum
from ..shared import spacefieldsparameter_enum as shared_spacefieldsparameter_enum
from ..shared import topicfieldsparameter_enum as shared_topicfieldsparameter_enum
from ..shared import userfieldsparameter_enum as shared_userfieldsparameter_enum
from ..shared import security as shared_security
from ..shared import security as shared_security
from ..shared import error as shared_error
from ..shared import get2spacesidresponse as shared_get2spacesidresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class FindSpaceByIDPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class FindSpaceByIDQueryParams:
    expansions: Optional[list[shared_spaceexpansionsparameter_enum.SpaceExpansionsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'expansions', 'style': 'form', 'explode': False }})
    space_fields: Optional[list[shared_spacefieldsparameter_enum.SpaceFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'space.fields', 'style': 'form', 'explode': False }})
    topic_fields: Optional[list[shared_topicfieldsparameter_enum.TopicFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'topic.fields', 'style': 'form', 'explode': False }})
    user_fields: Optional[list[shared_userfieldsparameter_enum.UserFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user.fields', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class FindSpaceByIDSecurity:
    bearer_token: Optional[shared_security.SchemeBearerToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    

@dataclasses.dataclass
class FindSpaceByIDRequest:
    path_params: FindSpaceByIDPathParams = dataclasses.field()
    query_params: FindSpaceByIDQueryParams = dataclasses.field()
    security: FindSpaceByIDSecurity = dataclasses.field()
    

@dataclasses.dataclass
class FindSpaceByIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_spaces_id_response: Optional[shared_get2spacesidresponse.Get2SpacesIDResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
