import os 
from twilio.rest import Client 
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

from_number =   '+18886815709'
to_number =     '+19788814542'

def send_message(intruder_detected):
    msg = "Intruder Alert! 👽" if intruder_detected else "Welcome!"
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body=msg,
                        from_=from_number,
                        to=to_number
                    )
    # print(message.sid)

# send_message(True)