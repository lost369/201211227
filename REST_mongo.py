
# coding: utf-8

# ## REST

# In[1]:

get_ipython().system(u'curl http://httpbin.org/ip')


# In[2]:

get_ipython().system(u'curl http://httpbin.org/get')


# In[3]:

get_ipython().system(u'curl http://httpbin.org/get?show_env=1')


# In[5]:

import requests
r = requests.post("http://httpbin.org/post")


# In[7]:

k=r.json()


# In[21]:

k['headers']


# In[9]:

for item in k:
    print item


# In[17]:

get_ipython().system(u'curl http://httpbin.org/encoding/utf8')


# In[24]:

import locale


# In[25]:

locale.getdefaultlocale()


#  xml

# In[26]:

input = '''<students>
<student x="1">
    <id>001</id>
    <name>Kim</name>
</student>
<student x="2">
    <id>002</id>
    <name>Lee</name>
</student>
</students>
'''
print input
import xml.etree.ElementTree as ET
nodes=ET.fromstring(input)
for node in nodes.getiterator():
    print node.tag, node.attrib


# In[30]:

print nodes[0].attrib
print nodes[1].attrib
nodes.tag


#  json

# In[31]:

import json
input = '''[
    { "id" : "001", "x" : "2", "name" : "Chuck"},
    { "id" : "009","x" : "7","name" : "Brent" }
]'''


# In[32]:

info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print item['id'], item['name']


# ip주소에서 지역정보 알아내기

# In[35]:

import requests
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr


# In[36]:

import json
geojson=json.loads(geostr)


# In[37]:

type(geojson)


# In[38]:

print geojson['country_code']


# In[39]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[40]:

import os

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=getKey(keyPath)


# 서울시 노선별 지하철역 목록 구하기

# In[69]:

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'


# In[71]:

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX
url+='/'
url+=LINE_NUM


# In[72]:

import requests
data=requests.get(url).text
print data


# In[73]:

import re
p=re.compile('<STATION_NM>(.+?)</STATION_NM>')
res=p.findall(data)
for item in res:
    print item


# In[75]:

import lxml
import lxml.etree
import StringIO
tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATION_NM')
for node in nodes:
    print node.text


# 서울시 외국인 주민 자녀 국적취득 년도별 시군구 합계 구하기

# In[77]:

KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='ListLocaldata470401S'
START_INDEX=str(1)
END_INDEX=str(5)


# In[78]:

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=START_INDEX
url+='/'
url+=END_INDEX


# In[79]:

import requests

data=requests.get(url).text
print data


# In[80]:

tree=lxml.etree.fromstring(data.encode('utf-8'))

nodes=tree.xpath('//STATMAN')
for node in nodes:
    print node.text


# In[91]:

import os
import requests
KEY=str(key['dataseoul'])
TYPE='xml'
SERVICE='CardSubwayStatisticsService'
START_INDEX=1
END_INDEX=5
USE_MON='201306'


# In[92]:

url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=str(START_INDEX)
url+='/'
url+=str(END_INDEX)
url+='/'
url+=USE_MON


# In[93]:

response = requests.get(url).text
print response


# 2013년 1년 동안 지하철역 승하차 인원

# In[104]:

import pymongo
from pymongo import MongoClient
client=MongoClient('localhost:27017')


# In[117]:

db=client.Employees
db.mytable.insert({
    "name":"js"
    })


# In[118]:

empCol=db.mytable.find()
for emp in empCol:
    print emp


# In[111]:

db.mytable.remove()


# In[168]:

import json
_maxIter=2
_iter=0
while _iter<_maxIter:
    #print _api
    response = requests.get(url).text
    jd = json.loads(response)
    for item in jd['CardSubwayStatisticsService']['row']:
        db.mytable.insert(item)
    START_INDEX+=5
    END_INDEX+=5
    _iter+=1
    url='http://openapi.seoul.go.kr:8088/'
    url+=KEY
    url+='/'
    url+=TYPE
    url+='/'
    url+=SERVICE
    url+='/'
    url+=str(START_INDEX)
    url+='/'
    url+=str(END_INDEX)
    url+='/'
    url+=USE_MON


# In[132]:

KEY=str(key['dataseoul'])
TYPE='json'
SERVICE='CardSubwayStatisticsService'
START_INDEX=1
END_INDEX=5
USE_MON='201306'
url='http://openapi.seoul.go.kr:8088/'
url+=KEY
url+='/'
url+=TYPE
url+='/'
url+=SERVICE
url+='/'
url+=str(START_INDEX)
url+='/'
url+=str(END_INDEX)
url+='/'
url+=USE_MON


# In[133]:

response = requests.get(url).text
print response


# In[141]:

import json
jd = json.loads(response)
#print jd['STATION_NM']
#for key,value in jd.items():
#    print "---",key,value

print jd['CardSubwayStatisticsService']['row'][0]
#n=len(jd['SearchSTNBySubwayLineService']['row'])
#for i in range(0,n):
#    print jd['SearchSTNBySubwayLineService']['row'][i]
for item in jd['CardSubwayStatisticsService']['row']:
    print item.keys()
    for i in item.keys():
        if i=='SUB_STA_NM':
            print ''.join(item.values())
            print item.values()[1]

