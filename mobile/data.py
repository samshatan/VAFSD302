import numpy as np
import pandas as pd
data={
"Name": ['Alice','Bob','Charlie','David','Edward'],
"Age": [25,np.nan,35,45,np.nan],
"Salary": [50000,60000,np.nan,80000,1200000],
"Gender": ['Female','Male',np.nan,'Male','Female']
}
df=pd.DataFrame(data)
#print("Original DataFrame:")
#print(df)
print("Checking for missing Values: ")
print(df.isnull().sum())
#df_dropna=df.dropna()
#print("DataFrame after dropping rows missing values: ")
#print(df_dropna)
#df_fill_0=df.fillna(0)
#print("DataFrame after filling missing value with 0")
#print(df_fill_0)
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print("DataFrame after filling missing values with mean: ")
print(df)
df["Gender"]=df["Gender"].fillna(df["Gender"].mode()[0])
print("DataFrame after filling missing values with mode: ")
print(df)