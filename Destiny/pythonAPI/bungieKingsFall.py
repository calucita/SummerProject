from variables import *
###########################################################################
response = urllib2.urlopen('https://www.bungie.net/en/Activities/Detail?activity=kingsfall')
html = response.read()


###########################################################################
# Get the Challenge of the week


curr="This week's King's Fall Challenge is "
for i in chal:
    if i in html:
        curr=curr+i+":"


###########################################################################

war = " a different player should hold the Aura for each damage phase; no Guardian should hold the Aura more than once during the fight."
gol = " each player must hold the Gaze at least once during each damage phase."
ory = " detonate a total of 16 or more Blight Bombs all at once."

if "War" in curr:
    curr=curr+war+glgs
elif "Golgo" in curr:
    curr=curr+gol+glgs
else:
    curr=curr+ory+glgs

print curr
