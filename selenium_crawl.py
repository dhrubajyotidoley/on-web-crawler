import re
import urllib2
from bs4 import BeautifulSoup
import MySQLdb
import xlsxwriter
from selenium import webdriver
'''
product = 'non-ferrous-metals'
url = 'http://dir.indiamart.com/impcat/' + product + '.html'

'''
driver = webdriver.Firefox()
driver.get("http://dir.indiamart.com/impcat/non-ferrous-metals.html")
driver.implicitly_wait(5)
j=2
i='//div[contains(@id,"fetch'+str(j)+'")]'
'''while True:
    try:
        x = driver.find_element_by_xpath(i)
        break
    except:
        driver.execute_script("window.scrollTo(0, 9999);")'''
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
while True:
	i='//div[contains(@id,"fetch'+str(j)+'")]'
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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
	driver.execute_script("window.scrollTo(document.body.scrollHeight, 0);")

html = driver.page_source
#driver.quit()
print("Done")
workbook = xlsxwriter.Workbook('India-Mart1.xlsx')
worksheet = workbook.add_worksheet()

'''
try:
    response = request(url)

except:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    
soup = BeautifulSoup(response)
'''
soup = BeautifulSoup(html)

row = 0
col = 0

worksheet.write(row,col,'Company Name')
worksheet.write(row,col+1,'Address')
worksheet.write(row,col+2,'Telephone')
worksheet.write(row,col+3,'Link')

row = 2
k=1
for i in soup.find_all('div', {'class' : 'listing-address-container'}):
    a = i.find('span',{'itemprop' : 'name'}).get_text()
    #print a
    worksheet.write(row,0, a)
    b = i.find('span',{'itemprop' : 'streetAddress'}).get_text()
    #print b
    worksheet.write(row,1, b)
    c = i.find('span' , {'itemprop' : 'telephone'}).get_text()
    #print c
    worksheet.write(row,2, c)
    d = i.find('span' , {'itemprop' : 'url'}).get_text()
    #print d
    worksheet.write(row,3, d)
    row+=1
    print k
    k+=1
workbook.close()
