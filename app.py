import json
import os
from flask import Flask, request
from flask_cors import CORS
from tweets import Tweet

app = Flask(__name__)
CORS(app)

@app.route("/tweets", methods=['POST'])
def score():
    try:
        messages = request.get_json()['messages']
        message = messages[0]
        if (message['key'] == 'TWEETS_GET'):
            symbol = message['value']['symbol']
            from_dt = message['value']['from_dt']
            twt = Tweet(symbol)
            result = twt.SearchTweets(since=from_dt)
            return json.dumps(result)
    except (Exception) as error:
        print(error)
    return "OK"


@app.route("/live/ping", methods=['GET'])
def test():
    return "OK"


if __name__ == '__main__':
    hostEnv = os.getenv('HOST_URL', '0.0.0.0')
    portEnv = os.getenv('HOST_PORT', 8101)
    app.run(host=hostEnv, port=portEnv, debug=False, threaded=True)
