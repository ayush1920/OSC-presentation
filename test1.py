import requests as rq
import re
import urllib
import urllib.request


def download(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [("User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0")]
    urllib.request.install_opener(opener)
    name = url.split('/')[-1]
    print(url, name)
    urllib.request.urlretrieve(url,name)

r = rq.get('https://wall.alphacoders.com/by_category.php?id=10&name=Earth+Wallpapers')
r = r.text


f = re.findall('big.php\?i=(.*?)\"',r)
f = ['https://wall.alphacoders.com/big.php?i='+i for i in f]

for i in f:
    r = rq.get(i)
    r  =r.text
    r = re.sub(r'[^\x00-\x7F]+',' ', r)
    m = re.findall('<div class=\"center img-container-desktop\">(.*?)<picture>',r, re.DOTALL)
    ind1  = m[0].find('https')
    ind2 = m[0].find('\"',ind1)
    m = m[0][ind1:ind2]
    print(m)
    download(m)
