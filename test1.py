from urllib.request import urlopen
html=urlopen("http://www.haidiyun.top/index.html")
print(html.read())