
# coding: utf-8

# In[1]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[2]:

import os

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=getKey(keyPath)


# In[3]:

import twitter


# In[4]:

auth = twitter.oauth.OAuth(key['ACCESSTOKEN'],key['ACCESSTOKENSECRET'],
                            key['CONSUMERKEY'], key['CONSUMERSECRET'])
_client = twitter.Twitter(auth=auth)
print _client


# In[5]:

_client.statuses.update(status="Hello Twitter 1 160930")


# In[9]:

_client.statuses.home_timeline()


# In[31]:

timeline = _client.statuses.home_timeline()


# In[7]:

print type(timeline)
print len(timeline)


# In[41]:

print type(timeline[0])
for key in timeline[0].keys():
    print key,timeline[0][key]


# In[42]:

import oauth2


# In[44]:

q = '#박근혜'
count = 100
# See https://dev.twitter.com/docs/api/1.1/get/search/tweets 
search_results = _client.search.tweets(q=q, count=count)
statuses = search_results['statuses']


# In[53]:

for i,tweet in enumerate(statuses):
    #print tweet[u'user'][u'name']
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])
    _col2.insert_one(tweet)


# In[54]:

for i in _col2.find():
    print i


# In[24]:

type(statuses)


# In[19]:

import io
with io.open('src/ds_twitter_i.json','w',encoding='utf8') as json_file:
    data=json.dumps(content,json_file,ensure_ascii=False, encoding='utf8')
    


# In[27]:

import oauth2 as oauth
import json

consumer = oauth.Consumer(key=key['CONSUMERKEY'], secret=key['CONSUMERSECRET'])
token=oauth.Token(key=key['ACCESSTOKEN'], secret=key['ACCESSTOKENSECRET'])


# In[28]:

consumer


# In[30]:

client = oauth.Client(consumer, token)


# In[5]:

help(client.request)


# ## T-2 자신의 타임라인 가져오기

# In[34]:

from pymongo import MongoClient


# In[35]:

_mclient=MongoClient()


# In[24]:

_mclient['ds_twitter']


# In[37]:

_db=_mclient.ds_twitter


# In[50]:

_col=_db.home_timeline


# In[46]:

_col2=_db.president


# In[10]:

home_timeline = _client.statuses.home_timeline()


# In[20]:

print home_timeline[0].keys()


# In[32]:

len(home_timeline)


# In[31]:

home_timeline[0]['text']


# In[35]:

print home_timeline


# In[51]:

for i in home_timeline:
    print i['id'], i['text']
    _col.insert(i)


# In[45]:

for i in _col.find():
    print i

