import requests as rq
import codecs

def save(data):
    with codecs.open('page.htm','w','utf-8') as f:
        f.write(data)

head  ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}
r  = rq.get('http://vtopcc.vit.ac.in:8080/vtop/', headers = head)
save(r.text)
