
import urllib2


###########################################

response = urllib2.urlopen('https://api.twitch.tv/kraken/streams/calucita')
api = response.read()

if '"stream":null' in api:
    print "Stream offline"
