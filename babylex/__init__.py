import json

import boto3
import base64
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.vendored.requests import Session

REGION = 'us-east-1'
SHA256_EMPTY_HASH = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'


class LexContentSigV4Auth(SigV4Auth):
    def payload(self, request):
        return SHA256_EMPTY_HASH


class LexSession:
    LEX_URL = "https://runtime.lex.{}.amazonaws.com/bot/{}/alias/{}/user/{}/"

    def __init__(self, bot, alias, user, creds=None, region='us-east-1'):
        if not creds:
            self.creds = boto3.Session().get_credentials()
        # region can be changed to refer to boto3.Session().region_name
        self.region = region
        self.url = LexSession.LEX_URL.format(region, bot, alias, user)
        self.session = Session()

    def text(self, input_text, session_attributes=None):
        """input_text will be passed to your lex bot"""
        url = self.url + 'text'
        payload = json.dumps({
            "inputText": input_text,
            "sessionAttributes": session_attributes
        })
        request = AWSRequest(method="POST", url=url, data=payload)
        SigV4Auth(self.creds, 'lex', self.region).add_auth(request)

        return self.session.send(request.prepare()).json()

    def content(self, data, ctype, accept, session_attributes=None):
        """This will post any content to your lex bot

        Valid values for ctype and accept are found here:
        http://docs.aws.amazon.com/lex/latest/dg/API_PostContent.html"""
        url = self.url + 'content'
        request = AWSRequest(method="POST", url=url, data=data)
        request.headers["accept"] = accept
        request.headers["content-type"] = ctype
        if session_attributes:
            request.headers.add_header(
                "x-amz-lex-session-attributes",
                base64.b64encode(json.dumps(session_attributes))
            )
        LexContentSigV4Auth(self.creds, 'lex', self.region).add_auth(request)
        prepared = request.prepare()
        prepared.body = data

        return self.session.send(prepared)
