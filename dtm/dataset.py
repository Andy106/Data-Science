#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import pandas as pd
import sklearn

class Dataset:
        
    def get_data(self, path_to_file = 'C:\\D Drive\\Data Science\\MLOps\\Data-Science-feature-decision_tree_model\\dtm\\data\\diabetes.csv'):
        data = pd.read_csv(path_to_file)
        X = data.drop('Outcome',axis=1)
        Y = data['Outcome']
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = .3, random_state = 101)
        return X_train, X_test, y_train, y_test


# In[ ]:




