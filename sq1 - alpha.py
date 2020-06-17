import requests as rq
import urllib
import urllib.request
url = 'https://wall.alphacoders.com/search.php?search=nature'

##s ="""Host: wall.alphacoders.com
##User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0
##Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
##Accept-Language: en-US,en;q=0.5
##Accept-Encoding: gzip, deflate, br
##Connection: keep-alive
##Referer: https://wall.alphacoders.com/by_sub_category.php?id=118376&name=Nature+Wallpapers
##Cookie: wa_session=s44pavsnge70o3tek3q26k3jsksm3konfg28hn899vrgsnp5j4dfuja2cacje5guqgca2uth5ocbh8n4dvkn5n6p9cphc1kboak89u2; __cfduid=d651549650a89255b9cd215c643d928c81592323746; cookieconsent_status=allow
##Upgrade-Insecure-Requests: 1"""

# ------------- split -----------------

##s = s.split('\n')
##for i in s:
##    k = i.split(':')
##    dic[k[0]]  = ':'.join(k[1:])[1:]
##dic ={}



##def download(url):
##    opener = urllib.request.build_opener()
##    opener.addheaders = [("User-Agent" , "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0")]
##    urllib.request.install_opener(opener)
##    name = url.split('/')[-1]
##    print(url, name)
##    urllib.request.urlretrieve(url,name)

r =  rq.get(url)
import codecs

##with codecs.open('dasd.htm','w','utf-8') as f:
##    f.write(r.text)

r = r.text
import re

l = re.findall('big.php\?i=(.*?)\"', r)
l = [f'https://wall.alphacoders.com/big.php?i={i}\"' for i in l]
for i in l:
    r = rq.get(i)
    r = r.text
    # remove non ascii char
    r = re.sub(r'[^\x00-\x7F]+',' ', r)
    m = re.findall('<div class=\"center img-container-desktop\">(.*?)<picture>',r, re.DOTALL)
    ind1  = m[0].find('https')
    ind2 = m[0].find('\"',ind1)
    m = m[0][ind1:ind2]
    print(m)
    download(m)
    break
