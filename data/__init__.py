import pandas as pd
import numpy as np
# tesing
df = pd.read_csv('time_passenger_data.csv', sep=',')
df.set_index(df['time'])
print(df.head(5))
print(df.dtypes)
#data_all = np.array(df).astype(float)

print("-------------------------")
df = pd.read_csv('../data/pre.csv', sep=',')
print(df.shape,df.dtypes)
for(t,p) in df.iterrows():
    print(t,p)