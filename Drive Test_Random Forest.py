#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#df = pd.read_excel ('')
#df.head()


# In[2]:


df.drop("A", axis=1, inplace=True)
df.drop("B", axis=1, inplace=True)
df.drop("C", axis=1, inplace=True)
df.drop("D", axis=1, inplace=True)
df.head()


# In[3]:


df["A"].replace({"-": "Testing"}, inplace=True)

print(df)


# In[11]:


scoring = 'accuracy'
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection 
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from matplotlib import pyplot
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from numpy import mean
from numpy import std


# In[5]:


X= df.drop("COLO",axis=1)
y= df["COLO"]


# In[6]:


le = LabelEncoder()
y = le.fit_transform(y)


# In[7]:


labels_dict = {index: value for index, value in enumerate(le.classes_)}
labels_dict


# In[8]:


from imblearn.over_sampling import SMOTE

# transform the dataset
oversample = SMOTE()
X, y = oversample.fit_resample(X, y)
# summarize distribution
counter = Counter(y)
for k,v in counter.items():
	per = v / len(y) * 100
	print('Class=%d, n=%d (%.3f%%)' % (k, v, per))
# plot the distribution
pyplot.bar(counter.keys(), counter.values())
pyplot.show()


# In[9]:


from sklearn.model_selection import train_test_split
validation_size = 0.20
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = validation_size, random_state = 1)


# In[12]:


model = RandomForestClassifier(bootstrap=True, class_weight='balanced', criterion='gini',
            max_depth=None, max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1,
            oob_score=False, random_state=None, verbose=0,
            warm_start=False)


model.fit(X_train,y_train)
y_pred=model.predict(X_test)

#evaluate each model in turn
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=5, random_state=1)
n_scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')

print('Accuracy: %.3f (%.3f)' % (mean(n_scores), std(n_scores)))


# In[13]:


from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))


# # SAVE MODEL

# In[ ]:


import pickle


# In[ ]:


Pkl_Filename = "testsave2.pkl"  

with open(Pkl_Filename, 'wb') as file:  
    pickle.dump(model, file)

