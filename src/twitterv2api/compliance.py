import requests
from typing import Any,Optional
from twitterv2api.models import shared, operations
from . import utils

class Compliance:
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

    
    def create_batch_compliance_job(self, request: operations.CreateBatchComplianceJobRequest) -> operations.CreateBatchComplianceJobResponse:
        r"""Create compliance job
        Creates a compliance for the given job type
        https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/post-compliance-jobs
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/compliance/jobs"
        
        headers = {}
        req_content_type, data, json, files = utils.serialize_request_body(request)
        if req_content_type != "multipart/form-data" and req_content_type != "multipart/mixed":
            headers["content-type"] = req_content_type
        if data is None and json is None:
           raise Exception('request body is required')
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("POST", url, data=data, json=json, files=files, headers=headers)
        content_type = r.headers.get("Content-Type")

        res = operations.CreateBatchComplianceJobResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.CreateComplianceJobResponse])
                res.create_compliance_job_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def get_batch_compliance_job(self, request: operations.GetBatchComplianceJobRequest) -> operations.GetBatchComplianceJobResponse:
        r"""Get Compliance Job
        Returns a single Compliance Job by ID
        https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs-id
        """
        
        base_url = self._server_url
        
        url = utils.generate_url(base_url, "/2/compliance/jobs/{id}", request.path_params)
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetBatchComplianceJobResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2ComplianceJobsIDResponse])
                res.get2_compliance_jobs_id_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def get_tweets_compliance_stream(self, request: operations.GetTweetsComplianceStreamRequest) -> operations.GetTweetsComplianceStreamResponse:
        r"""Tweets Compliance stream
        Streams 100% of compliance data for Tweets
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/tweets/compliance/stream"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetTweetsComplianceStreamResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.tweet_compliance_stream_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def get_tweets_label_stream(self, request: operations.GetTweetsLabelStreamRequest) -> operations.GetTweetsLabelStreamResponse:
        r"""Tweets Label stream
        Streams 100% of labeling events applied to Tweets
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/tweets/label/stream"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetTweetsLabelStreamResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.tweet_label_stream_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def get_users_compliance_stream(self, request: operations.GetUsersComplianceStreamRequest) -> operations.GetUsersComplianceStreamResponse:
        r"""Users Compliance stream
        Streams 100% of compliance data for Users
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/users/compliance/stream"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.GetUsersComplianceStreamResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[Any])
                res.user_compliance_stream_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    
    def list_batch_compliance_jobs(self, request: operations.ListBatchComplianceJobsRequest) -> operations.ListBatchComplianceJobsResponse:
        r"""List Compliance Jobs
        Returns recent Compliance Jobs for a given job type and optional job status
        https://developer.twitter.com/en/docs/twitter-api/compliance/batch-compliance/api-reference/get-compliance-jobs
        """
        
        base_url = self._server_url
        
        url = base_url.removesuffix("/") + "/2/compliance/jobs"
        
        query_params = utils.get_query_params(request.query_params)
        
        client = utils.configure_security_client(self._client, request.security)
        
        r = client.request("GET", url, params=query_params)
        content_type = r.headers.get("Content-Type")

        res = operations.ListBatchComplianceJobsResponse(status_code=r.status_code, content_type=content_type)
        
        if r.status_code == 200:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Get2ComplianceJobsResponse])
                res.get2_compliance_jobs_response = out
        else:
            if utils.match_content_type(content_type, "application/json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Error])
                res.error = out
            if utils.match_content_type(content_type, "application/problem+json"):
                out = utils.unmarshal_json(r.text, Optional[shared.Problem])
                res.problem = out

        return res

    