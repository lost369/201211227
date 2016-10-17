
# coding: utf-8

# ## REST

# In[27]:

import os
KEY="576e676c626c6f7335386e525a6e67"
TYPE='xml'
SERVICE='SearchSTNBySubwayLineService'
START_INDEX='1'
END_INDEX='10'
LINE_NUM='2'
#params=os.path.join(KEY,TYPE,SERVICE,START_INDEX,END_INDEX,LINE_NUM)


# In[32]:

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


# In[33]:

print url


# In[8]:

print(params)


# In[4]:

"/json/SearchSTNBySubwayLineService/1/5/1/"


# In[29]:

import urlparse
_url='http://openapi.seoul.go.kr:8088/'
url=urlparse.urljoin(_url,params)
print url


# In[16]:

myurl='http://openapi.seoul.go.kr:8088/576e676c626c6f7335386e525a6e67/xml/SearchSTNBySubwayLineService/1/5/1/'


# In[34]:

import requests
data=requests.get(url)


# In[35]:

print data.text


# In[47]:

import lxml.html
from lxml import etree


# In[46]:

print type(data.text)


# In[51]:

r=requests.get("http://httpbin.org/get")


# In[52]:

r.status_code


# In[55]:

r=requests.get('http://httpbin.org/status/404')


# In[56]:

r.headers


# In[58]:

get_ipython().system(u'curl http://httpbin.org/get')


# ## 한글

# In[61]:

r=requests.get('http://httpbin.org/encoding/utf8')


# In[65]:

r.text[:500]


# In[66]:

print '\u203e'


# In[67]:

import locale


# In[68]:

locale.getdefaultlocale()

