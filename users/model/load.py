
import pandas as pd
import os


def load_user_table(scope):


	if os.path.exists( scope.path_user_file ):
		user_table = pd.read_csv( scope.path_user_file, 
									dtype={	
											'name':'str', 
											'pword':'str',
											'country_codes':'str',
											'can_edit_targets':'boolean', 
											'can_see_total_movember':'boolean', 
											'can_edit_forex_rates':'boolean',
											'can_edit_previous_rates':'boolean', 
											'can_edit_config':'boolean',
											'can_edit_users':'boolean',
											'can_download_rates_table':'boolean',
											'selected_country':'str',
											'target_setting_method':'str',
											 },
									index_col=None,
									)
		
		user_table.set_index('name', inplace=True)


	else: 
		user_table = pd.DataFrame(columns=[	
											'name', 
											'pword', 
											'country_codes', 
											'can_edit_targets', 
											'can_see_total_movember', 
											'can_edit_forex_rates',
											'can_edit_previous_rates',
											'can_edit_config', 
											'can_edit_users', 
											'can_download_rates_table',
											'selected_country', 
											'target_setting_method'
											  ])




	scope.user_df = user_table

		


