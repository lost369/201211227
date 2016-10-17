
# coding: utf-8

# In[2]:

import urllib


# In[3]:

response = urllib.urlopen('http://python.org/')


# In[4]:

response


# In[8]:

_html=response.read()


# In[5]:

import re


# In[6]:

p=re.compile('href="(http://.*?)"')


# In[9]:

res=p.findall(_html)


# In[10]:

for item in res:
    print item


# In[15]:

p=re.compile('<p>(.*?)</p>')


# In[16]:

res=p.findall(_html)


# In[17]:

for item in res:
    print item


# In[18]:

from lxml import etree


# In[20]:

_htmlTree = etree.HTML(_html)


# In[21]:

_htmlTree


# In[22]:

nodes = _htmlTree.xpath('//a[@href]')


# In[24]:

nodes


# In[25]:

for node in nodes:
    print node.attrib


# In[30]:

from lxml.cssselect import CSSSelector


# In[31]:

sel=CSSSelector('a[href]')


# In[33]:

import lxml.html


# In[34]:

html= lxml.html.fromstring(_html)


# In[35]:

results=sel(html)


# In[36]:

print len(results)


# In[44]:

for item in results:
    print item.get('href'), item.text


# In[58]:

sel=CSSSelector('body p')


# In[59]:

results=sel(html)


# In[60]:

print len(results)


# In[64]:

for item in results:
    print item.text
    

