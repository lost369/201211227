
# coding: utf-8

# In[2]:

import urllib


# In[3]:

response = urllib.urlopen('https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=omDuV9CdJcLc0ATQ_7_QBQ/')


# In[4]:

_html = response.read()


# In[5]:

from lxml import etree


# In[6]:

_htmlTree = etree.HTML(_html)


# In[57]:

nodes = _htmlTree.xpath('//*[@class="lm"]/text()')


# In[56]:

nodes2 = _htmlTree.xpath('//*[@class="rgt"]/text()')


# In[53]:

nodes3 = _htmlTree.xpath('//*[@class="rgt rm"]/text()')


# In[58]:

print len(nodes2)


# In[59]:

for i in range(30):
    k=4*i
    print nodes[i].strip(), nodes2[k].strip(), nodes2[k+1].strip(), nodes2[k+2].strip(), nodes2[k+3].strip(), nodes3[i].strip()

