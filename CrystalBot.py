import tweepy
import time

auth = tweepy.OAuthHandler('5oFXrjGOac1JrVFDhvWGsC2rJ','ChlfIgYafE1V5pJ79fRsAzJqQQbqn6l0FoqHaKGTCa1W5ti8JS')

auth.set_access_token('1318645824751083521-5fJGTOUwhKe8yVrmr4Uw5z8a4RVxqy',
'UD9U3faPKZ0uUCrkM3Lx4ixayfmQXWgjoXzUShkaQI82j')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# print(user)

clc_tag = '#CLC'
# ssi_el_ssi_tag = '#씨엘씨'
# clc_username = '@CUBECLC'

nrTweets = 1000


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

