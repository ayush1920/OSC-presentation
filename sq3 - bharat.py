import requests as rq

s ="""Host: www.bharatacharyaeducation.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: advanced-frontend=gn5ll57kpsdcjv2bd0rf69ogo4; _csrf-frontend=c5ff72bca67c495b68157aa4b937d16912a03a59e66038d3cad42a40deab460da%3A2%3A%7Bi%3A0%3Bs%3A14%3A%22_csrf-frontend%22%3Bi%3A1%3Bs%3A32%3A%22bmtE04EaOxES3NCuI2-4BshTAUYCAMij%22%3B%7D; _ga=GA1.2.186647056.1592331138; _gid=GA1.2.1763113695.1592331138; GED_PLAYLIST_ACTIVITY=W3sidSI6IjRlN28iLCJ0c2wiOjE1OTIzMzEzMDcsIm52IjoxLCJ1cHQiOjE1OTIzMzEyMzYsImx0IjoxNTkyMzMxMzA2fSx7InUiOiJ4aENOIiwidHNsIjoxNTkyMzMxMzA3LCJudiI6MCwidXB0IjoxNTkyMzMxMjQ5LCJsdCI6MTU5MjMzMTI2NH0seyJ1IjoiZXprVCIsInRzbCI6MTU5MjMzMTIzNiwibnYiOjEsInVwdCI6MTU5MjMzMTIzMCwibHQiOjE1OTIzMzEyMzV9XQ..
Upgrade-Insecure-Requests: 1"""


dic  ={}
for i in s.split('\n'):
    k = i.split(':')
    dic[k[0]] = ':'.join(k[1:])[1:]
# print(dic)

r = rq.post('https://www.bharatacharyaeducation.com/index.php/channel/view?id=4' , headers = dic)
# print(r.text)
htm = r.text
import re


l = re.findall('href=\"/index.php/video/view\?id=(.*?)\"', htm)
for i in l:
    print(i)
