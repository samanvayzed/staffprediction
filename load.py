#!/anaconda3/bin/python3

import numpy as np
from sklearn.externals import joblib
import sys

# Load the model that you just saved

model = joblib.load('model.pkl')

X = np.array([
[1541356200.0,   0,       1,      0,       0,       0],
[1541356200.0,   0,       1,       0,       0,        0],
[1541356200.0,   0,       1,       0,       0,        0],
[1541356200.0,   0,       1,       0,       0,        0],
[1541442600.0,   0,       0,       1,       0,        0],
[1541442600.0,   0,       1,       0,       0,        0],
[1541442600.0,   0,       0,       0,       1,        0],
[1541442600.0,   0,       0,       0,       1,        0],
[1541442600.0,   0,       1,       0,       0,        0],
[1541442600.0,   0,       1,       0,       0,        0],
[1541529000.0,   0,       0,       1,       0,        0],
[1541442600.0,   0,       1,       0,       0,        0],
[1541529000.0,   0,       1,       0,       0,        0]])

#print(X)


test_res = model.predict(X)

print(test_res)

