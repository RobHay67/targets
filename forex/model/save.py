import pandas as pd

from config.model.forex_rates import scope_forex_rates


def save_forex_rates(scope):

	# convert our forex rate dictionary into a pandas dataframe
	forex_table_edited = pd.DataFrame(columns=['campaign', 'country', 'forex_to_sub', 'forex_to_aud'])
	campaign = scope.campaign_forex

	for country, row in scope.forex_rates_maintenance.items():
		new_row = {'campaign':campaign, 'country':country, 'forex_to_sub':row['sub'], 'forex_to_aud':row['aud']}
		forex_table_edited = forex_table_edited.append(new_row, ignore_index=True)

	# so now we remove the old forex rates 
	scope.forex_df = scope.forex_df[scope.forex_df['campaign'] != campaign].copy()

	# and add the latest forex rates back into the df
	scope.forex_df = scope.forex_df.append(forex_table_edited)

	# refresh the application forex rates (in case we updated the current campaign)
	scope_forex_rates(scope)

	# TODO Recalculate forex values???

	saving_df = scope.forex_df.copy()

	saving_df.to_csv( scope.path_forex_file, index=False )





