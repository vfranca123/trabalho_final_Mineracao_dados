import pandas as pd

data = pd.read_csv("data/magic04.csv",na_values="?",header= None)
data.columns=["fLength","fWidth","fSize","fConc","fConc1","fAsym","fM3Long","fM3Trans","fAlpha","fDist","class"]

#Removing duplicates
if(data.duplicated().any()):
    data = data.drop_duplicates()

#identifying end removing outliers (IQR method)
columns = data.select_dtypes(include="number").columns #only numeric columns
outliers = []
for column in columns:
    Q1= data[column].quantile(0.25)
    Q3= data[column].quantile(0.75)

    #interquartile range
    IQR = Q3-Q1

    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR

    data = data[(data[column] >= lower) & (data[column] <= upper)]
    


#normalizing data (min-max) 
for column in columns:
    min = data[column].min()
    max = data[column].max()
    data[column] = (data[column]- min)/(max-min)

data.to_csv("data/magic04_preprocessed.csv",index=False)