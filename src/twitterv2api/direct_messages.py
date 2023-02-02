import requests
from typing import Optional
from twitterv2api.models import shared, operations
from . import utils

class DirectMessages:
    _client: requests.Session
    _security_client: requests.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests.Session, security_client: requests.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version

    
    def dm_conversation_by_id_event_id_create(self, request: operations.DmConversationByIDEventIDCreateRequest) -> operations.DmConversationByIDEventIDCreateResponse:
        r"""Send a new message to a DM Conversation
        Creates a new message for a DM Conversation specified by DM Conversation ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/dm_conversations/{dm_conversation_id}/messages", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DmConversationByIDEventIDCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateDmEventResponse])
                res.create_dm_event_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def dm_conversation_id_create(self, request: operations.DmConversationIDCreateRequest) -> operations.DmConversationIDCreateResponse:
        r"""Create a new DM Conversation
        Creates a new DM Conversation.
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/dm_conversations"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DmConversationIDCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateDmEventResponse])
                res.create_dm_event_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def dm_conversation_with_user_event_id_create(self, request: operations.DmConversationWithUserEventIDCreateRequest) -> operations.DmConversationWithUserEventIDCreateResponse:
        r"""Send a new message to a user
        Creates a new message for a DM Conversation with a participant user by ID
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/dm_conversations/with/{participant_id}/messages", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.DmConversationWithUserEventIDCreateResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 201:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateDmEventResponse])
                res.create_dm_event_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def get_dm_conversations_id_dm_events(self, request: operations.GetDmConversationsIDDmEventsRequest) -> operations.GetDmConversationsIDDmEventsResponse:
        r"""Get DM Events for a DM Conversation
        Returns DM Events for a DM Conversation
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/dm_conversations/{id}/dm_events", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDmConversationsIDDmEventsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2DmConversationsIDDmEventsResponse])
                res.get2_dm_conversations_id_dm_events_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def get_dm_conversations_with_participant_id_dm_events(self, request: operations.GetDmConversationsWithParticipantIDDmEventsRequest) -> operations.GetDmConversationsWithParticipantIDDmEventsResponse:
        r"""Get DM Events for a DM Conversation
        Returns DM Events for a DM Conversation
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/dm_conversations/with/{participant_id}/dm_events", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDmConversationsWithParticipantIDDmEventsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2DmConversationsWithParticipantIDDmEventsResponse])
                res.get2_dm_conversations_with_participant_id_dm_events_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def get_dm_events(self, request: operations.GetDmEventsRequest) -> operations.GetDmEventsResponse:
        r"""Get recent DM Events
        Returns recent DM Events across DM conversations
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/dm_events"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetDmEventsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2DmEventsResponse])
                res.get2_dm_events_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    