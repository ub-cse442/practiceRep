import re
import urllib2
import sys



k = '124,12,33'

u = k.replace(',', '')

print type(u)

quit()


#check if python version 3.X or 2.X
if (sys.version_info > (3, 0)):
	def myRequest(web):
		return urllib2.request.urlopen(web)
else:
	def myRequest(web):
		return urllib2.urlopen(web)

k = myRequest('https://en.wikipedia.org/wiki/United_States_presidential_election,_2012')

print k.readline()

quit()

florida = '<td style="text-align:left;"><a href="/wiki/United_States_presidential_election_in_Florida,_2004" title="United States presidential election in Florida, 2004">Florida</a></td>'


re1 = '<td style="text-align:left;"><a href="/wiki/United_States_presidential_election_in_.+?." title="United States presidential election in .+?.">.+?.</a></td>'


print re.findall(re1, florida)
