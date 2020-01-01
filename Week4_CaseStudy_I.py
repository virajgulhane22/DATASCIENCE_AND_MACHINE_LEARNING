# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:44:00 2019

@author: Dell
"""
import pandas as pd
import numpy as np
import seaborn as sns

#Setting Dimensions for plot
sns.set(rc={'figure.figsize':(11.7,8.27)})


#Reading CSV file
cars_data=pd.read_csv('cars_sampled.csv')

#Creating Copy
cars=cars_data.copy()


#Structure of data
cars.info()


#Summarizing data
cars.describe()
pd.set_option('display.float_format',lambda x: '%.3f' %x)
cars.describe()
