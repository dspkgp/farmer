import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

# Load the diabetes dataset
iris_X, iris_y = load_iris(return_X_y=True)

df = pd.DataFrame(iris_X, columns=['col1', 'col2', 'col3', 'col4'])
df['target'] = pd.Series(iris_y)

df.to_csv('data_raw.csv', index=False)
