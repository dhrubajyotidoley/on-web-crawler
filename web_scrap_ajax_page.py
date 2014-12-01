from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import mechanize
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://dir.indiamart.com/search.mp?ss=copper+tubes&cq=Thane")
j=2
while True:
	i='//div[contains(@id,"scroll'+str(j)+'")]'
	driver.execute_script("window.scrollTo(0, 99999);")
	try:
		x = driver.find_element_by_xpath(i)
		a= x.click();
	except:
		break	
	j=j+1
	try:
		x = driver.find_element_by_xpath('//div[contains(@class,"cls_div")]')
	except:
		pass
	driver.execute_script("window.scrollTo(99999, 0);")
driver.execute_script("window.scrollTo(99999, 0);")
print "loading done..."
produnt_name =driver.find_elements_by_xpath('//a[contains(@class,"product-name")]')
desc =driver.find_elements_by_xpath('//p[contains(@class,"description-clr description-padding")]')
cname =driver.find_elements_by_xpath('//span[contains(@class,"company-name")]')
address =driver.find_elements_by_xpath('//span[contains(@class,"srch-add")]')
link = driver.find_elements_by_xpath('//a[contains(@class,"g9")]')
contact = driver.find_elements_by_xpath('//span[contains(@class,"listing-contact phone-block")]')
i=0
for a in produnt_name:
	print 'produnt_name:'+a.text
	print desc[i].text
	print cname[i].text
	print address[i].text
	print link[i].text
	print contact[i].text
	i=i+1
