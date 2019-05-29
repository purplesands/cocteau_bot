import time
from linereader import copen
from random import randint

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
		time.sleep(1)