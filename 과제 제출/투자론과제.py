# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 00:04:20 2018

@author: 삼성컴퓨터
작성 날짜: 2018-03-30
참고 논문: 
    -주식_기대수익률의_횡단면에_관한_실증연구(2013. 강장구)
    -복권성향 주식선호 횡단면분석(2012. 김규영)
과제 수행 수업: 투자론

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import scipy

os.chdir('C:\Users\\한승표\Desktop\대학원수업\투자론\투자론 과제\복권성향 주식선호 횡단면분석')
#일별 수익률
data=pd.read_excel('dailydata.xlsx', index_col='time')
data.index=pd.DatetimeIndex(data.index)
data_max=data.resample('M').max()
data_max_t=data_max.T
#매달 수익률
month_ret=pd.read_excel('monthdata.xlsx', index='time', index_col='time')
month_ret.index=pd.DatetimeIndex(month_ret.index)
month_ret_t=month_ret.T

b=[]
for i in list(data_max_t.columns.values):
    data_max_t_a=data_max_t.sort_values([i], ascending=True)
    b.append(data_max_t_a.index.values)

1_buffer=[]
2_buffer=[]
3_buffer=[]
4_buffer=[]
5_buffer=[]
for i in range(len(b)):
    first=b[i][:20]
    second=b[i][20:40]
    third=b[i][40:60]
    fourth=b[i][60:80]
    fifth=b[i][80:]
    1_buffer.append(first)
    2_buffer.append(second)
    3_buffer.append(third)
    4_buffer.append(fourth)
    4_buffer.append(fifth)
    
1_r=[]   
for j in range(len(list(month_ret_t.columns.values))-1):
    1_buffer_r = []
    for i in range(len(1_buffer[0])):
        a = month_ret_t[month_ret_t.index.str.startswith(1_buffer[j][i])].iloc[0]
        1_buffer_r.append(a[j+1])
    1_r.append(1_buffer_r)


2_r=[]   
for j in range(len(list(month_ret_t.columns.values))-1):
    2_buffer_r = []
    for i in range(len(2_buffer[0])):
        a = month_ret_t[month_ret_t.index.str.startswith(2_buffer[j][i])].iloc[0]
        2_buffer_r.append(a[j+1])
    2_r.append(2_buffer_r)
    
3_r=[]   
for j in range(len(list(month_ret_t.columns.values))-1):
    3_buffer_r = []
    for i in range(len(3_buffer[0])):
        a = month_ret_t[month_ret_t.index.str.startswith(3_buffer[j][i])].iloc[0]
        3_buffer_r.append(a[j+1])
    3_r.append(3_buffer_r)

4_r=[]   
for j in range(len(list(month_ret_t.columns.values))-1):
    4_buffer_r = []
    for i in range(len(4_buffer[0])):
        a = month_ret_t[month_ret_t.index.str.startswith(4_buffer[j][i])].iloc[0]
        4_buffer_r.append(a[j+1])
    4_r.append(4_buffer_r)
    
5_r=[]   
for j in range(len(list(month_ret_t.columns.values))-1):
    5_buffer_r = []
    for i in range(len(5_buffer[0])):
        a = month_ret_t[month_ret_t.index.str.startswith(5_buffer[j][i])].iloc[0]
        5_buffer_r.append(a[j+1])
    5_r.append(5_buffer_r)

    
1_mean=[]
for i in 1_r:
    listSum = sum(i)
    listLength = len(i)
    1_mean.append(listSum / listLength)

2_mean=[]
for i in 2_r:
    listSum = sum(i)
    listLength = len(i)
    2_mean.append(listSum / listLength)

3_mean=[]
for i in 3_r:
    listSum = sum(i)
    listLength = len(i)
    3_mean.append(listSum / listLength)

4_mean=[]
for i in 4_r:
    listSum = sum(i)
    listLength = len(i)
    4_mean.append(listSum / listLength)

5_mean=[]
for i in 5_r:
    listSum = sum(i)
    listLength = len(i)
    5_mean.append(listSum / listLength)

1_mean = pd.DataFrame(1_mean)
2_mean = pd.DataFrame(2_mean)
3_mean = pd.DataFrame(3_mean)
4_mean = pd.DataFrame(4_mean)
5_mean = pd.DataFrame(5_mean)

pf=pd.concat([1_mean,2_mean,3_mean, 4_mean, 5_mean], axis=1)
pf.index=data_max.index[1:]
pf.to_csv('pf.csv')
