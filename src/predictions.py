# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 01:01:05 2021

@author: dearr
"""
import numpy as np
import pickle
import pandas as pd
import xgboost as xgb

def predict_values(df):
    x_cols = ['inning', 'total_runs', 'ballsRemaining','wicketsRemaining', 'tot_runs', 'score_target', 'remaining_target', 'runrate', 'required_run_rate', 'runrate_diff', 'is_batting_team']
    val_X = np.array(df[x_cols[:]])
    test1 = pd.DataFrame(val_X[0])
    test1 = np.array(test1.transpose())
    xgtest = xgb.DMatrix(test1)
    
    modelodds = pickle.load(open(r'E:\Testing\Python\PredictionModel\pickle\ballbyballodds.pkl','rb'))
    model5 = pickle.load(open(r'E:\Testing\Python\PredictionModel\pickle\overs_5.pkl','rb'))
    model6 = pickle.load(open(r'E:\Testing\Python\PredictionModel\pickle\overs_6.pkl','rb'))
    model10 = pickle.load(open(r'E:\Testing\Python\PredictionModel\pickle\overs_10.pkl','rb'))
    model15 = pickle.load(open(r'E:\Testing\Python\PredictionModel\pickle\overs_15.pkl','rb'))
    model20 = pickle.load(open(r'E:\Testing\Python\PredictionModel\pickle\overs_20.pkl','rb'))
    
    df['pred_odds'] = modelodds.predict(xgtest)
    df['team1_probability'] = df['pred_odds']
    df['team1_odds'] = 1/df['team1_probability']
    df['team2_probability'] = 1 - df['team1_probability']
    df['team2_odds'] = 1/df['team2_probability']
    df['pred5'] = model5.predict(xgtest)
    df['pred6'] =  model6.predict(xgtest)
    df['pred10'] = model10.predict(xgtest)
    df['pred15'] = model15.predict(xgtest)
    df['pred20'] = model20.predict(xgtest)
    return(df)