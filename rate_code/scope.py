

from types import SimpleNamespace
from rate_code.load_data import scope_paths



def set_scope():
	scope = SimpleNamespace( 
								rates_df_columns = ['campaign', 'payment_country', 'region', 'tenure',  'metric', 'result', 'formula', 'finance_measure'],
								
								nrows 				= 200,
								campaign_previous	= 2021,
								campaign_retained	= 2020,
								show_regions		= False,
								save_for_finance	= False,
								save_for_target_app = True,
								)
	
	if scope.save_for_finance == True:
		scope.finance_description = True,
		scope.save_for_target_app = False	
	else:
		scope.finance_description = False,

	scope_paths(scope)


	return scope