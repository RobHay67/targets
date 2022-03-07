
# we need to store these as a file in the project directory
import pandas as pd
import os
# import pathlib


from config.model.countries import country_dict



def scope_forex_rates(scope):

	current_campaign = scope.campaign
	campaign_forex_rates = scope.forex_df.loc[scope.forex_df['campaign'] == current_campaign]
	

	forex_rates = {}

	for country_code in country_dict.keys():
		if country_code != 'all':
			forex_rates[country_code] = {}

			# set rates for the country / campaign combination (zero if rates are missing)
			if campaign_forex_rates.empty:
				sub_rate = 0.0
				aud_rate = 0.0
			else:
				country_forex_rates = campaign_forex_rates.loc[campaign_forex_rates['country'] == country_code]
				sub_rate = float(country_forex_rates['forex_to_sub'])
				aud_rate = float(country_forex_rates['forex_to_aud'])
			
			forex_rates[country_code]['sub'] = sub_rate
			forex_rates[country_code]['aud'] = aud_rate

	scope.forex_rates = forex_rates






def load_forex_rates(scope):

	if os.path.exists( scope.path_forex_file ):

		forex_table = pd.read_csv( scope.path_forex_file, 
									dtype={'campaign':'int', 'country':'str', 'forex_to_sub':'float64', 'forex_to_aud':'float64'},
									# parse_dates=csv_dates(schema),
									)

		# ticker_index.set_index('share_code', inplace=True)

		scope.forex_df = forex_table

		scope.loaded_forex_table = True

	else: 

		forex_table = pd.DataFrame(columns=['campaign', 'country', 'forex_to_sub', 'forex_to_aud'])

		scope.forex_df = forex_table
		












