import urllib2
from bs4 import BeautifulSoup

fish_url = 'http://www.opennirvana.com'

links = []

def get_link(url):
   page = urllib2.urlopen(url)
   html_doc = page.read()
   soup = BeautifulSoup(html_doc)
   urllinks = []
   for link in soup.find_all('a'):
      links = link.get('href')
      links = str(links)
      if links.startswith('/') or fish_url in links:
         urllinks.append(links)
   return urllinks

links = get_link(fish_url)
newlinks = []

for i in links:
   if fish_url not in i:
      i = fish_url + i
   newlinks.append(i)

newlinks = list(set(newlinks))
del links[:]

for j in newlinks:
   links = get_link(j)
   for k in links:
      if fish_url not in k:
         k = fish_url + k
      if k not in newlinks:
         newlinks.append(k)

for l in newlinks:
	print l
