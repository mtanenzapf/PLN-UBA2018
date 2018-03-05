from sentiment.tass import InterTASSReader
from collections import defaultdict

reader = InterTASSReader('TASS/InterTASS/tw_faces4tassTrain1000rc.xml')
tweets = list(reader.tweets())  # iterador sobre los tweets
x = list(reader.X())  # iterador sobre los contenidos de los tweets
y = list(reader.y())  # iterador sobre las polaridades de los tweets

print(len(tweets))

polarity_tweets = defaultdict(int)
	
for polarity in y:
	polarity_tweets[polarity] += 1

print(polarity_tweets)