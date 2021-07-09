#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pickle


# In[51]:


with open("testsave2.pkl", 'rb') as file:  
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
        print(inputan, "Build")
    elif hasil == 1:
        print(inputan,"H3I DT")
    elif hasil == 2:
        print(inputan,"ISAT DT")
    elif hasil == 3:
        print(inputan,"Protel")
    elif hasil == 4:
        print(inputan,"TSEL DT")
    elif hasil == 5:
        print(inputan,"XL MR")
    elif hasil == 6:
        print(inputan,"XL DT")


# In[ ]:




