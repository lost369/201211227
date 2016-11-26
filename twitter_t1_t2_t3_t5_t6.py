
# coding: utf-8

# # T-1: Twitter에 'Hello World'를 쓴다.

# In[2]:

def getKey(keyPath):
    d=dict()
    f=open(keyPath,'r')
    for line in f.readlines():
        row=line.split('=')
        row0=row[0]
        d[row0]=row[1].strip()
    return d


# In[3]:

import os

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=getKey(keyPath)


# In[4]:

import twitter


# In[5]:

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


# In[5]:

q = 'seoul'
count = 10
# See https://dev.twitter.com/docs/api/1.1/get/search/tweets 
search_results = _client.search.tweets(q=q, count=count)
statuses = search_results['statuses']


# In[6]:

for i,tweet in enumerate(statuses):
    #print tweet[u'user'][u'name']
    print "[%d]\t%d\t%s:%s" % (i,tweet['id'],tweet['user']['name'],tweet['text'])
    #_col2.insert_one(tweet) 
    # i를 0부터 10까지 나오게 하는게 enumerate


# In[54]:

for i in _col2.find():
    print i


# In[24]:

type(statuses)


# In[19]:

import io
with io.open('src/ds_twitter_i.json','w',encoding='utf8') as json_file:
    data=json.dumps(content,json_file,ensure_ascii=False, encoding='utf8')
    


# In[30]:

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


# In[33]:

home_timeline = _client.statuses.home_timeline()


# In[20]:

print home_timeline[0].keys()


# In[32]:

len(home_timeline)


# In[31]:

home_timeline[0]['text']


# In[35]:

print home_timeline


# In[34]:

for i in home_timeline:
    print i['id'], i['text']
    #_col.insert(i)


# In[45]:

for i in _col.find():
    print i


# # T-3: Twitter에 'Seoul'을 2015년 12월 한 달 분량을 읽는다.

# In[44]:

q = '박근혜'
count = 200
since_id='784295227351871489'
# See https://dev.twitter.com/docs/api/1.1/get/search/tweets 
search_results = _client.search.tweets(q=q, count=count,since_id=since_id)
statuses = search_results['statuses']


# In[45]:

print len(statuses)


# In[40]:

search_results


# In[46]:

for i,tweet in enumerate(statuses):
    #print tweet[u'user'][u'name']
    print tweet['id']
    #_col2.insert_one(tweet) 
    # i를 0부터 10까지 나오게 하는게 enumerate


# In[47]:

f=open('_todel.txt','w')
for i,tweet in enumerate(statuses):
    print i,tweet['id'],tweet['text']
    j=json.dumps([i,tweet['id'],tweet['text']])
    f.write(j)
f.close()


# In[48]:

statuses[-1]['id']#v파이썬에서 -1은 맨마지막을 지칭하는 것 statuses[-1]['id']-1은 다음 max_id 지칭


# In[49]:

prev_id=None


# In[52]:

prev_id=None
f=open('_todel3.txt','a')
for i in range(0,20):
    q = '박근혜'
    count = 10
    search_results = _client.search.tweets(q=q, count=count,max_id=prev_id)
    statuses = search_results['statuses']
    print len(statuses)
    for i,tweet in enumerate(statuses):
        #print str(i),tweet['id'],tweet['user']['name'],tweet['text']
        f.write(json.dumps([str(i),tweet['id'],tweet['user']['name']]))
        f.write("\n")
    #if data["statuses"] == []:
    #    print "end of data"
    #    break
    #else:
    prev_id=int(statuses[-1]['id'])-1
    print prev_id
f.close()


# # T-5 follower를 가져온다

# In[7]:

followers=_client.followers.list()


# In[8]:

print len(followers)
print type(followers)


# In[34]:

followers


# In[35]:

for k,v in followers.iteritems():
    print k


# In[10]:

for i in followers['users']:
    print i['id'],i['screen_name']


# # T-6: Follower의 timeline을 가져온다.

# In[61]:

user_id='397672819'
count=20
search_results = _client.statuses.user_timeline(user_id=user_id, count = count)


# In[63]:

search_results[0]['id']


# In[25]:

len(search_results)


# In[56]:

print search_results[-1]['text']


# In[33]:

for tweet in search_results:
    print tweet['text']


# In[65]:

prev_id=800581273404076032
for i in range(0,20):
    user_id='397672819'
    count=20
    search_results = _client.statuses.user_timeline(user_id=user_id, count=count,max_id=prev_id)
    for tweet in search_results:
        print tweet['text']
        #f.write(json.dumps([str(i),tweet['id'],tweet['user']['name']]))
        #f.write("\n")
    #if data["statuses"] == []:
    #    print "end of data"
    #    break
    #else:
    prev_id=int(search_results[-1]['id'])-1
    print prev_id


# In[11]:

followers=_client.friends.list()


# In[12]:

for i in followers['users']:
    print i['id'],i['screen_name']

