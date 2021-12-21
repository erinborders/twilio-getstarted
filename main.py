import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='insert twilio trial number here',
                     to='insert personal phone number here'
                 )
print(message.sid)
