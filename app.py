#!TwitterLifterAPI/bin/python
import os
import tweepy 
from flask import Flask
from flask import send_from_directory
from TwitterLifterAPI.EntityLinker import entitylinker
from TwitterLifterAPI import twitterlifterapi

CONSUMER_KEY = "AXM5In6hWf6aXn0IO7EjJptm1"
CONSUMER_SECRET = "nmn0xLhXCbhj0dJuhlplKrAnsiXTbLQXT52r0UtOyuUBUKjbjf"
ACCESS_TOKEN = "803329880238804992-ZbrgtA4jZSsb3SIIcElaawKvpCQVHlf"
ACCESS_TOKEN_SECRET = "NFaTiTzYBabHQAGUxz9QNb6wyZOMaGhuGIS1oe6lN8wUn"

app = Flask(__name__)

@app.route('/')
def index():
    return "API Instructions:<br>Input: 193.70.1.232:5000/TWEETID<br>Output: RDF processed result of the tweet (JSON formated)"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<id>')
def lifter(id):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    tweet = api.get_status(id)
    return twitterlifterapi.lift(tweet)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded="True")
