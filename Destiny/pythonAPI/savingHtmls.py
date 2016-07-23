import urllib2

fXur = open('XurHtml', 'w')
fActivities = open('ActivitiesHTML', 'w')
fIB = open ('IBHTML', 'w')


response = urllib2.urlopen('https://www.bungie.net/en/Activities')
html = response.read()
fActivities.write(html)



response = urllib2.urlopen('https://www.bungie.net/en/Activities/Detail?activity=xur')
html = response.read()
fXur.write(html)

response = urllib2.urlopen('https://www.bungie.net/en/Activities/Detail?activity=ironbanner')
html = response.read()
fIB.write(html)

