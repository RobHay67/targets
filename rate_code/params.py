

from types import SimpleNamespace



def set_params():
	params = SimpleNamespace( 
								rates_df_columns = ['campaign', 'payment_country', 'region', 'tenure',  'metric', 'result', 'formula', 'finance_measure'],
								finance_description = False,
								nrows 				= 1000,
								campaign 			= 2021,
								# Set Name Variables
								current_campaign = '2022',
								previous_campaign = '2021',
								retained_campaign = '2020',
								)
	# project_params(params, project_description)
	# market_params(params)
	# terminal_params(params, args)
	# folder_params(params)
	# share_index_params(params, args)
	# analysis_params(params, args)
	# share_data_params(params)
	# download_params(params, args)
	# strategy_params(params, args)
	# chart_params(params)

	
	# print_share_index_industries(params)
	
	

	return params