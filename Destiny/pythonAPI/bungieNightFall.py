from variables import *
###########################################################################
response = urllib2.urlopen('https://www.bungie.net/en/Activities/Detail?activity=nightfall')
html = response.read()


###########################################################################
# Get the Nightfall of the week


currNite="This week's Nightfall is: "
for i in nite:
    if i in html:
        currNite=currNite+i+". "


###########################################################################
# Get the modifiers for this week 

current="And the modifiers are: "
for i in mods:
    if i in html:
        current=current+i+", "

current=currNite+current[:-2]+". "+glgs
print current

