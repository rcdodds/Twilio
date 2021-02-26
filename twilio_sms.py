# Imports
from twilio.rest import Client
import json


# Send a motivational text
def send_text(text_body, to_number=None):
    # Read in Twilio project credentials from JSON file
    with open('twilio_credentials.json', mode='r') as file:
        twilio_dict = json.load(file)

    # Start a Twilio client using the project credentials
    client = Client(twilio_dict['account_sid'], twilio_dict['auth_token'])

    # If recipient is not specified, use the default from th project credentials
    if not to_number:
        to_number = twilio_dict['to_number']

    # Send text
    client.messages.create(
        body=text_body,
        from_=twilio_dict['from_number'],
        to=to_number
    )
