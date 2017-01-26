import json

import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.vendored.requests import Session

LEX_URL = "https://runtime.lex.us-east-1.amazonaws.com"
BOT_TEMPLATE_STRING = "/bot/{}/alias/{}/user/{}/"
REGION = 'us-east-1'
B3_SESSION = boto3.Session()

class LexSession():
    def __init__(self, bot, alias, user):
        self.url = LEX_URL + BOT_TEMPLATE_STRING.format(bot, alias, user)
        self.session = Session()
    
    def request(self, url, payload):
        request = AWSRequest(method="POST", url=url, data=json.dumps(payload))
        SigV4Auth(
            B3_SESSION.get_credentials(),
            'lex',
            REGION
        ).add_auth(request)
        return self.session.send(request.prepare())
        
    def text(self, input_text, session_attributes=None):
        url = self.url + 'text'
        payload = {"inputText": input_text, "sessionAttributes": session_attributes}
        return self.request(url, payload).json()
    