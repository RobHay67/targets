


def print_report_header(scope):

	for i in range(10):
		print('')
	print('='*100)
	print('Target Setting for ' + str( scope.campaign_previous+1) + ' campaign.')
	print('-'*100)
	print('rates based on the ' + str( scope.campaign_previous)   + ' campaign.')
	print('retention from the ' + str( scope.campaign_retained)   + ' campaign.')
	print('='*100)



def print_section_title( description ):
	print ( '-'*130)
	print ( description )
	print ( '-'*130)




def add_measure_to_rates_df( rates_df, country, region, tenure, metric, result, measure, formula='' ):
	
	campaign =  2021
	finance_measure = country.upper()+'-'+measure
	tab1 = 75
	tab2 = 40
	
	print ( finance_measure.ljust(tab1), str( formula ).rjust(tab2), str( result ) )
		
	rates_df = rates_df.append( {'campaign':campaign, 'payment_country':country, 'region':region, 'tenure':tenure, 'metric':metric, 'result':result, 'formula':formula, 'finance_measure':finance_measure }, ignore_index=True)  
	
	return rates_df


rates_df_columns = ['campaign', 'payment_country', 'region', 'tenure',  'metric', 'result', 'formula', 'finance_measure']



def print_country(country):
	print ( '='*130)
	print ( country.upper() )
	print ( '='*130)