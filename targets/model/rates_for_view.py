from config.model.countries import country_dict


from config.model.tenure import tenure_levels
from config.model.countries import country_key_from_name


def target_rates_for_view(scope):

	payment_country = country_key_from_name(scope.target_selected_country)
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
	print( '\033[91mfilter to the region in the loop so we get the correct rate\033[0m' )
	for region in scope.target_regions:
		
		if region != 'row_heading':

			# Filter for Region
			base_df_for_region = base_df[base_df['region'] == region]
			target_df_for_region = target_df[target_df['region'] == region]
			

			base_rates[region] = {}
			target_rates[region] = {}

			for metric in tenure_metrics:

				# Base Rates (last Campaign)
				if metric in base_df_for_region.index:
					base_result = base_df_for_region.loc[metric].at['result']
				else:
					base_result = 0.0

				base_rates[region][metric] = base_result

				# Target Rates (Current Campaign)
				print(target_df_for_region)
				if metric in target_df_for_region.index:
					target_result = target_df_for_region.loc[metric].at['result']
				else:
					target_result = 0.0
				
				target_rates[region][metric] = target_result


	scope.target_base_rates = base_rates
	scope.target_rates = target_rates

				

