import tweepy
import time

auth = tweepy.OAuthHandler('INSERT KEY HERE','INSERT KEY HERE')

auth.set_access_token('INSERT KEY HERE',
'INSERT KEY HERE')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# print(user)

clc_tag = '#CLC'
# ssi_el_ssi_tag = '#씨엘씨'
# clc_username = '@CUBECLC'
tweetNo = 1000
nrTweets = tweetNo

class CrystalBot(object):
    def __init__(self):
        for tweet in tweepy.Cursor(api.search, clc_tag).items(nrTweets):
            try:
                tweet.retweet()
                tweet.favorite()
                print("Tweet Retweeted")
                time.sleep(90)
            except tweepy.TweepError as error:
                print(error.reason)
            except StopIteration:
                break

while nrTweets > 0:
    CrystalBot()
else:
    nrTweets = tweetNo
    CrystalBot()
