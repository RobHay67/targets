

from config.model.countries import region_dict, country_key_from_name



def set_regions_for_country(scope):

	# Add a default value at position 0 to be used as a row heading where necessary
	regions = []
	target_cols = ['row_heading']
	
	
	# generate a list of regions for this payment_country
	payment_country = country_key_from_name(scope.user_selected_country)

	if payment_country in region_dict.keys():
		regions += region_dict[payment_country]
		target_cols += region_dict[payment_country]

	# Add a Total column at the end of the list (we can target set at this level as well)
	target_cols += ['Total']
	
	
	scope.target_regions = regions
	scope.target_columns = target_cols





# if region not in ['row_heading', 'Total']