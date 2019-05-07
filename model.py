#!/anaconda3/bin/python3

import datetime
import time
import pandas as pd
import os
import sys
import numpy as np 

from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn.ensemble import RandomForestRegressor
 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error

pd.set_option('display.max_rows', 2000)
#eid,epochtime,sales

df = pd.read_csv('data.csv', names=['eid', 'epochtime','sales'])

df = df.iloc[1:]
print(df)


categoricals = ['eid']


x_ohe = pd.get_dummies(df, columns=categoricals, dummy_na=True)
#print(x_ohe)

sys.exit()

dependent_variable = 'sales'

X = x_ohe[x_ohe.columns.difference([dependent_variable])]
y = x_ohe[dependent_variable]


# It is very important to check the order of columns in X lest we get negative values

X = X[['epochtime','eid_110','eid_49','eid_55','eid_74','eid_nan']]

#print(X)
#print(y)


############################
# Train Test Split
###########################
 
x1, x2, y1, y2 = train_test_split(X,y, test_size=0.1,random_state=0)
assert len(x1) == len(y1)
assert len(x2) == len(y2)

 
########################
# Linear Regression
########################

#print("LR")
#lr = LinearRegression()

#lr.fit(x1,y1)
#y_pred_lr = lr.predict(x2)
#comp_lr = np.column_stack((y2,y_pred_lr))
#print(comp_lr)



#sys.exit() 
 

############################
# Support Vector Regression
############################
 
#print("SVR")
#'C': 1e16, 'epsilon': 1000.0, 'gamma': 1e-28 
#svr = svm.SVR(C=1e16, epsilon= 1000.0, gamma= 1e-28)
 
#svr.fit(x1,y1)
#y_pred_svr = svr.predict(x2)
#comp_svr = np.column_stack((y2,y_pred_svr))
#print(comp_svr)


'''
svr = svm.SVR() 
parameters_svr = {
        'C' : [1e16,1e17,1e18],
        'epsilon' : [1e03],
        'gamma': [1e-28,1e-29]
}
reg_svr = GridSearchCV(svr, parameters_svr)
reg_svr.fit(X,y)
print(reg_svr.best_params_)
sys.exit()

'''





####################################################################################################

model = LinearRegression()
model.fit(X, y)


# Save your model

from sklearn.externals import joblib
joblib.dump(model, 'model.pkl')
print("Model dumped!")


# Load the model that you just saved
#lr = joblib.load('model.pkl')
#a =[33,1546108200.0]

#pred_test=np.array([[33,1546108200.0]])
#test_res=lr.predict(pred_test).astype('int64')

#print(lr.predict(a))

#Saving the data columns from training

model_columns = list(X.columns)
print(model_columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")
