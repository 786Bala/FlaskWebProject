# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 00:38:41 2021

@author: dearr
"""
def get_remaining_balls(a):
    b = str.split(str(a),sep = '.')
    overs = 120 - (int(b[0])*6 + int(b[1]))    
    actual_overs = int(b[0]) + int(b[1])/6
    return(overs,actual_overs)

def get_remaining_target(row):
    if row['score_target'] == -1.:
        return -1
    else:
        return row['score_target'] - row['tot_runs']
def get_required_rr(row):
    if row['remaining_target'] == -1:
        return -1.
    elif row['over'] == 20:
        return 99
    else:
        return row['remaining_target'] / (20-row['actual_overs'])
def get_rr_diff(row):
    if row['inning'] == 1:
        return -1
    else:
        return row['runrate'] - row['required_run_rate']
def get_additional_parameters(df):
    df['ballsRemaining'],df['actual_overs'] = zip(*df['over'].apply(lambda x:get_remaining_balls(x)))
    df['wicketsRemaining'] = df['wickets'].apply(lambda x:10-x)
    df['runrate'] = df['total_runs']/df['actual_overs']
    df['remaining_target'] = df.apply(lambda row: get_remaining_target(row),axis=1)
    df['required_run_rate'] = df.apply(lambda row: get_required_rr(row), axis=1)
    df['runrate_diff'] = df.apply(lambda row: get_rr_diff(row), axis=1)
    df['is_batting_team'] = df['inning'].copy()
    di = {1: 1, 2: 0}
    df = df.replace({"is_batting_team": di})
    return(df)