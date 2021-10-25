import pandas as pd

dataset = 'USA_Housing.csv'
df = pd.read_csv(dataset, header=0)

# print(df.columns)
# print(df.index)

df.set_index('Address', inplace=True)
# print(df)

df.reset_index(inplace=True)
# print(df)

# print(df.iloc[0:4, 0:3])
# print(df.loc[0:4, ['Avg. Area Income', 'Avg. Area House Age']])

X = df.drop('Price', axis=1)
print(X.head())

y = df['Price']
print(y.head(10))