import pandas as pd
import os


from config.model.folders import set_path_to_target_file
from config.model.regions import set_regions_for_country

from targets.model.rates_for_view import target_rates_for_view


def scope_target(scope):

	scope.target_setting_method = 'Country'
	# scope.target_refresh_widgets = True

	# Establish the regions for the default country / tenure
	set_regions_for_country(scope)

	

def load_target_rates(scope):

	set_path_to_target_file(scope)

	if os.path.exists( scope.path_target_file ):

		taget_table = pd.read_csv( scope.path_target_file, 
									dtype={'campaign':'int', 'payment_country':'str', 'region':'str', 'tenure':'str', 'metric':'str', 'value':'float64'},
									# parse_dates=csv_dates(schema),
									index_col=None,

									)

		# ticker_index.set_index('share_code', inplace=True)

		scope.target_df = taget_table

		scope.loaded_target_table = True

	else: 

		taget_table = pd.DataFrame(columns=['campaign', 'payment_country', 'region', 'tenure', 'metric', 'value'])

		scope.target_df = taget_table
		

	# establish a default set of target rates to display in the browser

	target_rates_for_view(scope)






