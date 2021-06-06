#!/usr/bin/env python
# coding: utf-8

# In[19]:


from kaggle.api.kaggle_api_extended import KaggleApi


# In[20]:


class Download:
    
    def __init__(self):
        self.api = KaggleApi()
        self.api.authenticate()
        
    def download_file(self, path_to_file = 'C:\\D Drive\\Data Science\\MLOps\\Data-Science-feature-decision_tree_model\\dtm\\data'):
        self.api.dataset_download_file('saurabh00007/diabetescsv',file_name='diabetes.csv',path= path_to_file)

