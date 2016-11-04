from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://baidu.lecai.com/lottery/draw/list/50?type=latest&num=100")
bsObj=BeautifulSoup(html)
nameList = bsObj.findAll("td", {"class":"redBalls"})
#nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
	print(name.get_text())
	
