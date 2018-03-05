from sentiment.tass import InterTASSReader
from tass import GeneralTASSReader
from collections import defaultdict


def getStatistics(reader, corpus):
    y = list(reader.y())  # iterador sobre las polaridades de los tweets

    polarity_tweets = defaultdict(int)

    for polarity in y:
        polarity_tweets[polarity] += 1

    print(corpus)
    print("Cantidad total de tweets: " + str(len(y)))
    print("Cantidad de tweets por cada valor de polaridad:")

    for polarity in polarity_tweets.keys():
    	print(polarity + ": " + str(polarity_tweets[polarity]))


getStatistics(InterTASSReader('TASS/InterTASS/tw_faces4tassTrain1000rc.xml'), "InterTASS")
getStatistics(GeneralTASSReader('TASS/GeneralTASS/general-tweets-train-tagged.xml'), "GeneralTASS")
