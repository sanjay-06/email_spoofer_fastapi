from __future__ import print_function
from importlib.resources import contents
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
class Spoof:
    def __init__(self) -> None:
        self.configuration = os.environ.get("YOUR_CONFIGURATION")
        self.configuration.api_key['api-key'] = os.environ.get("YOUR_API_KEY")
        self.api_instance = os.environ.get("YOUR_TRANSACTION_CONFIGURATION")

    def createmail(self,sender,sendername,reciever,recievername,subject,body):
        self.subject = subject
        self.html_content = "<html><body><p>"+body+"</p></body></html>"
        self.sender = {"name":sendername,"email":sender}
        self.to = [{"name":recievername,"email":reciever}]
        
    def sendmail(self):
        self.send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(os.environ.get("CONTENTS_YOU_SEND"))
    
    def logresponse(self):
        try:
            api_response = self.api_instance.send_transac_email(self.send_smtp_email)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
