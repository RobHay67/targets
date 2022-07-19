

from types import SimpleNamespace
import pandas as pd
from rate_code.load_data import scope_paths


target_app_columns 	= ['campaign', 'payment_country', 'region', 'tenure', 'metric', 'result']
finance_columns 	= ['finance_measure','formula','result']

def set_scope():
	scope = SimpleNamespace( 

								nrows 				= None,

								campaign_previous	= 2021,
								campaign_retained	= 2020,

								show_regions		= True,
								save_rates			= True,

								target_app_rates_df = pd.DataFrame( columns=target_app_columns),
								finance_rates_df 	= pd.DataFrame( columns=finance_columns),
								)
	

	scope_paths(scope)


	return scope