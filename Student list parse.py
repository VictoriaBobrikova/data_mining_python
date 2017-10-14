            #Программа извлекает ссылки из ответа посковика ВК.
            #Программа должна пробегать первые 50 страниц поиска, т.к. ВК выдает только 1000 первых пользователей.
            #Пока нам удалось распарсить первую страницу. Однако, выводятся левые ссылки, а также дублируются нужные.
            #Также пока не удалось справиться с ошибкой
            #
            #

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
print(header)

i=0
#while i<=49
url = "https://vk.com/search?c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Buniversity%5D=56&offset="+str(i*20)
r=requests.get(url, headers=header)
print(r.ok)
#print('1)', r.text)
page = BeautifulSoup(r.text, 'html.parser')
user_list=page.findAll('a')
#if a.has_key('href'):
for link in page('a'):
    print(link['href'])
print(user_list)
#for element in user_list:
#        urls.append(element.string)
#for key,val in user_list.items():
#    for link in user_list('div'):
#        print(link['href'])


#