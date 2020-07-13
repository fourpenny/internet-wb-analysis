# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 14:31:47 2020

@author: chris
"""
import pandas as pd
import matplotlib.pyplot as plt

years = []

starting_year = 1960
ending_year = 2019
counter = 0

while counter <= (ending_year - starting_year):
    year_to_add = starting_year + counter
    years.append(str(year_to_add))
    print(years)
    counter += 1

online = pd.read_csv('raw_data/internet-users.csv')
gdppc = pd.read_csv('raw_data/gdp-per-capita.csv')

countries1 = online["Country Name"]
usinternet = online.loc[countries1 == "United States"]

countries2 = gdppc["Country Name"]
usgdp = gdppc.loc[countries2 == "United States"]

