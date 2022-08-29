import pandas as pd
import numpy as np

data=pd.read_csv('25day_dataset.csv') #read dataset as a dataframe


data.drop(1461218, inplace=True)  #data cleaning

data.loc[data.wahing_machine>0.0,'wahing_machine']= 1.0 #class 1

data.loc[data.dishwasher>0.0,'dishwasher']= 2.0 #class2

data.loc[data.oven>0.0,'oven']= 3.0 #class 3

dc = data[['wahing_machine','dishwasher','oven']].sum(axis=1) #create a new classes's dataframe

data["classe"] = dc #create a new class column with dc dataframe

features = data.iloc[:,0:12]
label = data.iloc[:, 16]
classes = list(np.unique(label))
Nclasses = len(classes)

print(classes) #print delle classi 0.0(nessuno dispositivo acceso) 1.0(wahing_machine) 2.0(dishwasher) 3.0(oven)
