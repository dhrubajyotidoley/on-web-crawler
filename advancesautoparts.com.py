'''
Date: January 7 2017
Author: Dhrubajyoti Doley
Version: 0.1.1
Email: dhruba@opennirvana.com

Part 1: city pin code and extract data (shop name, physical address, pin code number)
Part 2: Shop by category only sub category (product name, link to product page,
      number of reviews, stars and part number, in/out stock, and ship to home.
'''

import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib2
from BeautifulSoup import BeautifulSoup
import json


search_page = 'https://shop.advanceautoparts.com/webapp/wcs/stores/servlet/StoreLocatorView?langId=-1&catalogId=10051&storeId=10151'

city_list = 'city_list.xlsx'

def Search_Page(pin):
   driver = webdriver.Firefox()
   driver.get(search_page)

   user = driver.find_element_by_id("stlocatorAddress")
   user.send_keys(pin)

   submit = driver.find_element_by_class_name("findStore")
   submit.send_keys("\n")
   submit.send_keys(Keys.RETURN)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def main():
   wb = xlrd.open_workbook(city_list)
   sh = wb.sheet_by_index(0)
   r=1
   while r < len(sh.col(0)):
      pin = int(sh.col_values(1)[r])
      Search_Page(pin)
      r+=1



#url = 'https://shop.advanceautoparts.com/webapp/wcs/stores/servlet/StoreLocatorView?storeId=10151&catalogId=10051&langId=-1&filter=&json=true&rnum=10&max=10&min=1&latitude=37.09024&longitude=-95.71289100000001&resolvedZipcode=67301&stPrefStore=&setStoreCookie=true&address=22011020&radius=50'
url = 'https://shop.advanceautoparts.com/webapp/wcs/stores/servlet/StoreLocatorView?storeId=10151&catalogId=10051&langId=-1&filter=&json=true&rnum=10&max=10&min=1&latitude=36.7266574&longitude=-83.4552486&resolvedZipcode=40863&stPrefStore=&setStoreCookie=true&address=22012005&radius=50'
page = urllib2.urlopen(url)
html_doc = page.read()

data = find_between( html_doc, "var response = [", "];" )

#json_data = json.loads(data)

#print data
with open('test.json', 'w') as e:
   e.write(data)


#print len(json_data)
#print json_data['Name']

#print json_data['Address1']

'''
if __name__=='__main__':
   main()
'''
