# activate Pipenv 	- pipenv shell
# python rates.py	- python rates.py

# Transfer Jupyter Notebook code to live alongside our Target Setting Code


# TODO - see if we can generate both the finance and target rate files at the same time


import pandas as pd
import numpy as np


from rate_code.scope import set_scope
from rate_code.states import country_region_config
from rate_code.load_data import load_customer_dataframe
from rate_code.report import print_report_header, print_country
from rate_code.rates import store_movember_rates

scope = set_scope()
# print(scope)





print_report_header(scope)

# -------------------------------------
# Load Dataframes
# -------------------------------------
frs_current  = load_customer_dataframe( scope, 'Customers', scope.campaign_previous, scope.nrows )
dnt_current  = load_customer_dataframe( scope, 'Donations', scope.campaign_previous, scope.nrows )
frs_previous = load_customer_dataframe( scope, 'Customers', scope.campaign_retained, scope.nrows )


# Create an Empty Rates Df






# TODO Country Lists for testing purposes
country_list  = [ 'au', 'ca', 'gb', 'us', 'ie', 'nz', 'at', 'be', 'cz', 'dk', 'fi', 'fr', 'de', 'it', 'nl', 'no', 'es', 'se', 'ch', 'hk', 'ex', 'sg', 'za' ]
# country_list  = [ 'au', 'ca', 'at' ]
# country_list  = [ 'us' ]




# Primary Controller - iterate through Countries and then regions and generate the appropriate information

for country in country_list:
	print_country(country)
	scope.country = country
	scope.region = 'Total'
	
	# Subset Customer Dataframes for each Country
	country_frs_current  = frs_current[frs_current['payment_country'] == country].copy()
	country_dnt_current  = dnt_current[dnt_current['payment_country'] == country].copy()
	country_frs_previous  = frs_previous[frs_previous['payment_country'] == country].copy()
	
	# Store for use by store_movember_rates (Regions will override this)
	scope.country_frs_current  = country_frs_current
	scope.country_dnt_current  = country_dnt_current
	scope.country_frs_previous  = country_frs_previous

	store_movember_rates(scope)

		
	country_regions = list(country_region_config[country]['regions'])

	if 'Other' in country_regions:
		scope.region = 'Other'
		# We only have a single region so add the totals again, but with a region of other
		store_movember_rates(scope)
	else:
		# We have multiple regions so we need a region subset of data to pass to the report constructor
		
		# Create a general purpose region field for subsetting - ie Australia migth = state wheras canada = province
		region_field = country_region_config[country]['region_field']
		country_frs_current['region'] = np.where( country_frs_current[region_field].isin(country_regions),  country_frs_current[region_field], 'Other' )
		country_dnt_current['region'] = np.where( country_dnt_current[region_field].isin(country_regions),  country_dnt_current[region_field], 'Other' )
		country_frs_previous['region']= np.where( country_frs_previous[region_field].isin(country_regions), country_frs_previous[region_field], 'Other' )
		
		# Add Other to our country_regions list so we get all data by region - everyone has an other
		country_regions.append('Other')

		for region in country_regions:
			scope.region = region

			scope.country_frs_current  = country_frs_current[country_frs_current['region']   == region].copy()
			scope.country_dnt_current  = country_dnt_current[country_dnt_current['region']   == region].copy()
			scope.country_frs_previous = country_frs_previous[country_frs_previous['region'] == region].copy()
			
			store_movember_rates(scope)

	if scope.save_rates:
		scope.target_app_rates_df.to_csv(scope.path_target_rates, index=False)
		scope.finance_rates_df.to_csv(scope.path_finance_rates, index=False)



	print('='*100)

