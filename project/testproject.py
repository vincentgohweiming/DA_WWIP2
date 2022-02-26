import requests
from bs4 import BeautifulSoup
import unittest
import scrapping as scrapytestings

class scrapytestings(unittest.TestCase):


 def test_website(self):
        url = "http://192.168.0.120/spicyx/"
        r = requests.get(url)
        if (r.status_code == 200):
            print("website reponse is okay")
        else:
            print("website status is not ok")
        websiteSource = r.content
        print(websiteSource)
 def test_contentExist(self):
     url = "http://192.168.0.120/spicyx/"
     r = requests.get(url)
     html_container = r.content
     page_content = BeautifulSoup(html_container, 'html.parser')
     content = page_content('div',{'id':'mw-content-text'})
     self.assertIsNotNone(content)
     print("tested content")
 def testwebsite(self):
    url = "http://192.168.0.120/spicyx/"
    r = requests.get(url)
    if (r.status_code == 200):
        print("website reponse is okay")
    else:
        print("website status is not ok")
    r.close()
    websiteSource = r.content
    print(websiteSource)


   #teach the script to recognise the item to extract
    html_container = r.content
    page_content = BeautifulSoup(html_container, 'html.parser')

    testsite = page_content.find_all('div', class_="media-body")
    for menu in testsite:
        menu_title= menu.h4.text
        menu_price = menu.span.text
        menu_description = menu.p.text
        print(menu_title)
        print(menu_price)
        print(menu_description)
