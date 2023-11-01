#!/usr/bin/env python
# coding: utf-8

# # Spam Filter

# In[133]:


import numpy as np
import pandas as pd
import os
import nltk
import statsmodels.api as sm
import seaborn as sns
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.stem.porter import PorterStemmer
import string
from wordcloud import WordCloud


# In[69]:


sns.set()


# ## doc file--> xem bo du lieu co gi

# In[70]:


raw_d=pd.read_csv('spam_ham_dataset.csv')
print(raw_d)


# In[71]:


raw_d.head(10)


# In[72]:


raw_d=raw_d.drop('Unnamed: 0', axis=1)


# In[73]:


raw_d.head()


# ## Tao ham 

# In[74]:


subjects = []
for i in range(len(raw_d)):
    ln = raw_d["text"][i]
    line = ""
    for i in ln:
        if(i == '\r'):
            break
        line = line + i
    line = line.replace("Subjects: ", "")
    subjects.append(line)


# In[75]:


raw_d['Subjects'] = subjects
data1 = raw_d.copy()


# In[76]:


data1.describe() # ham describe : mo ta data, thong ke mot so yeu to co ban


# In[77]:


data1.info()


# In[78]:


data1.duplicated().sum()


# In[79]:


data1 = data1.drop_duplicates(keep='first')


# In[80]:


data1


# In[81]:


data1.shape


# ## EDA Exploratory Data Analysis – Phân tích Khám phá Dữ liệu

# In[82]:


palette_color = sns.color_palette('bright')
s= data1['label'].value_counts()
# Ve du lieu
plt.pie(s, data= data1 , labels = s.index, colors = palette_color, autopct='%.0f%%')
plt.show()


# In[83]:


nltk.download('punkt')


# ### nltk : Natural Language Toolkit - xử lý ngôn ngữ tự nhiên thống kê

# In[84]:


data1['len_alphabets'] = data1['Subjects'].apply(len)
data1['len_words'] = data1['Subjects'].apply(lambda x:len(nltk.word_tokenize(x)))
data1['len_words']


# In[85]:


data1['len_sent'] = data1['Subjects'].apply(lambda x:len(nltk.sent_tokenize(x)))
data1['len_sent']


# In[86]:


data1.head(10)


# ### For spam

# In[87]:


data1[data1['label_num']==1][['len_alphabets','len_words','len_sent']].describe()


# In[88]:


plt.figure(figsize=(12,6))
sns.histplot(data1[data1['label_num']==0]['len_alphabets'])
sns.histplot(data1[data1['label_num']==1]['len_alphabets'], color='red')


# In[89]:


plt.figure(figsize=(12,6))
sns.histplot(data1[data1['label_num']==0]['len_words'])
sns.histplot(data1[data1['label_num']==1]['len_words'], color='red')


# In[90]:


sns.pairplot(data1, hue='label_num')


# In[91]:


sns.heatmap(data1.corr(), annot=True)


# # Data preprocessing 

# ## All Lower case
# ## Tokenization
# ## No special characters
# ## Removing stop words/punctuation
# ## Stemming

# In[95]:


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopwords.words('english')


# In[96]:


import string
string.punctuation


# ### ham chuyen doi

# In[123]:


from nltk.stem.porter import PorterStemmer
ps= PorterStemmer()


# In[128]:


def transform_text(text):
    text =text. lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)


# In[130]:


ps=PorterStemmer()


# In[131]:


data1['transformed_text']=data1['Subjects'].apply(transform_text)
data1.head(10)


# ## Generating Word cloud - tao dam may luu word

# In[138]:


wc=WordCloud(width = 2000, height = 2000, min_font_size=10, background_color = 'white')


# In[139]:


spam_wc=wc.generate(data1[data1['label']== 'spam']['transformed_text'].str.cat(sep=" "))


# In[140]:


plt.figure(figsize=(13, 13))
plt.title("Most common words in Spam email Subjects", fontdict={'size': 20, 'color': 'black', 
                                  'verticalalignment': 'bottom'})
plt.imshow(spam_wc)


# In[141]:


ham_wc= wc.generate(data1[data1['label']=='ham']['transformed_text'].str.cat(sep=" "))


# In[142]:


plt.figure(figsize=(13, 13))
plt.title("Most common words in Spam email Subjects", fontdict={'size': 20, 'color': 'black', 
                                  'verticalalignment': 'bottom'})
plt.imshow(ham_wc)


# In[ ]:




