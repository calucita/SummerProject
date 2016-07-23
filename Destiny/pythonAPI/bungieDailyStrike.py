from variables import *
###########################################################################
response = urllib2.urlopen('https://www.bungie.net/en/Activities/Detail?activity=dailychapter')
html = response.read()


###########################################################################
# Get the Nightfall of the week


curr="Today's story mission is: "
for i in stor:
    if i in html:
        curr=curr+i+". "
        break


current=curr+glgs
print current

