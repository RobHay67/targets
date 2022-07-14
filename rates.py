# activate Pipenv 	- pipenv shell
# python rates.py	- python rates.py

# Transfer Jupyter Notebook code to live alongside our Target Setting Code


from inspect import formatannotationrelativeto
import pandas as pd
import numpy as np


from rate_code.scope import set_scope
from rate_code.states import country_region_config
from rate_code.load_data import load_customer_dataframe
from rate_code.report import print_report_header, print_country
from rate_code.rates import movember_rates

scope = set_scope()

print_report_header(scope)

# -------------------------------------
# Load Dataframes
# -------------------------------------
frs_current  = load_customer_dataframe( scope, 'Customers', scope.campaign_previous, scope.nrows )
dnt_current  = load_customer_dataframe( scope, 'Donations', scope.campaign_previous, scope.nrows )
frs_previous = load_customer_dataframe( scope, 'Customers', scope.campaign_retained, scope.nrows )


# Create an Empty Rates Df
rates_df = pd.DataFrame( columns=scope.rates_df_columns)

# TODO Country Lists for testing purposes
# country_list  = [ 'au', 'ca', 'gb', 'us', 'ie', 'nz', 'at', 'be', 'cz', 'dk', 'fi', 'fr', 'de', 'it', 'nl', 'no', 'es', 'se', 'ch', 'hk', 'ex', 'sg', 'za' ]
country_list  = [ 'au', 'ca', 'at' ]
# country_list  = [ 'au' ]

for country in country_list:
	print_country(country)
	
	# Subset Customer Dataframes for each Country
	country_frs_current  = frs_current[frs_current['payment_country'] == country].copy()
	country_dnt_current  = dnt_current[dnt_current['payment_country'] == country].copy()
	country_frs_previous  = frs_previous[frs_previous['payment_country'] == country].copy()

	rates_df = movember_rates(scope, rates_df, country, 'Total', country_frs_current, country_dnt_current, country_frs_previous)

	# Iterate Through the Regions Now
	country_regions = list(country_region_config[country]['regions'])
	

	if scope.show_regions:

		if 'Other' in country_regions:
			# We only have a single region so add the totals again, but with a region of other
			rates_df = movember_rates(scope, rates_df, country, 'Other', country_frs_current, country_dnt_current, country_frs_previous)
		else:
			# We have multiple regions so we need a region subset of data to pass to report constructort
			
			# Create a general purpose region field for subsetting
			region_field = country_region_config[country]['region_field']
			country_frs_current['region'] = np.where( country_frs_current[region_field].isin(country_regions), country_frs_current[region_field], 'Other' )
			country_frs_previous['region']= np.where( country_frs_previous[region_field].isin(country_regions), country_frs_previous[region_field], 'Other' )
			country_dnt_current['region'] = np.where( country_dnt_current[region_field].isin(country_regions), country_dnt_current[region_field], 'Other' )
			
			# Add Other to our country list so we get all data by region
			country_regions.append('Other')

			for region in country_regions:
				region_frs_current  = country_frs_current[country_frs_current['region']   == region].copy()
				region_frs_previous = country_frs_previous[country_frs_previous['region'] == region].copy()
				region_dnt_current  = country_dnt_current[country_dnt_current['region']   == region].copy()
				
				rates_df = movember_rates(scope, rates_df, country, region, region_frs_current, region_dnt_current, region_frs_previous)


	if scope.save_for_target_app:
		print('save_for_target_app')
		target_rates = rates_df[rates_df['metric'] != 'ignore'].copy()
		target_rates = target_rates[['campaign', 'payment_country', 'region', 'tenure', 'metric', 'result']]
		target_rates.to_csv(scope.path_target_rates, index=False)

	
	if scope.save_for_finance:
		print('save_for_finance')
		finance_rates = rates_df[rates_df['region'] == 'Total'].copy()
		finance_rates = finance_rates[finance_rates['metric'] != 'comment']
		finance_rates = finance_rates[['finance_measure','formula','result']]
		finance_rates.to_csv(scope.path_finance_rates, index=False)








