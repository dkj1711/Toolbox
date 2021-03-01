from sklearn.impute import SimpleImputer
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import OneHotEncoder
import numpy as np
def drop_duplicates(data):
    len(data) # Check number of rows before removing duplicates
    data = data.drop_duplicates() # Remove duplicates
    len(data)# Check new number of rows
    return data
def missing_data(data,pos):
    print(data.isnull().sum().sort_values(ascending=False))
    imputer = SimpleImputer(strategy="mean") # Instanciate a SimpleImputer object with strategy of choice
    imputer.fit(data[[pos]]) # Call the "fit" method on the object
    data[pos] = imputer.transform(data[[pos]]) # Call the "transform" method on the object
    return data
def outliers(data,pos):
    print(data[[pos]].boxplot())
    print(data[pos].min()) 
    print(data[pos].max())
    false_observation = data[pos].argmin() # Get index corresponding to minimum value
    data = data.drop(false_observation).reset_index(drop=True) # Drop row
    data[[pos]].boxplot() # Visualize boxplot 
    return data
def scaling_robustscaelr(data,pos):
    r_scaler = RobustScaler() # Instanciate Robust Scaler
    r_scaler.fit(data[[pos]]) # Fit scaler to feature
    data[pos] = r_scaler.transform(data[[pos]]) #Scale
    return data
def encoding(data, pos):
    data[pos].unique()  # Check unique values for streets (3)
    ohe = OneHotEncoder(sparse = False) # Instanciate encoder
    ohe.fit(data[[pos]]) # Fit encoder
    alley_encoded = ohe.transform(data[[pos]]) # Encode alley
    data[pos],data[pos],data[pos] = alley_encoded.T # Transpose encoded Alley back into dataframe
    return data
def discretizing(data,pos,keyword1,keword2):
    data[f'{pos} binary'] = pd.cut(x = data[pos],
                       bins=[data[pos].min()-1,
                             data[pos].mean(),
                             data[pos].max()+1], 
                       labels=[keyword1, keword2])
    return data
    
