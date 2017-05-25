import os
import datetime
from flask import Flask, request
from twilio.rest import Client
import client

on_call = os.getenv('ON_CALL')
twilio_client = Client(os.getenv('TWILIO_ACCOUNT_KEY'), os.getenv('TWILIO_API_KEY'))


def send_message(body):
    twilio_client.messages.create(
        to=on_call,
        from_=os.getenv('TWILIO_PHONE_NUMBER'),
        body=body
    )

app = Flask(__name__)


@app.route('/analyze', methods=['POST'])
def analyze():
    text = str(request.form.get('text'))
    sentiment_client = client.SentimentClient()
    text.replace('\n', '')  # remove all new lines
    sentences = text.rstrip('.').split('.')  # remove the last period before splitting
    negative_sentences = [
        sentence for sentence in sentences
        if sentiment_client.analyze(sentence).rstrip() in ['Negative', 'Very negative']  # remove newline char
    ]
    urgent = len(negative_sentences) / len(sentences) > 0.75
    with open('logfile.txt', 'a') as fp_log:
        fp_log.write("Received: " % request.form.get('text'))
        fp_log.write("urgent = %s" % (str(urgent)))
        fp_log.write("\n")

    return "Got it"


@app.route('/')
def health_check():
    return "Alive"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
