import requests
from typing import Optional
from twitterv2api.models import shared, operations
from . import utils

class Bookmarks:
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

    
    def get_users_id_bookmarks(self, request: operations.GetUsersIDBookmarksRequest) -> operations.GetUsersIDBookmarksResponse:
        r"""Bookmarks by User
        Returns Tweet objects that have been bookmarked by the requesting User
        https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/get-users-id-bookmarks
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/bookmarks", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetUsersIDBookmarksResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2UsersIDBookmarksResponse])
                res.get2_users_id_bookmarks_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def post_users_id_bookmarks(self, request: operations.PostUsersIDBookmarksRequest) -> operations.PostUsersIDBookmarksResponse:
        r"""Add Tweet to Bookmarks
        Adds a Tweet (ID in the body) to the requesting User's (in the path) bookmarks
        https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/post-users-id-bookmarks
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/bookmarks", request.path_params)
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.PostUsersIDBookmarksResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BookmarkMutationResponse])
                res.bookmark_mutation_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def users_id_bookmarks_delete(self, request: operations.UsersIDBookmarksDeleteRequest) -> operations.UsersIDBookmarksDeleteResponse:
        r"""Remove a bookmarked Tweet
        Removes a Tweet from the requesting User's bookmarked Tweets.
        https://developer.twitter.com/en/docs/twitter-api/tweets/bookmarks/api-reference/delete-users-id-bookmarks-tweet_id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/users/{id}/bookmarks/{tweet_id}", request.path_params)
        
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("DELETE", url)
        content_type = r.headers.get("Content-Type")

        res = operations.UsersIDBookmarksDeleteResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.BookmarkMutationResponse])
                res.bookmark_mutation_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    