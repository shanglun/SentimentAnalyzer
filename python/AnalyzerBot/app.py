from flask import Flask, request
import datetime

app = Flask(__name__)


@app.route('/analyze', methods=['POST'])
def analyze():
    with open('logfile.txt', 'a') as fp_log:
        fp_log.write('endpoint hit %s \n' % datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return "Got it"

app.run(debug=True)
