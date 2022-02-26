import requests
url = "http://192.168.0.120/spicyx/"
r = requests.get(url)
print(r.text)
print("Status code:")
print("\t *",r.status_code)
h = requests.head(url)
print("Header:")
for every_line in h.headers:
    print("\t",every_line,":",h.headers[every_line])
print("Header:")
headers = {
    "User-Agent": "Mobile"
}
url2 = "http://httpbin.org/headers"
rh = requests.get(url2, headers=headers)
print(rh.text)