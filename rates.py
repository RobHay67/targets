# activate Pipenv 	- pipenv shell
# python rates.py	- python rates.py

# Transfer Jupyter Notebook code to live alongside our Target Setting Code



from inspect import formatannotationrelativeto
import pandas as pd
import numpy as np

import itertools   # for building a matrix of possible combinations


from rate_code.params import set_params

from rate_code.states import country_region_config
from rate_code.load_data import load_customer_dataframe

from rate_code.report import print_country
from rate_code.rates import movember_rates

#============================================================================= Default Params - should onl be campaign year (List= single or multiple vals)
tab = 15
#----------------------------------------------------------------------------- Default Paths

# fundraiser_columns = ['payment_country', 'member_id', 'feat_new', 'feat_return_retained', 'type_foundation', 'fundraising_category', 'value_lcl_total_donations', 'feat_active' ]
# donation_columns   = ['payment_country', 'member_id', 'feat_new', 'feat_return_retained', 'type_foundation', 'fundraising_category', 'value_lcl_total_donations' ]
# rates_df_columns = ['campaign', 'payment_country', 'region', 'tenure',  'metric', 'result', 'formula', 'finance_measure']



params = set_params()

print(params)


# -------------------------------------
# Run Variables
# -------------------------------------
# finance_description = False
# nrows 				= 1000
# campaign 			= 2021

# -------------------------------------
# Load Dataframes
# -------------------------------------
fundraisers_2021 = load_customer_dataframe( 'Customers', 2021, params.nrows )
fundraisers_2020 = load_customer_dataframe( 'Customers', 2020, params.nrows )
donations_2021   = load_customer_dataframe( 'Donations'  , 2021, params.nrows )


# Set for 2022 Campaign Forecast
frs_current  = fundraisers_2021.copy()
dnt_current    = donations_2021.copy()
frs_previous  = fundraisers_2020.copy()





# Create an Empty Rates Df
rates_df = pd.DataFrame( columns=params.rates_df_columns)

# TODO Country Lists for testing purposes
country_list  = [ 'au', 'ca', 'gb', 'us', 'ie', 'nz', 'at', 'be', 'cz', 'dk', 'fi', 'fr', 'de', 'it', 'nl', 'no', 'es', 'se', 'ch', 'hk', 'ex', 'sg', 'za' ]
# country_list  = [ 'au', 'ca', 'at' ]


for country in country_list:
    print_country(country)
    
    # Subset for Country
    country_frs_current  = frs_current[(frs_current['customer_type'] == 'fundraiser')        & (frs_current['payment_country'] == country)].copy()
#     country_frs_current  = frs_current[(frs_current['target_customers'] == 1)        & (frs_current['payment_country'] == country)].copy()
#     country_frs_previous = frs_previous[(frs_previous['target_customers'] == 1)      & (frs_previous['payment_country'] == country)].copy()
    country_frs_previous = frs_previous[(frs_previous['customer_type'] == 'fundraiser')      & (frs_previous['payment_country'] == country)].copy()
    country_dnt_current  = dnt_current[(dnt_current['donation_type'] == 'donate_to_charity') & (dnt_current['payment_country'] == country)].copy()
    country_regos_current  = len( country_frs_current)
    country_funds_current  = country_frs_current['lcl_fundr_total'].sum()
    country_regos_previous = len( country_frs_previous)
    
    rates_df = movember_rates(params, rates_df, country, 'Total', country_frs_current, country_dnt_current, country_regos_current, country_regos_previous, country_funds_current)
 
    # Iterate Through the Regions Now
    country_regions = list(country_region_config[country]['regions'])
#     print(country_regions)
    
    if 'Other' in country_regions:
        # We only have a single region so add the totals again, but with a region of other
        print('Only 1 Region - this is working fine')
        rates_df = movember_rates(rates_df, country, 'Other', country_frs_current, country_dnt_current, country_regos_current, country_regos_previous, country_funds_current)
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
#             print(region)
            region_frs_current  = country_frs_current[country_frs_current['region']   == region].copy()
            region_frs_previous = country_frs_previous[country_frs_previous['region'] == region].copy()
            region_dnt_current  = country_dnt_current[country_dnt_current['region']   == region].copy()
            region_regos_current  = len( region_frs_current)
            region_funds_current  = region_frs_current['lcl_fundr_total'].sum()
            region_regos_previous = len( region_frs_previous)
    
            rates_df = movember_rates(rates_df, country, region, region_frs_current, region_dnt_current, region_regos_current, region_regos_previous, region_funds_current)
           












