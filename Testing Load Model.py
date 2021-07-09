#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pickle


# In[51]:


with open("TestingAja.pkl", 'rb') as file:  
    Pickled_RF_Model = pickle.load(file)

Pickled_RF_Model


# In[80]:


row = [-110.06, -8.68216, 115.197], 
    [-83.75, -8.69234, 115.174], 
    [-107.52, -8.7802, 115.178]


# In[87]:


# TestPredict = pd.read_excel('Predict.xlsx')
for x,y,z in row:
    inputan = [[x,y,z]]
    hasil = Pickled_LR_Model.predict(inputan)
    if hasil == 0:
        print(inputan, "A")
    elif hasil == 1:
        print(inputan,"B")
    elif hasil == 2:
        print(inputan,"C")
    elif hasil == 3:
        print(inputan,"D")
    elif hasil == 4:
        print(inputan,"E")
    elif hasil == 5:
        print(inputan,"F")
    elif hasil == 6:
        print(inputan,"G")


# In[ ]:




