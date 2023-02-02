import requests
from typing import Optional
from twitterv2api.models import shared, operations
from . import utils

class Spaces:
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

    
    def find_space_by_id(self, request: operations.FindSpaceByIDRequest) -> operations.FindSpaceByIDResponse:
        r"""Space lookup by Space ID
        Returns a variety of information about the Space specified by the requested ID
        https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/spaces/{id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FindSpaceByIDResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2SpacesIDResponse])
                res.get2_spaces_id_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def find_spaces_by_creator_ids(self, request: operations.FindSpacesByCreatorIdsRequest) -> operations.FindSpacesByCreatorIdsResponse:
        r"""Space lookup by their creators
        Returns a variety of information about the Spaces created by the provided User IDs
        https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-by-creator-ids
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/spaces/by/creator_ids"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FindSpacesByCreatorIdsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2SpacesByCreatorIdsResponse])
                res.get2_spaces_by_creator_ids_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def find_spaces_by_ids(self, request: operations.FindSpacesByIdsRequest) -> operations.FindSpacesByIdsResponse:
        r"""Space lookup up Space IDs
        Returns a variety of information about the Spaces specified by the requested IDs
        https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/spaces"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.FindSpacesByIdsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2SpacesResponse])
                res.get2_spaces_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def search_spaces(self, request: operations.SearchSpacesRequest) -> operations.SearchSpacesResponse:
        r"""Search for Spaces
        Returns Spaces that match the provided query.
        https://developer.twitter.com/en/docs/twitter-api/spaces/search/api-reference/get-spaces-search
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/spaces/search"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.SearchSpacesResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2SpacesSearchResponse])
                res.get2_spaces_search_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def space_buyers(self, request: operations.SpaceBuyersRequest) -> operations.SpaceBuyersResponse:
        r"""Retrieve the list of Users who purchased a ticket to the given space
        Retrieves the list of Users who purchased a ticket to the given space
        https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-buyers
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/spaces/{id}/buyers", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.SpaceBuyersResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2SpacesIDBuyersResponse])
                res.get2_spaces_id_buyers_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def space_tweets(self, request: operations.SpaceTweetsRequest) -> operations.SpaceTweetsResponse:
        r"""Retrieve Tweets from a Space.
        Retrieves Tweets shared in the specified Space.
        https://developer.twitter.com/en/docs/twitter-api/spaces/lookup/api-reference/get-spaces-id-tweets
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/spaces/{id}/tweets", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.SpaceTweetsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2SpacesIDTweetsResponse])
                res.get2_spaces_id_tweets_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    