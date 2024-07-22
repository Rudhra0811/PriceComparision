import requests
import tldextract
from bs4 import BeautifulSoup

# Take Input

url1 = input("Enter URL: ")
url2 = input("Enter URL: ")

# loading
print('Calculating results...')

# Extract information from URL
extracted_info1 = tldextract.extract(url1)
extracted_info2 = tldextract.extract(url2)

# Headers

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

# Session

session = requests.Session()

req1 = session.get(url1, headers=headers)
req2 = session.get(url2, headers=headers)


soup1 = BeautifulSoup(req1.content, "html.parser")
soup2 = BeautifulSoup(req2.content, "html.parser")


print('Title 1:', soup1.title.string)
print('Title 2:', soup2.title.string)

