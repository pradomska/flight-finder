from twilio.rest import Client

TWILIO_SID = "ACed99dee86823f4e65269e783a7604e42"
TWILIO_AUTH_TOKEN = "326ccefd7adab7a75138b24830f66492"
TWILIO_VIRTUAL_NUMBER = "+16205268968"
TWILIO_VERIFIED_NUMBER = "+48600171513"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
