import os
import datetime
from flask import Flask, request
from twilio.rest import TwilioRestClient

on_call = os.getenv('ON_CALL')

client = TwilioRestClient(os.getenv('TWILIO_ACCOUNT_KEY'), os.getenv('TWILIO_API_KEY'))


def send_message(body):
    client.messages.create(
        to=on_call,
        from_=os.getenv('TWILIO_PHONE_NUMBER'),
        body=body
    )

app = Flask(__name__)


@app.route('/analyze', methods=['POST'])
def analyze():
    with open('logfile.txt', 'a') as fp_log:
        fp_log.write('endpoint hit %s \n' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return "Got it"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
