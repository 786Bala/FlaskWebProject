# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 14:44:54 2021

@author: 91988
"""


import warnings
warnings.filterwarnings('ignore')
from flask import Flask,request,jsonify
from flask_restful import Resource,Api
import json
import sys
from sqlalchemy import create_engine
#sys.path.append(r'E:\Arun\Flask\FlaskWebProject\Pickle')
from src import calculations,predictions
import urllib
import pickle
import pandas as pd

app = Flask(__name__)
api = Api(app)

#strparams =  {
#			"matchid" : 1099,
#			"inning" : 999,
#			"total_runs" : 45,
#			"tot_runs" : 6,
#			"score_target" : -1,
#			"over" : 3.1,
 #           "wickets" : 2
	#	}

#df = pd.json_normalize(params)
#params = params

class appRun(object):
    def __init__(self):
        self.quoted = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=SQL5080.site4now.net;DATABASE=db_a75b59_arunprabus;uid=db_a75b59_arunprabus_admin;pwd=_Cs32Nr4kccQQ7M")
        self.engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(self.quoted))
        self.modelodds = pickle.load(open(r'Pickle\ballbyballodds.pkl','rb'))
        self.model5 = pickle.load(open(r'Pickle\overs_5.pkl','rb'))
        self.model6 = pickle.load(open(r'Pickle\overs_6.pkl','rb'))
        self.model10 = pickle.load(open(r'Pickle\overs_10.pkl','rb'))
        self.model15 = pickle.load(open(r'Pickle\overs_15.pkl','rb'))
        self.model20 = pickle.load(open(r'Pickle\overs_20.pkl','rb'))


runObj = appRun()

@app.route('/')

def index():
    return "Hello World!"


@app.route("/search", endpoint = 'search', methods=["POST"])

def search():
    #df = df1.tail(1)
    params = request.get_json()
    df = pd.json_normalize(params)
    df = calculations.get_additional_parameters(df)
    df = predictions.predict_values(df,runObj.modelodds,runObj.model5,runObj.model6,runObj.model10,runObj.model15,runObj.model20)
    df.to_sql(con=runObj.engine, name='final_table', if_exists='append')
    #df2 = pd.read_sql("select * from final_table",con = runObj.engine)
    return 'Success'

@app.route('/healthcheck')
def hello():
    return 'Healthy'


if __name__ == "__main__":
    app.run(debug=True)