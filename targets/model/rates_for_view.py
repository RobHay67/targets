from config.model.countries import country_dict


from config.model.tenure import tenure_levels
from config.model.countries import country_key_from_name



def market_total(scope, tenure, metric):
	
	market_total = 0.0
	
	payment_country = country_key_from_name(scope.user_selected_country)

	target_df = scope.target_df[scope.target_df['payment_country'] == payment_country].copy()

	# if metric != 'regos_campaign_one_ago':
	if metric != 'regos_total_prior':
		target_df = target_df[target_df['campaign'] == int(scope.campaign)].copy()
	else:
		target_df = target_df[target_df['campaign'] == int(scope.campaign-1)].copy()	

	target_df = target_df[target_df['region'] == 'Total']
	# Exclude comments from target_df
	target_df = target_df[target_df['metric'] != 'comment']
	target_df['result'] = target_df['result'].astype(float)

	

	if tenure == 'p2p':
		target_df = target_df[target_df['tenure'] != 'Foundation']
		target_df = target_df[target_df['metric'] == metric]
		market_total = sum(target_df['result'])
	elif tenure == 'Total':
		target_df = target_df[target_df['metric'] == metric]
		market_total = sum(target_df['result'])
	else:
		target_df = target_df[target_df['tenure'] == tenure]
		target_df.set_index('metric', inplace = True)
		if metric in target_df.index:
			market_total = target_df.loc[metric].at['result']

	return market_total

def active_rate(scope, tenure):

	active_rate = 0.0
	total_regos =  market_total(scope, tenure, 'regos')
	total_active =  market_total(scope, tenure, 'active')
	
	if total_regos > 0:active_rate = total_active / total_regos

	return active_rate

def retention_rate(scope, tenure):
	# AKA : Retention Ratio

	retention_ratio = 0.0

	total_regos =  market_total(scope, tenure, 'regos')
	print('retention_rate > total_regos = ', total_regos)
	last_years_campaign_regos = market_total(scope, tenure, 'regos_total_prior')
	
	if last_years_campaign_regos > 0:
		retention_ratio = total_regos / last_years_campaign_regos

	return retention_ratio

def target_rates_for_view(scope):

	payment_country = country_key_from_name(scope.user_selected_country)
	tenure_metrics = tenure_levels[scope.target_selected_tenure]
	campaign_year_base   = int(scope.campaign) - 1			# last years rates
	campaign_year_target = int(scope.campaign)				# target year (this year)
	
	# Filter target rates to make it easier to find the values
	target_df = scope.target_df[scope.target_df['payment_country'] == payment_country].copy()
	target_df = target_df[target_df['tenure'] == scope.target_selected_tenure]

	# Filter for the relevant campaign year (Base is going to be the previous 1 campaign)
	base_df   = target_df[target_df['campaign'] == campaign_year_base]
	base_df.set_index('metric', inplace = True)
	target_df = target_df[target_df['campaign'] == campaign_year_target]
	target_df.set_index('metric', inplace = True)

	# Create dictionaries to store the relevant rates
	base_rates = {}
	target_rates = {}

	# Iterate through each region and extract the appropriate rates
	for region in scope.target_columns:

		if region != 'row_heading':

			# Filter for Region
			base_df_for_region = base_df[base_df['region'] == region]
			target_df_for_region = target_df[target_df['region'] == region]
			
			base_rates[region] = {}
			target_rates[region] = {}

			for metric in tenure_metrics:
				default_value = float(0.0) if metric != 'comment' else ''

				# Base Rates (last Campaign)
				if metric in base_df_for_region.index:
					base_result = base_df_for_region.loc[metric].at['result']
				else:
					base_result = default_value

				base_result = format_metrics(scope, metric, base_result)
				base_rates[region][metric] = base_result

				# Target Rates (Current Campaign)
				if metric in target_df_for_region.index:
					target_result = target_df_for_region.loc[metric].at['result']
					
				else:
					target_result = default_value
				
				target_result = format_metrics(scope, metric, target_result)
				target_rates[region][metric] = target_result


	scope.target_base_rates = base_rates
	scope.target_rates = target_rates

				

def format_metrics(scope, metric, value):
	expected_format = scope.metrics[metric]

	# print( metric, ' = ', value, ' > ', type(value), value!= value)

	# if value == nan:
	if metric == 'comment' and value != value: # last but is check if its a nan
		# print('changing the value')
		value = ''

	formatted_value = expected_format(value)
	
	return formatted_value






