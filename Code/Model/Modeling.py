import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from fbprophet import Prophet

df = pd.read_csv('/content/drive/MyDrive/SmartWatchDatastore.csv')
df.date = pd.to_datetime(df.date)
df = df.sort_values(by='date') 
df = df.set_index('date')
df = df.drop('__dt', axis=1)

new_df_steps = df[['steps']].sort_values(by='date').copy()
new_df_steps = new_df_steps.loc['2020-01-01':'2020-12-31']

size_of_train = int(np.ceil(new_df_steps.shape[0] * 0.70))
train = new_df_steps.iloc[:size_of_train]
test = new_df_steps.iloc[size_of_train:]

fig, ax= plt.subplots(1, 1, figsize=(20, 6))
sns.set_style("ticks")
sns.set_context("talk")

train.plot(ax=ax)
test.plot(ax=ax, c="g")
ax.yaxis.grid(True)
ax.legend(["Treino", "Teste"])
sns.despine(offset=200, trim=False)

train_prophet = train.reset_index().rename(columns={'date': 'ds', 'steps': 'y'})
train_prophet.head()

model = Prophet(weekly_seasonality=4, seasonality_mode="multiplicative")
model.fit(train_prophet)

future = model.make_future_dataframe(periods=0, freq="MS")
forecast = model.predict(future)

fig, ax= plt.subplots(1, 1, figsize=(25, 6))
sns.set_style("ticks")

sns.set_context("talk")
model.plot(forecast, ax=ax);
ax.yaxis.grid(True)

sns.despine(offset=5, trim=False);