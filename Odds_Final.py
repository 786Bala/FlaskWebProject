# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 22:15:37 2021

@author: dearr
"""
import pickle
import pandas as pd
import numpy as np
import xgboost as xgb
import json
import sys
sys.path.append(r'E:\Testing\Python\PredictionModel\pickle')
from src import calculations,predictions
import requests

#df1 = pd.read_csv(r'R:\OneDrive\Desktop\input.csv')
df1 = pd.DataFrame(requests.get("http://arunprabus-001-site1.etempurl.com/api/ScoredDetails/1").json())
df = df1.tail(1)
#f = open(r'C:\Users\dearr\Downloads\response.json')
#data = json.load(data)
#df = pd.DataFrame.from_dict(data, orient='columns')
#df = df.rename({'inningsId': 'inning', 'score': 'tot_runs'}, axis='columns')
#df = pd.read_csv(r'C:\Users\dearr\OneDrive\Desktop\Book2.csv')

df = calculations.get_additional_parameters(df)
df = predictions.predict_values(df)

d = df.to_json(orient='records')


