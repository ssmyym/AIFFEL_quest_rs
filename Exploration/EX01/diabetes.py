#!/usr/bin/env python
# coding: utf-8

# In[141]:


## data load 
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[142]:


diabetes = load_diabetes()
df_x = diabetes.data
df_y = diabetes.target


# In[143]:


## padnas values를 사용하여 numpy array로 변경 
df_x = np.array(df_x)
df_y = np.array(df_y)


# In[144]:


## train data test data split 
X_train, X_test , y_train, y_test = train_test_split(df_x, df_y, test_size = 0.2 , random_state = 42)


# In[145]:


## 10개의 feauture인 것을 확인 숫자 상수 b 1개 
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)


# In[146]:


W = np.random.rand(X_train.shape[1])
b = np.random.rand()


# In[147]:


def model(X,w,b):
    predictions = 0
    for i in range(10):
        predictions += X[:,i] * W[i]
    predictions += b
    return predictions


# In[148]:


def MSE(a , b):
    mse = ((a - b) ** 2).mean()
    return mse


# In[149]:


def loss(X,W,b,y):
    predictions = model(X,W,b)
    L = MSE(predictions,y)
    return L


# In[150]:


def gradient(X,W,b,y):
    ## data point 개수 
    N = len(y)
    
    y_pred = model(X,W,b)
    
    # 공식에 맞게 gradient 계산
    dW = 1/N * 2 * X.T.dot(y_pred - y)
        
    # b의 gradient 계산
    db = 2 * (y_pred - y).mean()
    return dW, db


# In[151]:


dw, db = gradient(X_train,W,b,y_train)
print("dW:", dw)
print("db:", db)


# In[153]:


LEARNING_RATE = 0.165


# In[154]:


losses = [] 

for i in range(1, 1001):
    dW, db = gradient(X_train, W, b, y_train)
    W -= LEARNING_RATE * dW
    b -= LEARNING_RATE * db
    L = loss(X_train, W, b, y_train)
    losses.append(L)
    if i % 10 == 0:
        print('Iteration %d : Loss %0.4f' % (i, L))


# In[155]:


plt.plot(losses)
plt.show()


# In[156]:


W, b


# In[157]:


prediction = model(X_test, W, b)
mse = loss(X_test, W, b , y_test)
mse


# In[158]:


plt.scatter(X_test[:, 0], y_test)
plt.scatter(X_test[:, 0], prediction)
plt.show()


# In[ ]:




