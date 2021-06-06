#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import sklearn
import pickle

from dtm import Dataset


# In[8]:


class Dtmodel:
    
    def __init__(self):
        dset = Dataset()
        self.X_train, self.X_test, self.y_train, self.y_test = dset.get_data()
        
    def train(self, path_to_file = 'C:\\D Drive\\Data Science\\MLOps\\Data-Science-feature-decision_tree_model\\dtm\\model\\model.pickle'):
        from sklearn.tree import DecisionTreeClassifier
        classifier = DecisionTreeClassifier(max_depth=4)
        classifier.fit(self.X_train, self.y_train)
        filename = path_to_file
        pickle.dump(classifier, open(filename, 'wb'))
        
    def predict(self, path_to_file = 'C:\\D Drive\\Data Science\\MLOps\\Data-Science-feature-decision_tree_model\\dtm\\model\\model.pickle'):
        filename = path_to_file
        loaded_model = pickle.load(open(filename, 'rb'))
        prediction = loaded_model.predict(self.X_test)
        from sklearn.metrics import accuracy_score
        return (accuracy_score(self.y_test, prediction))


# In[ ]:




