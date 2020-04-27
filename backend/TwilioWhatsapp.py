import os
from twilio.rest import Client

# https://www.twilio.com/docs/libraries/reference/twilio-python/index.html

def send_whatsapp_message(to_whatsapp_number, message_body):
    client = Client()

    from_whatsapp_number = "whatsapp:+14155238886"
    #  set environment variable https://superuser.com/questions/555081/ubuntu-environment-setting-for-gui-session-or-making-the-same-with-terminal
    to_whatsapp_number="whatsapp:" + to_whatsapp_number

    client.messages.create(body=message_body, from_=from_whatsapp_number, to=to_whatsapp_number)


