#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA


# In[76]:


# 데이터 가져오기
file_path = '~/data/data/bike-sharing-demand/train.csv'
train = pd.read_csv(file_path)

# 데이터 확인
print(train.head())
print(train.info())


# In[77]:


train['datetime'] = pd.to_datetime(train['datetime'])


# In[78]:


# 연, 월, 일, 시, 분, 초 컬럼 생성
train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['minute'] = train['datetime'].dt.minute
train['second'] = train['datetime'].dt.second


# In[79]:


# 6개의 서브플롯 생성
fig, axes = plt.subplots(3, 2, figsize=(15, 10))

# 시각화
sns.countplot(data=train, x='year', ax=axes[0, 0])
sns.countplot(data=train, x='month', ax=axes[0, 1])
sns.countplot(data=train, x='day', ax=axes[1, 0])
sns.countplot(data=train, x='hour', ax=axes[1, 1])
sns.countplot(data=train, x='minute', ax=axes[2, 0])
sns.countplot(data=train, x='second', ax=axes[2, 1])

# 레이아웃 조정

plt.show()


# In[80]:


non_zero_seconds = train[train['second'] != 0]
non_zero_seconds


# In[81]:


non_zero_minute = train[train['minute'] != 0]
non_zero_minute


# In[82]:


## x에 사용될 feature 선택 , second , minute는 count 0이여서 제외 
features = [ 'hour', 'temp', 'humidity', 'windspeed', 'weather']
X = train[features]
y = train['count']


# In[83]:


X_train,X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 확인
print(X_train.shape, X_test.shape)
print(y_train.shape, y_test.shape)


# In[85]:


model = LinearRegression()
model.fit(X_train, y_train)


# In[86]:


y_pred = model.predict(X_test)


# In[87]:


mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)


# In[88]:


print(mse)
print(rmse)


# In[89]:


# temp와 count 시각화
plt.figure(figsize=(10, 5))
plt.scatter(X_test['temp'], y_test, color='blue', label='Actual Count')
plt.scatter(X_test['temp'], y_pred, color='red', label='Predicted Count')
plt.xlabel('Temperature')
plt.ylabel('Count')
plt.legend()
plt.show()


# In[90]:


# humidity와 count 시각화
plt.figure(figsize=(10, 5))
plt.scatter(X_test['humidity'], y_test, color='blue', label='Actual Count')
plt.scatter(X_test['humidity'], y_pred, color='red', label='Predicted Count')
plt.xlabel('Humidity')
plt.ylabel('Count')
plt.legend()
plt.show()


# In[ ]:




