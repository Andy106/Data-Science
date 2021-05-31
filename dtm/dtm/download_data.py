#!/usr/bin/env python
# coding: utf-8

# In[19]:


from kaggle.api.kaggle_api_extended import KaggleApi


# In[20]:


class Download:
    
    def __init__(self):
        self.api = KaggleApi()
        self.api.authenticate()
        
    def download_file(self):
        self.api.dataset_download_file('saurabh00007/diabetescsv',file_name='diabetes.csv',path='C:\\D Drive\\Data Science\\MLOps\\Data-Science-feature-decision_tree_model\\data')

