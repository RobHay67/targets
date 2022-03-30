



def forex_rates_for_view(scope):

	# Create a dicitonary of the selected forex campaign and store the rates in this
	# so that they can be edited by the appropriate widget

	current_campaign = scope.campaign_forex
	campaign_forex_rates = scope.forex_df.loc[scope.forex_df['campaign'] == current_campaign]
	
	forex_rates = {}

	for country_code in scope.country_code_list:
		if country_code != 'all':
			forex_rates[country_code] = {}

			# set rates for the country / campaign combination (zero if rates are missing)
			if campaign_forex_rates.empty:
				sub_rate = 0.0
				aud_rate = 0.0
			else:
				country_forex_rates_df = campaign_forex_rates.loc[campaign_forex_rates['country'] == country_code]
				sub_rate = float(country_forex_rates_df['forex_to_sub'])
				aud_rate = float(country_forex_rates_df['forex_to_aud'])
			
			forex_rates[country_code]['sub'] = sub_rate
			forex_rates[country_code]['aud'] = aud_rate

	scope.forex_rates_for_view = forex_rates



