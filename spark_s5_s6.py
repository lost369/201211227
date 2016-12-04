
# coding: utf-8

# # S.5 Spark SQL

# In[2]:

import findspark
spark_home="C:/spark-1.6.0-bin-hadoop2.6"
findspark.init(spark_home)


# In[3]:

import pyspark
conf=pyspark.SparkConf()
conf = pyspark.SparkConf().setAppName("myAppName")
sc = pyspark.SparkContext(conf=conf)


# In[4]:

from pyspark.sql import SQLContext
sqlCtx = SQLContext(sc)


# In[5]:

pDf=sqlCtx.read.json("C:/spark-1.6.0-bin-hadoop2.6/examples/src/main/resources/people.json")


# In[7]:

pDf.filter(pDf['age'] < 21).show()


# In[8]:

pDf.registerTempTable("yesun")
sqlCtx.sql("select age from yesun").show()


# In[10]:

import requests
r=requests.get("https://raw.githubusercontent.com/jokecamp/FootballData/master/World%20Cups/all-world-cup-players.json")
wc=r.json()


# In[12]:

wcDf=sqlCtx.createDataFrame(wc)
wcDf.printSchema()


# In[19]:

wcDf.registerTempTable("world")
sqlCtx.sql("select FullName, Position, DateOfBirth from world").show()


# In[21]:

import json
import requests
_url="https://health.data.ny.gov/api/views/jxy9-yhdk/rows.json?accessType=DOWNLOAD"
_json=requests.get(_url).json()


# In[24]:

_df=sqlCtx.createDataFrame(_json['data'])


# In[25]:

_df.printSchema()


# In[27]:

_df.registerTempTable("babyNames")
sqlCtx.sql("select _10 , _9 from babyNames").show(5)


# # S.6 DataFrame

# In[5]:

from pyspark.sql import Row
Person = Row('name', 'weight')
rows = [Person('kim', 70), Person('lee', 75), Person('lim', 80),]


# In[6]:

rowsDF=sqlCtx.createDataFrame(rows)


# In[7]:

rowsDF.printSchema()


# In[11]:

rowsDF.where(rowsDF.weight > 75)    .select([rowsDF.name, rowsDF.weight]).show()


# In[12]:

rowsDF.groupby(rowsDF.weight).max().show()


# # S.7 Statistics

# In[16]:

from pyspark.sql.functions import rand, randn
 # Create a DataFrame with one int column and 10 rows.
df = sqlCtx.range(0, 20)
df.show()


# In[17]:

df.select("id", rand(seed=5).alias("uniform"), randn(seed=27).alias("normal")).show()
df.describe().show()


# In[18]:

df = sqlCtx.createDataFrame(
    [
        ['No','young', 'false', 'false', 'fair'],
        ['No','young', 'false', 'false', 'good'],
        ['Yes','young', 'true', 'false', 'good'],
        ['Yes','young', 'true', 'true', 'fair'],
        ['No','young', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'fair'],
        ['No','middle', 'false', 'false', 'good'],
        ['Yes','middle', 'true', 'true', 'good'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','middle', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'excellent'],
        ['Yes','old', 'false', 'true', 'good'],
        ['Yes','old', 'true', 'false', 'good'],
        ['Yes','old', 'true', 'false', 'excellent'],
        ['No','old', 'false', 'false', 'fair'],
    ],
    ['cls','age','f1','f2','f3']
)


# In[19]:

from pyspark.ml.feature import StringIndexer
labelIndexer = StringIndexer(inputCol="cls", outputCol="labels")
model=labelIndexer.fit(df)
df1=model.transform(df)


# In[20]:

labelIndexer = StringIndexer(inputCol="age", outputCol="att1")
model=labelIndexer.fit(df1)
df2=model.transform(df1)
labelIndexer = StringIndexer(inputCol="f1", outputCol="att2")
model=labelIndexer.fit(df2)
df3=model.transform(df2)
labelIndexer = StringIndexer(inputCol="f2", outputCol="att3")
model=labelIndexer.fit(df3)
df4=model.transform(df3)
labelIndexer = StringIndexer(inputCol="f3", outputCol="att4")
model=labelIndexer.fit(df4)
df5=model.transform(df4)


# In[21]:

df5.show()


# In[ ]:



