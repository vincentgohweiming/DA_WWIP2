import requests
from bs4 import BeautifulSoup
import unittest
import scrapping as scrapytestings
import request as prog

class scrapytestings(unittest.TestCase):


 def test_website(self):
        #set the target url
        url = "http://192.168.0.120/spicyx/"
        r = requests.get(url)
        #test the webstie
        if (r.status_code == 200):
            print("website reponse is okay")
        else:
            print("website status is not ok")
        websiteSource = r.content
        print(websiteSource)
 def test_contentExist(self):
     #set the url
     url = "http://192.168.0.120/spicyx/"
     r = requests.get(url)
     #test whether the page content exist
     #print out the whole content of the page
     html_container = r.content
     page_content = BeautifulSoup(html_container, 'html.parser')
     content = page_content('div',{'id':'mw-content-text'})
     self.assertIsNotNone(content)
     #print the message to see it successful
     print("tested content")
 def testsite(self):
     #set the target url
    url = "http://192.168.0.120/spicyx/"
    r = requests.get(url)
     #if the server is okay it will print the message
    if (r.status_code == 200):
        print("website reponse is okay")
    else:
        print("website status is not ok")
    r.close()
    websiteSource = r.content
    print(websiteSource)


   #teach the script to recognise the item
    html_container = r.content
    page_content = BeautifulSoup(html_container, 'html.parser')
   #test the page for menu and description
    testsite = page_content.find_all('div', class_="media-body")
    for menu in testsite:
        menu_title= menu.h4.text
        menu_price = menu.span.text
        menu_description = menu.p.text
        #print out the menu title,price,description
        print(menu_title)
        print(menu_price)
        print(menu_description)
if __name__ == '__main__':
    unittest.main()
