#!/usr/bin/env python
# coding: utf-8

# # COLLECTING DATA

# In[71]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score,learning_curve,validation_curve
from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn import svm, naive_bayes, metrics
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, precision_score, recall_score
import matplotlib.pyplot as plt
from nltk.stem import LancasterStemmer
import nltk
nltk.download("punkt")
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split as ttsplit
import pickle
from sklearn.naive_bayes import MultinomialNB, GaussianNB
import os
import statsmodels.api as sm
import seaborn as sns
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.stem.porter import PorterStemmer
import string
from wordcloud import WordCloud


# In[72]:


sns.set()


# # PREPARING DATA

# In[73]:


raw_d=pd.read_csv('spam_ham_dataset.csv')
print(raw_d)


# In[74]:


raw_d.head(10)


# In[75]:


raw_d = raw_d.drop('Unnamed: 0', axis=1)


# In[91]:


subjects = []
for i in range(len(raw_d)):
    ln = raw_d["text"][i]
    line = ""
    for i in ln:
        if(i == '\r'):
            break
        line = line + i
    line = line.replace("Subject: ", "")
    subjects.append(line)


# In[92]:


raw_d['Subject'] = subjects
data1 = raw_d.copy()


# In[93]:


data1.describe()


# In[94]:


data1.info()


# In[95]:


data1.duplicated().sum()


# In[96]:


data1 = data1.drop_duplicates(keep='first')


# In[97]:


data1


# In[109]:


# Gán cột Subject vừa xử lý xong là trục X
message_X = data1.iloc[:,-1]
message_X


# In[110]:


# Gán cột label vừa xử lý xong là trục Y
label_Y = data1.iloc[:,0]
label_Y


# In[111]:


# Hiển thị thống kê dữ liệu cột Label
count_class = pd.value_counts(data1['label'], sort= True)
count_class.plot(kind='bar',color= [ 'blue', 'red'])
plt.title('Statistical bar chart by label!')


# # CHOOSING MODEL

# In[112]:


# Khởi tạo biến lọc dữ liệu
lstem = LancasterStemmer()
def mes(messages):
    message_x = []
    for me_x in messages:
        # Lọc dữ liệu ngoài trừ bảng chữ cái
        me_x=''.join(filter(lambda mes:(mes.isalpha() or mes == " "), me_x))
        # Chia nhỏ các body emaill thành các từ
        words = word_tokenize(me_x)
        # Nhóm các từ gốc lại
        message_x+=[' '.join([lstem.stem(word) for word in words])]
    return message_x


# In[118]:


message_x = mes(message_X)
# Xử lý các túi từ, vector hóa, bỏ các từ dừng stopwords không cần thiết
tfvec = TfidfVectorizer(stop_words = 'english')
# Vectorizing feature data
# Đưa dữ liệu về dạng vector
x_new = tfvec.fit_transform(message_x).toarray()


# In[119]:


# Ham= 0 , spam =1 
y_new = data1['label_num']


# In[121]:


# tách dataset thành 80% training và 20% testing
x_train, x_test, y_train, y_test = ttsplit(x_new, y_new, test_size=0.2, random_state=1)


# In[123]:


classifier = MultinomialNB()
classifier.fit(x_train, y_train)


# # TRAINING MODEL

# In[133]:


# Định nghĩa range cho training size
train_sizes = np.linspace(0.1, 1.0, 10)
# Sử dụng learing curve cho NB model
train_sizes, train_scores, val_scores = learning_curve(classifier, x_train, y_train, train_sizes = train_sizes, cv=5)
# Tính giá trị trung bình và độ lệch cho training và validation scores
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
val_scores_mean = np.mean(val_scores, axis=1)
val_scores_std = np.std(val_scores , axis=1)
# Vẽ curve
plt.figure()
plt.title(' Learing curve Naive_bayes algorithm !')
plt.ylabel(' Accuracy')
plt.grid()
plt.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha= 0.1, color = 'r')
plt.fill_between(train_sizes, val_scores_mean - val_scores_std, val_scores_mean + val_scores_std, alpha= 0.1, color = 'g')
plt.plot(train_sizes, train_scores_mean, 'o-', color = 'r', label = "Training score")
plt.plot(train_sizes, val_scores_mean, 'o-', color = 'g', label = "Cross-validation score")
plt.legend(loc="best")
plt.show()


# # MAKING DECISION

# In[128]:


# Tính độ chính xác
Accuracy = accuracy_score(y_test, classifier.predict(x_test))
Precision= precision_score(y_test, classifier.predict(x_test))
Recall = recall_score(y_test, classifier.predict(x_test))
F1_Score = f1_score(y_test, classifier.predict(x_test))
print('Accuracy : {:.2f}%'.format(Accuracy*100))
print('Precision : {:.2f}%'.format(Precision*100))
print('Recall : {:.2f}%'.format(Recall*100))
print('F1_Score : {:.2f}%'.format(F1_Score*100))


# In[130]:


# Tính toán confusion
m_confusion_test= metrics.confusion_matrix(y_test, classifier.predict(x_test))
pd.DataFrame(data  = m_confusion_test, columns = [' Dự đoán (Ham)', ' Dự đoán (Spam)'],
            index = [' Thực tế (Ham)', ' Thực tế (Spam)'])


# In[132]:


# Biểu diễn bằng biểu đồ
cmat = confusion_matrix(y_test, classifier.predict(x_test))
print(' Confusion Matrix is : \n', cmat)
plt.figure(figsize=(6,6))
sns.heatmap(cmat, annot =True, cmap = 'Paired', cbar= False, fmt='d', xticklabels =[' Dự đoán (Ham)', ' Dự đoán (Spam)'], yticklabels=[' Thực tế (Ham)', ' Thực tế (Spam)'])


# In[ ]:




