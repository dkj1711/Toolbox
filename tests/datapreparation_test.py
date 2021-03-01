from Toolbox.DataPreparation import *
data = pd.read_csv("https://wagon-public-datasets.s3.amazonaws.com/Machine%20Learning%20Datasets/ML_Houses_dataset.csv")
data = data[['GrLivArea','BedroomAbvGr','KitchenAbvGr', 'OverallCond','RoofSurface','GarageFinish','CentralAir','ChimneyStyle','MoSold','SalePrice']].copy()

def test_duplicates(data):
    X = data.duplicated() == False
    y_dupl = True
    for i in X:
        if i == False:
            y_dupl = False
    assert y_dupl == True
def test_missing_value(data):

    X = data.isnull() == False
    y_miss = True
    for i in X:
        if i == False:
            y_miss = False
    assert y_miss == True
def test_scaler(data,pos):
    y_scaler = type(data[pos]) == type(0.33)
    assert y_scaler == True
pos = 'GrLivArea'
test_duplicates(data)
test_missing_value(data)
test_scaler(data,pos)