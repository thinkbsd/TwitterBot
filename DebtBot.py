# Twitter bot that will tweet "Hello World!" (and eventually the national debt daily).
from twython import Twython

API_KEY = 'YOUR TWITTER API KEY'
API_SECRET = 'YOUR TWITTER API SECRET'
ACCESS_TOKEN = 'YOUR TWITTER ACCESS TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR TWITTER ACCESS TOKEN SECRET'

twitter_client = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
twitter_client.update_status(status='Hello World!')
