'''
Date: January 7 2017
Author: Dhrubajyoti Doley
Version: 0.1.1
Email: dhruba@opennirvana.com

Part 1: search term plus the pincode
Part 2: name of business, number of reviews, stars, full address
Part 3: deals, request a quote, request an appointment, book online

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import urllib2
from BeautifulSoup import BeautifulSoup

url = 'https://www.yelp.com/'

#id = find_desc
#id = dropperText_Mast
#id = header-search-submit

def Search_Page(terms, pin):
   driver = webdriver.Firefox()
   driver.get(url)

   term_key = driver.find_element_by_id("find_desc")
   term_key.send_keys(terms)
   
   pin_key = driver.find_element_by_id("dropperText_Mast")
   pin_key.clear()
   pin_key.send_keys(pin)

   submit = driver.find_element_by_id("header-search-submit")
   submit.send_keys("\n")
   submit.send_keys(Keys.RETURN)
   print dir(driver)
   print driver.get_location()
   
   #driver.quit()

csv_file = 'us_postal_codes.csv'

terms = 'Body Shops'

#Search_Page(terms, pin)
with open(csv_file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        pin = row[0]
        print pin
        Search_Page(terms, pin)


#Writing the files into a csv file

'''
url = 'https://www.yelp.com/search?find_desc=Body+Shops&find_loc=00210&ns=1'

page = urllib2.urlopen(url)
html_doc = page.read()
soup = BeautifulSoup(html_doc)
#content = soup.findAll('li', attrs={'class':'regular-search-result'})
shop_name = soup.findAll('h3', attrs={'class':'search-result-title'})

address = soup.findAll('address')

for i in range(len(shop_name)):
   print shop_name[i].text
   #print address[i]
for i in range(len(address)):
   print address[i].text


ofile  = open('data.csv', "wb")
writer = csv.writer(ofile, delimiter='	', quotechar='"', quoting=csv.QUOTE_ALL)
k = 0
for row in range(len(shop_name)):
    writer.writerow(shop_name[k].text)
    k+=1
    
ofile.close()

'''

