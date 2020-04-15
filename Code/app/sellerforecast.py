#!/usr/bin/env python
import mysql.connector
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import warnings
import datetime
import os
import sys

def sforecast(query):
	today = str(datetime.date.today())
	lst = [None]*15
	for i in range(len(lst)):
		lst[i] = 0
	for i in range(0,15):
		datei = datetime.datetime.now() - datetime.timedelta(days=i)
		lst[i]=str(datei).split(" ")[0]
	lst.reverse()
	warnings.filterwarnings("ignore")
	mydb=mysql.connector.connect(host='localhost',user='root',password='',database='ec')
	mycursor=mydb.cursor()
	mycursor.execute(query) 
	result=mycursor.fetchall()
	lst2= [None]*len(lst)
	for i in range(len(lst)):
		lst2[i] = 0
	for i in range(len(result)):
		if str(result[i][1]).split(" ")[0] in lst:
			a=lst.index(str(result[i][1]).split(" ")[0])
			lst2[a] = int(result[i][0])
	for i in lst2:
		i = float(i)
	df = pd.DataFrame(list(zip(lst, lst2)), 
		columns =['Dat', 'Sales']) 
	con=df['Dat']
	df['Dat']=pd.to_datetime(df['Dat'])
	df.set_index('Dat', inplace=True)

	np.seterr(divide = 'ignore')
	df = df['Sales']
	fit = ExponentialSmoothing((df) ,seasonal_periods=7 ,trend='add', seasonal='add').fit()
	fit1 = fit.forecast(len(df))
	df.plot(kind="line",figsize=(10,5),color='blue')
	fit1.plot(kind="line",figsize=(10,5),color='red')
	plt.xlabel('Sales per Day')
	plt.ylabel('Day')
	plt.savefig('app/static/sgraph.png')
if __name__ == "__main__":
	#print(sys.argv[1])
	sforecast(sys.argv[1])