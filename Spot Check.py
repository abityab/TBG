#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_excel ('aaaa.xlsx') 
df.head()


# In[2]:


df.drop("A", axis=1, inplace=True)
df.drop("B", axis=1, inplace=True)
df.drop("C", axis=1, inplace=True)
df.drop("D", axis=1, inplace=True)
df.head()


# In[3]:


colo = pd.get_dummies(df['COLO'], drop_first=True)
colo.head()


# In[4]:


df=pd.concat([df,colo],axis=1)
df.drop(['COLO'],axis=1,inplace=True)
df.head()


# In[5]:


#spot check algorithm
scoring = 'accuracy'
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection 
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


# In[7]:


X= df.drop("XL",axis=1)
y= df["XL"]


# In[14]:


validation_size = 0.2
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = validation_size)


# In[15]:


models =[]
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

#evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = model_selection.KFold(n_splits=10)
    cv_results = model_selection.cross_val_score(model, X_train, y_train, cv = kfold, scoring = scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)


# In[ ]:




