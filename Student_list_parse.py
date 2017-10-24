from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests



ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
print(header)


url = "https://vk.com/search?c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Buniversity%5D=56&offset=80"
r=requests.get(url, headers=header)
print(r.ok)
page = BeautifulSoup(r.text, 'html.parser')
print(page.prettify())
tags=page.findAll("div", {"class":"labeled name"})