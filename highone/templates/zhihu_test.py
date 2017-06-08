# coding = utf-8
import os
import sys
import requests
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://www.zhihu.com/question/21358581'
req = requests.session()
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0",}
r = req.get(url,headers=headers)
# print r.content
soup = BeautifulSoup(r.text, 'html5lib')
print soup.find(class_='List')