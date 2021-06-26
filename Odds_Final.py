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
sys.path.append(r'R:\OneDrive\Desktop\ZenMinds\Model_Code\Pickles')
from src import calculations,predictions
import requests
import pyodbc
from pandas.io import sql
import urllib
from sqlalchemy import create_engine

url = 'http://arunprabus-001-site1.etempurl.com/api/ScoredDetails/2'

def odds_final(url):
    df1 = pd.DataFrame(requests.get(url).json())
#    df1 = pd.read_csv(r'R:\OneDrive\Desktop\input.csv')
    df = df1.tail(1)
    df = calculations.get_additional_parameters(df)
    df = predictions.predict_values(df)
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=SQL5080.site4now.net;'
                          'Database=db_a75b59_arunprabus;'
                          'uid=db_a75b59_arunprabus_admin;pwd=_Cs32Nr4kccQQ7M')
    cursor = conn.cursor()
    quoted = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=SQL5080.site4now.net;DATABASE=db_a75b59_arunprabus;uid=db_a75b59_arunprabus_admin;pwd=_Cs32Nr4kccQQ7M")
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted))
    df.to_sql(con=engine, name='final_table', if_exists='append')
    return 0

h = odds_final(url)



