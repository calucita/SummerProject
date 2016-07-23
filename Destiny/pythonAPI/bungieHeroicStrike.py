from variables import *
###########################################################################
response = urllib2.urlopen('https://www.bungie.net/en/Activities/Detail?activity=heroicstrike')
html = response.read()


###########################################################################
# Get the modifiers for this week 

current="The modifiers for this week's playlist are: "
for i in mods:
    if i in html:
        current=current+i+", "

current=current[:-2]+". "+glgs
print current

