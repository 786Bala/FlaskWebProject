# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 01:01:05 2021

@author: dearr
"""
import numpy as np
import pickle
import pandas as pd
import xgboost as xgb

def predict_values(df,modelodds, model5, model6, model10, model15, model20):
    x_cols = ['inning', 'total_runs', 'ballsRemaining','wicketsRemaining', 'tot_runs', 'score_target', 'remaining_target', 'runrate', 'required_run_rate', 'runrate_diff', 'is_batting_team']
    val_X = np.array(df[x_cols[:]])
    test1 = pd.DataFrame(val_X[0])
    test1 = np.array(test1.transpose())
    xgtest = xgb.DMatrix(test1)
        
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