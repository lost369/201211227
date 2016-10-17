
# coding: utf-8

# ## 국제학회 목록을 크롤링하기

# In[1]:

import lxml.html
from lxml.cssselect import CSSSelector
import requests
r = requests.get('https://www.ieee.org/conferences_events/index.html')

html = lxml.html.fromstring(r.text)


# In[27]:

sel=CSSSelector('div.content-c > div:nth-child(1) > div >div>p>a')


# In[28]:

results=sel(html)


# In[29]:

print len(results)


# In[32]:

for item in results:
    print item.get('href')
    print item.text


# In[33]:

sel=CSSSelector('div.content-c > div:nth-child(1) > div >div>p')


# In[34]:

results=sel(html)


# In[37]:

for item in results:
    print item.text_content()


# ## 프로야구 기록

# In[42]:

import urllib2
import requests
urlperson='http://www.kbreport.com/player/list?key=이대호'
urlbase="http://www.kbreport.com/leader/main?"
url1="rows=20&order=oWAR&orderType=DESC&"
url2="teamId=1&defense_no=2&year_from=2015&year_to=2015&split01=&split02_1=&split02_2=&r_tpa_count=&tpa_count=0"
urlbaseball=urlbase+url1+url2
print urlbaseball
data=requests.get(urlbaseball).text
#data=requests.get(urlperson).text
print data[6000:7000]


# In[43]:

print data.find('top-score-top')
print data.find('top-score end')


# In[44]:

mydata=data[6340:8353+len('top-score end')]


# In[46]:

import re
p=re.compile(u'.승.+')


# In[47]:

res=p.findall(mydata)


# In[48]:

for item in res:
    print item

