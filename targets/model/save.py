import pandas as pd
import numpy as np

from forex.model.rates_for_view import forex_rates_for_view
from config.model.countries import country_key_from_name
from config.model.tenure import tenure_levels


def save_target_rates(scope):
	
	campaign = scope.campaign
	payment_country = country_key_from_name(scope.target_selected_country)
	tenure_group = scope.target_selected_tenure
	tenure_metrics = tenure_levels[scope.target_selected_tenure]

	# convert our target rate dictionary into a pandas dataframe
	target_table_edited = pd.DataFrame(columns=['campaign', 'payment_country', 'region', 'tenure', 'metric', 'result'])

	for region, row in scope.target_rates.items():
		# print(region, row)
		if region != 'row_heading':
			for metric in tenure_metrics:
				new_row = {'campaign':campaign, 'payment_country':payment_country, 'region':region, 'tenure':tenure_group, 'metric':metric, 'result':row[metric]}
				target_table_edited = target_table_edited.append(new_row, ignore_index=True)
		
	# print('new rows = ', len(target_table_edited))
	# print(target_table_edited)


	# tag rows to remove - combination of Campaign, Country and Tenure Level
	target_df = scope.target_df.copy()
	# print('size of the target_df originally', len(target_df))
	target_df['delete'] = np.where((target_df['campaign'] == campaign) & ( target_df['payment_country'] == payment_country ) & ( target_df['tenure'] == tenure_group ), 1, 0)
	target_df = target_df[target_df['delete'] == 0].copy()
	target_df.drop(columns=['delete'], inplace=True)

	# print('size of the target_df after deleting duplicate rows', len(target_df))

	# and add the latest tenure target rates back into the target_df
	scope.target_df = target_df.append(target_table_edited)

	# print('size of the target_df after appending our new rows', len(scope.target_df))
	# print(scope.target_df.tail(20))

	# # refresh the application forex rates (in case we updated the current campaign)
	# forex_rates_for_view(scope)

	# TODO Recalculate forex values???
	print( '\033[91mTODO Recalculate Forex Values < save_target_rates > \033[0m' )

	# Save the rates File
	# saving_df = scope.target_df.copy()

	# saving_df.to_csv( scope.path_target_file, index=False )






