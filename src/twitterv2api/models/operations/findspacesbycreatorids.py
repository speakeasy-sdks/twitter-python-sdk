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
from ..shared import get2spacesbycreatoridsresponse as shared_get2spacesbycreatoridsresponse
from ..shared import problem as shared_problem


@dataclasses.dataclass
class FindSpacesByCreatorIdsQueryParams:
    user_ids: list[str] = dataclasses.field(metadata={'query_param': { 'field_name': 'user_ids', 'style': 'form', 'explode': True }})
    expansions: Optional[list[shared_spaceexpansionsparameter_enum.SpaceExpansionsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'expansions', 'style': 'form', 'explode': False }})
    space_fields: Optional[list[shared_spacefieldsparameter_enum.SpaceFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'space.fields', 'style': 'form', 'explode': False }})
    topic_fields: Optional[list[shared_topicfieldsparameter_enum.TopicFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'topic.fields', 'style': 'form', 'explode': False }})
    user_fields: Optional[list[shared_userfieldsparameter_enum.UserFieldsParameterEnum]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'user.fields', 'style': 'form', 'explode': False }})
    

@dataclasses.dataclass
class FindSpacesByCreatorIdsSecurity:
    bearer_token: Optional[shared_security.SchemeBearerToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    o_auth2_user_token: Optional[shared_security.SchemeOAuth2UserToken] = dataclasses.field(default=None, metadata={'security': { 'scheme': True, 'type': 'oauth2' }})
    

@dataclasses.dataclass
class FindSpacesByCreatorIdsRequest:
    query_params: FindSpacesByCreatorIdsQueryParams = dataclasses.field()
    security: FindSpacesByCreatorIdsSecurity = dataclasses.field()
    

@dataclasses.dataclass
class FindSpacesByCreatorIdsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error: Optional[shared_error.Error] = dataclasses.field(default=None)
    get2_spaces_by_creator_ids_response: Optional[shared_get2spacesbycreatoridsresponse.Get2SpacesByCreatorIdsResponse] = dataclasses.field(default=None)
    problem: Optional[shared_problem.Problem] = dataclasses.field(default=None)
    
