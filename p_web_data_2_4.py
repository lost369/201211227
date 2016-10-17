
# coding: utf-8

# ## 두번째 수업시간 복습

# In[2]:

import urllib2


# In[3]:

url='http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data'


# In[4]:

res=urllib2.urlopen(url)


# In[5]:

res


# In[6]:

html=res.read()


# In[7]:

html


# In[8]:

import urllib


# In[9]:

response = urllib.urlopen('http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data')


# In[10]:

_html= response.read()


# In[11]:

_html


# In[12]:

lines=_html.splitlines()


# In[14]:

lines


# In[18]:

data=[]


# In[19]:

for line in lines:
    data.append(line.split())


# In[20]:

for line in data:
    print line


# In[22]:

sum=0
cnt=0
for i in range(0,20):
    val=data[i][3]
    if val is '?':
        print i,"None"
    else:
        sum+=float(val)
        cnt+=1
        print i,val,sum
average=float(sum/cnt)
print cnt, sum, average


# ## 한국 포털사이트에서 노래제목을 검색

# In[24]:

import urllib


# In[26]:

keyword='비오는'


# In[27]:

f = urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")


# In[28]:

mydata= f.read()


# In[31]:

pos = mydata.find("트랙 리스트")
if (pos>0):
    pos = mydata.find("_title title NPI=", pos);
    pos = mydata.find("title=",pos+20)
    pos2 = mydata.find("\"", pos+8)
    print "---",mydata[pos+7:pos2]
print len(mydata)


# In[46]:

pos = mydata.find("트랙 리스트")


# In[49]:

pos = mydata.find("_title title NPI=", pos);


# In[50]:

pos = mydata.find("title=",pos+20)


# In[52]:

import re
p=re.compile('title=".*비.?오는.*"')
#res=p.search(data)
res=p.findall(mydata)
for item in res:
    print item


# In[53]:

import lxml.html
from lxml.cssselect import CSSSelector


# In[54]:

html = lxml.html.fromstring(mydata)


# In[60]:

sel = CSSSelector('#content > div:nth-child(4) > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack > table > tbody > tr:nth-child(2) > td.name > a._title.title')


# In[61]:

results = sel(html)


# In[64]:

for item in results:
    #print lxml.html.tostring(item)
    print item.text_content()


# In[65]:

sel = CSSSelector('#content > div:nth-child(4) > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack > table > tbody > tr > td.name > a._title.title')


# In[66]:

results = sel(html)


# In[67]:

for item in results:
    #print lxml.html.tostring(item)
    print item.text_content()


# In[76]:

from lxml.cssselect import CSSSelector

sel = CSSSelector('table[summary] > tbody > ._tracklist_move')
results = sel(html)


# In[77]:

_selName = CSSSelector('.name > a.title')
_selArtist = CSSSelector('._artist.artist')
_selAlbum= CSSSelector('.album > a')
_name=_selName(results[1])
_artist=_selArtist(results[1])
_album=_selAlbum(results[1])


# In[79]:

print _name[0].text_content()
print _artist[0].text_content().strip()
print _album[0].text_content()

