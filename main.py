import requests
import tldextract
from bs4 import BeautifulSoup
import cv2
import numpy as np

def get_soup(url, headers):
    session = requests.Session()
    req = session.get(url, headers=headers)
    return BeautifulSoup(req.content, "html.parser")

def show_captcha(captcha_url):
    captcha_response = requests.get(captcha_url, stream=True).raw
    image = np.asarray(bytearray(captcha_response.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    cv2.imshow("Captcha", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    captcha_input = input("Please enter captcha: ")
    return captcha_input

# Take Input
url1 = input("Enter URL: ")
url2 = input("Enter URL: ")

# loading
print('Calculating results...')

# Headers
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

soup1 = get_soup(url1, headers)
soup2 = get_soup(url2, headers)

captcha1 = soup1.find("form", {"name": "captchaForm"})
captcha2 = soup2.find("form", {"name": "captchaForm"})

if captcha1 is None:
    print("Lucky! No Captcha on site 1")
    print("Title of the page 1: ", soup1.title.string)
else:
    print("Captcha found on site 1")
    captcha_image_url1 = soup1.find("img", {"id": "captchaTag"}).get("src")
    captcha_input1 = show_captcha(captcha_image_url1)
    # Here you would handle sending the captcha response back to the server

if captcha2 is None:
    print("Lucky! No Captcha on site 2")
    print("Title of the page 2: ", soup2.title.string)
else:
    print("Captcha found on site 2")
    captcha_image_url2 = soup2.find("img", {"id": "captchaTag"}).get("src")
    captcha_input2 = show_captcha(captcha_image_url2)
    # Here you would handle sending the captcha response back to the server
