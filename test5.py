from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html)
#find a the giftList's children 
#for child in bsObj.find("table",{"id":"giftList"}).children:
#	print(child)
#find the tr labels from the netxt siblings
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:		
	print(sibling)
	