
from pickle import TRUE
import pandas as pd
import numpy as np

from config.model.forex_rates import scope_forex_rates


def save_forex_rates(scope):

	# convert our forex rate dictionary into a pandas dataframe
	forex_table_edited = pd.DataFrame(columns=['campaign', 'country', 'forex_to_sub', 'forex_to_aud'])
	campaign = scope.campaign_forex
	print(campaign)

	for country, row in scope.forex_rates_maintenance.items():
		new_row = {'campaign':campaign, 'country':country, 'forex_to_sub':row['sub'], 'forex_to_aud':row['aud']}
		forex_table_edited = forex_table_edited.append(new_row, ignore_index=True)

	# so now we remove the old forex rates 
	print( 'DELETING where campaing ==', campaign)
	# scope.forex_df = scope.forex_df.drop(scope.forex_df[scope.forex_df['campaign'] == campaign])
	
	
	print('='*88, ' before editing')
	print (scope.forex_df)
	# scope.forex_df = scope.forex_df.drop(scope.forex_df[scope.forex_df['campaign'] == campaign].index, inplace = True)
	scope.forex_df = scope.forex_df[scope.forex_df['campaign'] != campaign].copy()

	print('='*88, ' after removing')
	print (scope.forex_df)
	print('='*88, ' fin')

	print('='*88, ' new Data to be appended')
	print(forex_table_edited)
	

	# and add the latest forex rates back into the df
	scope.forex_df = scope.forex_df.append(forex_table_edited)

	print('='*88, ' after appending')
	print(scope.forex_df)

	# refresh the application forex rates
	scope_forex_rates(scope)

	# TODO Recalculate forex values???

	saving_df = scope.forex_df.copy()

	saving_df.to_csv( scope.path_forex_file, index=False )



