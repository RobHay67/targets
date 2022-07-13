
import pathlib
import pandas as pd


folder_customer_df = pathlib.Path.home().joinpath( 'amazon_s3', 'dataframes' )


def csv_params(core_df_name, campaign_year):

	df_dict_path   = pathlib.Path.joinpath( folder_customer_df, str( core_df_name + '_' + str( campaign_year ) + '_dict.csv') )
	df_dict        = pd.read_csv( df_dict_path, skiprows=[0], header=None).set_index(0)[1].to_dict()
	
	csv_read_dtypes = df_dict.copy()
	csv_read_dates = [] 
	for field, dtype in df_dict.items():
		if dtype in ['datetime64[ns]', 'datetime64[ns, Australia/Melbourne]']: 
			csv_read_dates.append(field)     # add date fields to list of dates
			del csv_read_dtypes[field]      # remove any date fields from the dtype dictionary

	return csv_read_dtypes, csv_read_dates

def load_customer_dataframe( core_df_name, campaign_year, nrows=None ):
	df_file_path   = pathlib.Path.joinpath( folder_customer_df, str( core_df_name + '_' + str( campaign_year ) +      '.csv') ) 
	csv_read_dtypes, csv_read_dates = csv_params(core_df_name, campaign_year)
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




