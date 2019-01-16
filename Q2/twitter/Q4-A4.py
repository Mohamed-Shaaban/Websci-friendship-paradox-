from twitter import *

config = {}
execfile("config.py", config)

twitter = Twitter(
		auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

username = "farra007"
query = twitter.friends.ids(screen_name = username, count = 1000)

print "found %d friends" % (len(query["ids"]))
for n in range(0, len(query["ids"]), 100):
	ids = query["ids"][n:n+100]
	subquery = twitter.users.lookup(user_id = ids)

	for user in subquery:
		username = user["screen_name"]
		query = twitter.friends.ids(screen_name = username)
		print (user["screen_name"]) + " number of following = "