import time, tweepy, os
from linereader import copen
from random import randint

app = Flask(__name__)
app.run(host= '0.0.0.0', port=environ.get('PORT'))

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

lyrics = copen('cocteaus.txt')
lines = lyrics.count('|')

while True:
	line = randint(1, lines)
	if line == 0:
		line = randint(1, lines)
	tweet = lyrics.getline(line)
	while len(tweet) < 200:
		line+=1
		if "~" not in lyrics.getline(line):
			tweet = tweet + lyrics.getline(line)
		else:
			break

	if len(tweet) <= 200 and tweet != '\n' :
		tweet = tweet.replace("|", '')
		print(tweet)
		api.update_status(tweet)
		time.sleep(60)
