import urllib.request 
import re   
from bs4 import BeautifulSoup  

response = urllib.request.urlopen('http://h.bilibili.com/xxxxx')
d = response.read()
soup = BeautifulSoup(d,"html.parser")
print(soup)
actList = []
for lind in soup.find_all('div', class_='info'):
    actid = lind.find('span', class_='floor').get_text()
    print(actid)
    if actid:
        actList.append(str(actid))
