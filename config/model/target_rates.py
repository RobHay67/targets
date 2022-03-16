import pandas as pd
import os


from config.model.folders import set_path_to_target_file


from config.model.countries import country_dict



def scope_target_rates(scope):

	#TODO - we need to configure this one rob
	print('TODO - scope_target_rates')

	# current_campaign = scope.campaign
	# campaign_forex_rates = scope.forex_df.loc[scope.forex_df['campaign'] == current_campaign]
	

	# forex_rates = {}

	# for country_code in country_dict.keys():
	# 	if country_code != 'all':
	# 		forex_rates[country_code] = {}

	# 		# set rates for the country / campaign combination (zero if rates are missing)
	# 		if campaign_forex_rates.empty:
	# 			sub_rate = 0.0
	# 			aud_rate = 0.0
	# 		else:
	# 			country_forex_rates = campaign_forex_rates.loc[campaign_forex_rates['country'] == country_code]
	# 			sub_rate = float(country_forex_rates['forex_to_sub'])
	# 			aud_rate = float(country_forex_rates['forex_to_aud'])
			
	# 		forex_rates[country_code]['sub'] = sub_rate
	# 		forex_rates[country_code]['aud'] = aud_rate

	# scope.forex_rates = forex_rates






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
		












