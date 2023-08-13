#Aim : Reading the content of URL, print it on console and open in webbrowser

import urllib.request
import webbrowser

fp = urllib.request.urlopen("http://www.python.org")
mybytes=fp.read()
mystr=mybytes.decode("utf8")
fp.close()
print(fp.geturl());
print(mystr)

webbrowser.open(fp.geturl(),new=2)