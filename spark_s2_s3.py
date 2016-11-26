
# coding: utf-8

# # 문제 S-2: Hello Spark

# In[8]:

import findspark
spark_home="C:/spark-1.6.0-bin-hadoop2.6"


# In[9]:

print spark_home


# In[10]:

findspark.init(spark_home)


# In[11]:

import pyspark


# In[12]:

conf=pyspark.SparkConf()


# In[13]:

conf=pyspark.SparkConf().setAppName("myApp")


# In[14]:

sc=pyspark.SparkContext(conf=conf)


# In[15]:

sc


# In[13]:

sc.version


# In[14]:

sc.master


# In[15]:

sc._conf.getAll()


# # 문제 S-3: Hello RDD

# In[23]:

celsius = [39.2, 36.5, 37.3, 37.8]
def c2f(c):
    f=list()
    for i in c:
        _f=(float(9)/5)*i + 32
        f.append(_f)
    return f


# In[24]:

print c2f(celsius)


# In[27]:

map(lambda c:(float(9)/5)*c + 32, celsius)


# In[28]:

get_ipython().run_cell_magic(u'writefile', u'data/ds_spark_wiki.txt', u"Wikipedia\nApache Spark is an open source cluster computing framework.\n\uc544\ud30c\uce58 \uc2a4\ud30c\ud06c\ub294 \uc624\ud508 \uc18c\uc2a4 \ud074\ub7ec\uc2a4\ud130 \ucef4\ud4e8\ud305 \ud504\ub808\uc784\uc6cc\ud06c\uc774\ub2e4.\nOriginally developed at the University of California, Berkeley's AMPLab,\nthe Spark codebase was later donated to the Apache Software Foundation,\nwhich has maintained it since.\nSpark provides an interface for programming entire clusters with\nimplicit data parallelism and fault-tolerance.")


# In[32]:

textFile=sc.textFile("data/ds_spark_wiki.txt")


# In[33]:

type(textFile)


# In[34]:

textFile.first()


# In[35]:

textFile.take(3)


# In[38]:

words=textFile.map(lambda x:x.split(' '))


# In[39]:

words.collect()


# In[44]:

textFile    .map(lambda x:len(x))    .collect()


# In[51]:

_sparkLine=textFile.filter(lambda line: "Spark" in line)


# In[52]:

_sparkLine.count()


# In[53]:

_sparkLine=textFile.filter(lambda line: u"스파크" in line)


# In[54]:

_sparkLine.count()


# In[55]:

print _sparkLine.first()


# In[56]:

a=[1,2,3]


# In[57]:

type(a)


# In[58]:

myrdd=sc.parallelize(a)


# In[60]:

myrdd.take(3)


# In[61]:

squared=myrdd.map(lambda x:x*x)


# In[62]:

squared.collect()


# In[64]:

a=["this is a line", "this is another line"]
myrdd=sc.parallelize(a)


# In[65]:

words=myrdd.map(lambda x:x.split(' '))


# In[66]:

words.collect()


# In[6]:

get_ipython().run_cell_magic(u'writefile', u'./data/ds_spark_2cols.csv', u'35, 2\n40, 27\n12, 38\n15, 31\n21, 1\n14, 19\n46, 1\n10, 34\n28, 3\n48, 1\n16, 2\n30, 3\n32, 2\n48, 1\n31, 2\n22, 1\n12, 3\n39, 29\n19, 37\n25, 2')


# In[16]:

inp_file = sc.textFile("./data/ds_spark_2cols.csv")
numbers_rdd = inp_file.map(lambda line: line.split(','))


# In[17]:

numbers_rdd.take(10)

