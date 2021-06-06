1. Download the diabetes.csv dataset from  https://www.kaggle.com/saurabh00007/diabetescsv/. 
  1.1 Instructions on how to authenticate to kaggle APIs are available @ https://python.plainenglish.io/how-to-use-the-kaggle-api-in-python-4d4c812c39c7. 
  1.2 download_data.py file has the csv download code
  1.3 The csv must be downloaded and saved in the Data folder

2. dataset.py file splits this data into training and test data

3. model.py file has the method to train a decision tree model, save the pickle file to the model folder and use that model pickle file to do predictions on the test data
  
4. test.py file has the code to test the entire workflow: download data -> split into test & train data -> train model -> do predictions on test data

5. dags folder has the dag file which aims to (albeit failed to) orchestrate the the workflow described above

6. dist folder has the distribution artifacts used to upload this model to PyPi repo - https://pypi.org/project/dtm/
