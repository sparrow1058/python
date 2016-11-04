from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
	try:
		html=urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsOjb=BeautifulSoup(html.read())
		title=bsOjb.body.h1
	except AttributeError as e:
		return None
	return title
title=getTitle("http://www.haidiyun.top/index.html")
if title==None:
	print("Title could not be found")
else:
	print(title)