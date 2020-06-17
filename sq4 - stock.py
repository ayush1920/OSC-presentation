import requests as rq
import json
from bokeh.plotting import  figure,show
from datetime import datetime, timedelta

end_time = str(datetime.today().timestamp()).split('.')[0]
start_time = str((datetime.today() - timedelta(hours=50, minutes=00)).timestamp()).split('.')[0]
print(start_time,end_time)
name  = "TCS.NS"
interval = "1m"
url = "https://query1.finance.yahoo.com/v8/finance/chart/"+name+"?symbol="+name+"&period1="+start_time+"&period2="+end_time+"&interval="+interval+"&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-IN&region=IN&crumb=IDZ1Or1I%2F1b&corsDomain=in.finance.yahoo.com"
print(url)
htm = rq.get(url)
data =json.loads(htm.text)
timestamp = list((data['chart']['result'][0]['timestamp']))

close  = list((data['chart']['result'][0]['indicators']['quote'][0]['close']))
#print(close)
none_cnt = close.count(None)
summ = 0
print(none_cnt)
for i in close:
    if i !=None:
        summ+=i
avg = int(summ/(len(close)-none_cnt))
for i in range(len(close)):
    if close[i]==None:
        close[i]=avg
# manage time split
split = 0
splittime=[timestamp[0]]
splitclose=[close[0]]
for i in range(0,len(timestamp)-1):
    if timestamp[i+1] - timestamp[i]>200:
        split=i+1
        timestamp1=timestamp[0:split]
        timestamp2= timestamp[split::1]
        diff = timestamp2[0] -  timestamp1[split-1] -50
        timestamp2 = [x - diff for x in timestamp2]
        splittime+=[timestamp1[split-1],timestamp2[0]]
        splitclose+= [close[split-1],close[split]]
        timestamp  = timestamp1+timestamp2
splittime.append(timestamp[-1])
splitclose.append(close[-1])
#print(close)
p = figure(plot_width=1500, plot_height=700,title=name +" "+str(datetime.fromtimestamp(int(start_time)))+" "+str(datetime.fromtimestamp(int(end_time))))
p.line(x=timestamp, y=close, color= "navy",line_width=2)
p.line(x=splittime, y=splitclose,color="firebrick",line_width=1)
p.xaxis.visible = False
p.xgrid.visible = False
p.ygrid.visible = False
show(p)
