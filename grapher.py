# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 19:44:48 2020

@author: chris
"""
import pandas as pd
import matplotlib.pyplot as plt
import colorcet as cc


users = pd.read_csv('raw_data/internet-users.csv')
density = pd.read_csv('raw_data/pop-density.csv')
income = pd.read_csv('raw_data/gdp-per-capita.csv')
colors = cc.cm.CET_L17
x = density['2017']
y = income['2017']
user_data = users['2017']

plt.scatter(x, y, c=user_data, s=(user_data*5), alpha=0.7, cmap=colors)
plt.title('Percentage of Internet Users by \n Population Density and GDP per Capita', pad=20)
plt.xlim(0, 100)
plt.ylim(0, 80000)
plt.xlabel('Population Density (in people per sq. km)', labelpad=10)
plt.ylabel('GDP per capita (in USD)', labelpad=10)
plt.style.use('seaborn')
cbar = plt.colorbar()
cbar.set_label('Percentage of population online', fontsize=11)
