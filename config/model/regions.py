

from config.model.countries import country_key_from_name


def set_regions_for_country(scope):

	# Add a default value at position 0 to be used as a row heading where necessary
	target_regions = []
	target_columns = ['row_heading']
	
	
	# generate a list of regions for this payment_country
	payment_country = country_key_from_name(scope.user_selected_country)

	region_df = scope.target_df.copy()

	region_df = region_df[region_df['payment_country'] == payment_country]

	region_list = list(region_df['region'].unique())
	
	# Remove any total - it may not be in the correct order and we need it last in the list
	if 'Total' in region_list: region_list.remove('Total')
	if 'total' in region_list: region_list.remove('total')

	target_columns += region_list
	target_columns += ['Total']


	target_regions = region_list	
	
	scope.target_regions = target_regions
	scope.target_columns = target_columns
