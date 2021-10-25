import pandas as pd
dataset = 'Banking_Marketing.csv'

df = pd.read_csv(dataset, header=0)
# print(df.dtypes)
sum_of_na = df.isna().sum()
# print(sum_of_na)
df_2 = df.dropna()
sum_of_na_2 = df_2.isna().sum()
# print(sum_of_na_2)

mean_age = df.age.mean()
# print(mean_age)
mean_age_2 = df.age.fillna(mean_age, inplace=True)

median_duration = df.duration.median()
# print(median_duration)
median_duration_2 = df.duration.fillna(median_duration, inplace=True)
