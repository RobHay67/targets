
# import pathlib
import pandas as pd
import os




def csv_params(scope, core_df_name, campaign_year):
	df_dict_path = os.path.join(scope.dir_customer_df, str( core_df_name + '_' + str( campaign_year ) + '_dict.csv') )
	df_dict        = pd.read_csv( df_dict_path, skiprows=[0], header=None).set_index(0)[1].to_dict()

	csv_read_dtypes = df_dict.copy()
	csv_read_dates = [] 
	for field, dtype in df_dict.items():
		if dtype in ['datetime64[ns]', 'datetime64[ns, Australia/Melbourne]']: 
			csv_read_dates.append(field)     # add date fields to list of dates
			del csv_read_dtypes[field]      # remove any date fields from the dtype dictionary

	return csv_read_dtypes, csv_read_dates

def load_customer_dataframe( scope, core_df_name, campaign_year, nrows=None ):
	df_file_path = os.path.join(scope.dir_customer_df, str( core_df_name + '_' + str( campaign_year ) +      '.csv') ) 

	csv_read_dtypes, csv_read_dates = csv_params(scope, core_df_name, campaign_year)
	core_df           = pd.read_csv( df_file_path, 
									dtype=csv_read_dtypes, 
									parse_dates=csv_read_dates, 
									nrows=nrows,
								   )
	if core_df_name =='Customers': 
		print ( ('columns = ' + str(len(core_df.columns)) ).ljust(15), ('rows = ' + str(len(core_df))).ljust(20), ('total LCL donations = ' + str(round(core_df.lcl_fundr_total.sum(),2))).ljust(40),           (' - Finished loading ' +  str(core_df_name)).ljust(40), 'campaign year =', campaign_year, )
	elif core_df_name =='Donations':
		print ( ('columns = ' + str(len(core_df.columns)) ).ljust(15), ('rows = ' + str(len(core_df))).ljust(20), ('total LCL donations = ' + str(round(core_df.lcl_fundr_total.sum(),2))).ljust(40),           (' - Finished loading ' +  str(core_df_name)).ljust(40), 'campaign year =', campaign_year, )
	else:                                                             
		print ( ('columns = ' + str(len(core_df.columns)) ).ljust(15), ('rows = ' + str(len(core_df))).ljust(20), ('total LCL donations = ' + str(round(core_df.value_lcl_total_donations.sum(),2))).ljust(40), (' - Finished loading ' +  str(core_df_name)).ljust(40), 'campaign year =', campaign_year, )
	return core_df




def scope_paths(scope):

	# Project Folder
	dir_project_dir = os.path.abspath(os.curdir)
	
	# Customer Dataframe Folder
	home_dir = os.path.expanduser( '~' )
	scope.dir_customer_df = os.path.join(home_dir, 'amazon_s3', 'dataframes')


	# Target Rates Path
	target_rate_filename = 'target_rates_' + str((scope.campaign_previous+1)) + '.csv'
	scope.path_target_rates = os.path.join(dir_project_dir, 'rate_code', 'files', target_rate_filename)

	# Finance Rates Path
	finance_rates_filename = 'finance_rates_' + str((scope.campaign_previous+1)) + '.csv'
	scope.path_finance_rates = os.path.join(dir_project_dir, 'rate_code', 'files', finance_rates_filename)











