import time
import tweepy 

consumer_key = "SaSW8NrEZRUsGfZlcOEwwJOoX"
consumer_secret = "C4K6cXR2fTVWhTDas4oJaQU4e3eUdfdrjM8qmaZmAEh1Dym2AC"
access_key = "4879994613-6ZGf0doVWQIMCTXgXLQZ72lVpwlOAhuSIwYc6UH"
access_secret = "BnmtgH0gVrMp5lni6c4sZKacW8Zqs6uCKIcBVwDVHVvQp"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)

api = tweepy.API(auth)

user = api.get_user('Shaaban_Migo')

print "Number of Followers I have is = " + "{0}".format(user.followers_count)

ids = []
i = 0
for user in tweepy.Cursor(api.followers, screen_name="farra007",count = 50).items():
		try:
			name = api.get_user(user.screen_name)	
			print "Number of Followers "+ user.screen_name + " have is = " + "{0}".format(name.followers_count)
			i=+1
		except tweepy.TweepError, e:
			if e == "[{u'message': u'Rate limit exceeded', u'code': 88}]":
				time.sleep(60*15) #Sleep for 5 minutes
			else:
				time.sleep(60*15)
			print "Number of Followers "+ user.screen_name + " have is = " + "{0}".format(name.followers_count)
#print e
print i
print "Number of Followers" + "{0}".format(i)