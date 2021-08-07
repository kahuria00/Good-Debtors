import os
import pandas as pd


current_directory = os.path.realpath(
	os.path.join(os.getcwd(), os.path.dirname(__file__)))

csv_list = ["transaction_data_1.csv",'transaction_data_2.csv','transaction_data_3.csv']


for sheet in csv_list:
	if sheet == "transaction_data_1.csv":
		csv_path = f"{current_directory}/{sheet}"
		df1 = pd.read_csv(csv_path)
		df1 = df1.sort_values(by=["customer_id"],ascending=True)
		df1['transaction_date'] =  pd.to_datetime(df1['transaction_date'])
		dates = df1.groupby('customer_id').transaction_date.diff().dt.days.ne(1).cumsum()
		df1=df1.groupby(['customer_id', dates]).size().reset_index(level=1, drop=True)
		df1 = df1.idxmax()
		print(sheet,df1)


	elif sheet == "transaction_data_2.csv":
		csv_path = f"{current_directory}/{sheet}"
		df2 = pd.read_csv(csv_path)
		df2=df2.sort_values(by=["customer_id"],ascending=True)
		df2['transaction_date'] =  pd.to_datetime(df2['transaction_date'])
		dates = df2.groupby('customer_id').transaction_date.diff().dt.days.ne(1).cumsum()
		df2=df2.groupby(['customer_id', dates]).size().reset_index(level=1, drop=True)
		df2 = df2.idxmax()
		print(sheet,df2)

	elif sheet == "transaction_data_3.csv":
		csv_path = f"{current_directory}/{sheet}"
		df3 = pd.read_csv(csv_path)
		df3=df3.sort_values(by=["customer_id"],ascending=True)
		df3['transaction_date'] =  pd.to_datetime(df3['transaction_date'])
		dates = df3.groupby('customer_id').transaction_date.diff().dt.days.ne(1).cumsum()
		df3=df3.groupby(['customer_id', dates]).size().reset_index(level=1, drop=True)
		df3 = df3.idxmax()
		print(sheet,df3)
		


		
		


		
		
