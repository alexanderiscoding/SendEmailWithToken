from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from starlette.responses import RedirectResponse

from pydantic import BaseModel

# using mailjet Python Library
# https://app.mailjet.com/auth/get_started/developer
from mailjet_rest import Client
api_key = 'your api'
api_secret = 'your api'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')

# using sendgrid Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
sendgrid_client = SendGridAPIClient('your api')

token_access = '5pCGf_bnBHVqJiiUCfq-Ip_jcJczWjrkBBZf1z-StvA'

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins=['*']
)

@app.get("/")
async def index() -> str:
    response = RedirectResponse(url='https://github.com/alexanderiscoding')
    return response

# for use only text replace HTMLPart for "TextPart": "{0}".format(item.content_email)
# for use customid "CustomID": "{0}".format(item.customid) after email content include customid: str in basemodel
class SendMailJet_Info(BaseModel):
    from_email: str
    from_name: str
    to_email: str
    to_name: str
    subject_email: str
    content_email: str

@app.post("/mailjet")
async def index(item: SendMailJet_Info):
    if item.token == token_access:
        data = {
            'Messages': [
                {
                "From": {
                    "Email": "{0}".format(item.from_email),
                    "Name": "{0}".format(item.from_name)
                },
                "To": [
                    {
                    "Email": "{0}".format(item.to_email),
                    "Name": "{0}".format(item.to_name)
                    }
                ],
                "Subject": "{0}".format(item.subject_email),
                "HTMLPart": "{0}".format(item.content_email)
                }
            ]
        }
        response = mailjet.send.create(data=data)
        return response.status_code
    else:
        return 401

# for use only text replace html_content for plain_text_content=PlainTextContent(item.content_email)
class SendMailGrid_Info(BaseModel):
    from_email: str
    from_name: str
    to_email: str
    to_name: str
    subject_email: str
    content_email: str
    token: str

@app.post("/sendgrid")
async def index(item: SendMailGrid_Info):
    if item.token == token_access:
        message = Mail(from_email=From(item.from_email, item.from_name),
                    to_emails=To(item.to_email, item.to_name),
                    subject=Subject(item.subject_email),
                    html_content=HtmlContent(item.content_email))
        response = sendgrid_client.send(message=message)
        return response.status_code
    else:
        return 401