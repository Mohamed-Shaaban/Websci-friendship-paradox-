from twitter import *
config = {}
#execfile("config.py", config)

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
twitter = Twitter(
auth = OAuth(config["4879994613-6ZGf0doVWQIMCTXgXLQZ72lVpwlOAhuSIwYc6UH"], config["BnmtgH0gVrMp5lni6c4sZKacW8Zqs6uCKIcBVwDVHVvQp"], config["SaSW8NrEZRUsGfZlcOEwwJOoX"], config["C4K6cXR2fTVWhTDas4oJaQU4e3eUdfdrjM8qmaZmAEh1Dym2AC"]))

username = "farra007"
query = twitter.friends.ids(screen_name = username, count = 1000)

print "found %d friends" % (len(query["ids"]))
for n in range(0, len(query["ids"]), 100):
	ids = query["ids"][n:n+100]
	subquery = twitter.users.lookup(user_id = ids)

for user in subquery:
	username = user["screen_name"]
	query = twitter.friends.ids(screen_name = username)
	print (user["screen_name"]) + " number of following = "​