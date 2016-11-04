from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html=urlopen("http://baidu.lecai.com/lottery/draw/list/50?type=latest&num=1000")
bsObj=BeautifulSoup(html,"html.parser")
redballs=bsObj.findAll("td",{"class":"redBalls"})
for redball in redballs:
	print(cnt)
	print(redball.get_text())
	
	
	
	
 