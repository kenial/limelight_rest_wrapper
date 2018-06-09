import sys
import time
import urllib
import hmac
import hashlib
import requests
import json

class LimelightRESTWrapper(object):
    def __init__(self, limelight_user_id, api_key):
        super(LimelightRESTWrapper, self).__init__()
        self.llnw_security_principal = limelight_user_id
        self.api_key = api_key

    @classmethod
    def generate_security_token(cls, url, http_method, api_key, query_params=None, post_data=None, timestamp=None):
        datastring = http_method + url
        if query_params != None:
            datastring += query_params
        datastring += timestamp
        if post_data != None:
            datastring += post_data
        # if python 3
        if sys.version_info > (3,0):
            token = hmac.new(bytes.fromhex(api_key), msg=datastring.encode("utf-8"), digestmod=hashlib.sha256).hexdigest()
        else:
            token = hmac.new(api_key.decode("hex"), msg=datastring, digestmod=hashlib.sha256).hexdigest()
        return token

    def api_get(self, endpoint, query_params):
        if endpoint == None or endpoint.strip() == "":
            raise Exception("REST API endpoint is needed")
        cur_timestamp = str(int(round(time.time()*1000)))
        # if python 3
        if sys.version_info > (3,0):
            url_encoded_query_params = urllib.parse.urlencode(query_params)
        else:
            url_encoded_query_params = urllib.urlencode(query_params)
        security_token = LimelightRESTWrapper.generate_security_token(url=endpoint, http_method="GET", query_params=url_encoded_query_params, api_key=self.api_key, timestamp=cur_timestamp)
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'X-llnw-security-principal': self.llnw_security_principal,
            'X-llnw-security-token': security_token,
            'X-llnw-security-timestamp': cur_timestamp,
        }
        res = requests.get(endpoint, params=query_params, headers=headers, verify=False)
        return res

    def api_post(self, endpoint, post_data):
        if endpoint == None or endpoint.strip() == "":
            raise Exception("REST API endpoint is needed")
        cur_timestamp = str(int(round(time.time()*1000)))
        post_data_json = json.dumps(post_data, separators=(",",":"))
        security_token = LimelightRESTWrapper.generate_security_token(url=endpoint, http_method="POST", post_data=post_data_json, api_key=self.api_key, timestamp=cur_timestamp)
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'X-llnw-security-principal': self.llnw_security_principal,
            'X-llnw-security-token': security_token,
            'X-llnw-security-timestamp': cur_timestamp,
        }
        res = requests.post(endpoint, data=post_data_json, headers=headers, verify=False)
        return res
