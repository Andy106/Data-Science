#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import pandas as pd
import sklearn

class Dataset:
    
    def __init__(self, path_to_file = 'C:\\Users\\IEUser\\Desktop\\data\\diabetes.csv'):
        self.data_dir = Path(path_to_file)
        
    def get_data(self):
        data = pd.read_csv(self.data_dir)
        X = data.drop('Outcome',axis=1)
        Y = data['Outcome']
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = .3, random_state = 101)
        return X_train, X_test, y_train, y_test


# In[ ]:




