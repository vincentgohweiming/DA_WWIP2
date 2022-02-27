#use the Request library
import requests
#set the target webpage
url = "http://192.168.0.120/spicyx/"
r = requests.get(url)
#This will get the full page
print(r.text)
#This will get the status code
print("Status code:")
print("\t *",r.status_code)
#this will get headers
h = requests.head(url)
print("Header:")
#print line by line
for every_line in h.headers:
    print("\t",every_line,":",h.headers[every_line])
print("Header:")
#modifying the user agent
headers = {
    "User-Agent": "Mobile"
}
#test it on an external website
url2 = "http://httpbin.org/headers"
rh = requests.get(url2, headers=headers)
print(rh.text)