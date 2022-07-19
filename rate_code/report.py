
tab1 = 75
tab2 = 40


def print_report_header(scope):

	for i in range(10):
		print('')
	print('='*100)
	print('Target Setting for ' + str( scope.campaign_previous+1) + ' campaign.')
	print('-'*100)
	print('rates based on the ' + str( scope.campaign_previous)   + ' campaign.')
	print('retention from the ' + str( scope.campaign_retained)   + ' campaign.')
	print('rows limit = ', scope.nrows)
	print('='*100)



def print_section_title( scope, description ):

	description = description + ' - ' + scope.country + ' - region = ' + scope.region

	print ( '-'*130)
	print ( description )
	print ( '-'*130)


def add_measure(scope, metric, result, measure, finance_desc=None, formula=None):

	# Ensure we have values for all strings
	if finance_desc==None: finance_desc = measure
	if formula == None: formula=''

	if metric != 'comment': # ignore the comments, they are always empty
		
		line_colour = '\033[0m' if scope.region != 'Total' else '\033[96m'

		print ( (line_colour+ measure).ljust(tab1)		, str( formula ).rjust(tab2), str( result ), '\033[0m' )
		# print ( finance_desc.ljust(tab1), str( formula ).rjust(tab2), str( result ) ) # TODO - just to show the differences

	if metric != 'ignore':
		scope.target_app_rates_df = scope.target_app_rates_df.append( 
										{	
											'campaign':scope.campaign_previous, 
											'payment_country':scope.country, 
											'region':scope.region, 
											'tenure':scope.tenure, 
											'metric':metric, 
											'result':result, 
										}, ignore_index=True)  


	if scope.region == 'Total' and metric != 'comment':
		# We only want the Totals and ignore any comments rows
		finance_measure = scope.country.upper()+'-'+finance_desc

		scope.finance_rates_df = scope.finance_rates_df.append( 
										{
											'finance_measure':finance_measure,
											'formula':formula, 
											'result':result, 						 
										}, ignore_index=True) 




def print_country(country):
	print ( '='*130)
	print ( country.upper() )
	print ( '='*130)


# -----------------------------------------------------------------------------------------------------------------------------------
# Colours
# -----------------------------------------------------------------------------------------------------------------------------------
red         = '\033[91m'
green       = '\033[92m'
yellow      = '\033[93m'
blue        = '\033[94m'
purple      = '\033[95m'
cyan        = '\033[96m'
white 		= '\033[0m'

# Finance Rates Sample
# 	finance_measure	formula	result
# 0	AU-NEW - No of New Fundraisers (previous campa...		48534
# 1	AU-NEW - No of Active Fundraisers		26082
# 2	AU-NEW - APAM (Active)	26082 / 11204473.58 =	429.59
# 3	AU-NEW - Total Funds		11,204,473.58
# 4	AU-NEW - Active Ratio	26082 / 48534 =	0.54
# 6	AU-RETAINED - No of Fundraisers (previous camp...		90922
# 7	AU-RETAINED - Total Retained from Previous int...		17496
# 8	AU-RETAINED - No of Active Fundraisers		11487
# 9	AU-RETAINED - APAM (Active)	6902602.73 / 11487 =	600.91
# 10	AU-RETAINED - Total Funds		6,902,602.73


# Target App Rates - Sample

# 	campaign	payment_country	region	tenure	metric	result
# 0	2021	au	Total	New	regos	48633
# 1	2021	au	Total	New	active	26007
# 2	2021	au	Total	New	apam	434.12
# 3	2021	au	Total	New	funds	11,290,177.15
# 5	2021	au	Total	New	comment	
# 6	2021	au	Total	Retained	regos_total_prior	90922
# 7	2021	au	Total	Retained	regos	17489
# 8	2021	au	Total	Retained	active	11471
# 9	2021	au	Total	Retained	apam	600.32
# 10 2021	au	Total	Retained	funds	6,886,251.96




