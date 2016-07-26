import re
import urllib2


###########################################
### Set main user name
userName="calucita"

### Get User ID 
getId=urllib2.urlopen('https://api.twitch.tv/kraken/channels/'+userName)
outId=getId.read()
searchId=re.search('(?<="_id":)\d+', outId)
userId=searchId.group(0)

### See if channel is online and/or hosting
response = urllib2.urlopen('https://api.twitch.tv/kraken/streams/'+userName)
api = response.read()
#print api
if '"stream":null' in api:
    #print "Stream offline"
    getHost=urllib2.urlopen('http://tmi.twitch.tv/hosts?include_logins=1&host='+userId)
    readHost=getHost.read()
    searchHost=re.search('(?<="target_login":")\w+', readHost)
    #print searchHost.group(0)
    if searchHost is None:
        print "Channel offline and not hosting"
    else:
        print "Channel offline and hosting "+searchHost.group(0)
else:
    print "Stream is live"
    
