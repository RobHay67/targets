

from config.model.countries import region_dict, country_key_from_name



def set_regions_for_country(scope):

	regions = []

	payment_country = country_key_from_name(scope.target_selected_country)
	
	# generate a list of regions for this payment_country
	if payment_country in region_dict.keys():
		regions += region_dict[payment_country]

	regions += ['TOTAL']
	
	scope.target_regions = regions


