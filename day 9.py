# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os

folder_path = r"C:\Users\soora\OneDrive\Desktop\code files\sample spyder codes"
print("Files in directory:", os.listdir(folder_path))
import pandas as pd

file_path = r"C:\Users\soora\OneDrive\Desktop\code files\sample spyder codes\Apple Stock Price History (1).csv"
superman = pd.read_csv(file_path)
print(superman.head())  

superman=pd.read_csv('Apple Stock Price History (1).csv',usecols=[0,1,2,3,4])

pohl_avg=superman[['Price','Open','High','Low']].mean(axis=1)

obs=np.arange(1,len(superman)+1,1)
plt.plot(obs,pohl_avg,'r',label='MY FIRST PLOT')
