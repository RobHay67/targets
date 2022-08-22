

from types import SimpleNamespace
import pandas as pd
from rate_code.load_data import scope_paths


target_app_columns 	= ['campaign', 'payment_country', 'region', 'tenure', 'metric', 'result']
finance_columns 	= ['finance_measure','formula','result']


target_campaign = 2018



def set_scope():
	scope = SimpleNamespace( 

								nrows 				= None,

								campaign_previous	= target_campaign - 1,
								campaign_retained	= target_campaign - 2,
								# campaign_previous	= 2018,
								# campaign_retained	= 2017,

								show_regions		= False,
								save_rates			= True,
								show_community		= False,

								target_app_rates_df = pd.DataFrame( columns=target_app_columns),
								finance_rates_df 	= pd.DataFrame( columns=finance_columns),
								)
	

	scope_paths(scope)


	return scope