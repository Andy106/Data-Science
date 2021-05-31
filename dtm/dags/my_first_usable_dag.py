#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from dtm import Dtmodel
from dtm import Download

model = Dtmodel()
data = Download()

dag = DAG('my_first_usable_dag', description='My First Usable DAG',
          schedule_interval='0 12 * * *',
          start_date=datetime(2021, 5, 27), catchup=False)

download_operator = PythonOperator(task_id='task_1', python_callable=data.download_file(), dag=dag)

train_operator = PythonOperator(task_id='task_2', python_callable=model.train(), dag=dag)

predict_operator = PythonOperator(task_id='task_2', python_callable=model.predict(), dag=dag)

download_operator >> model_operator >> predict_operator

# In[ ]:




