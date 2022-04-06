import streamlit as st

from config.model.tenure import tenure_levels
from targets.model.widget_key import create_widget_key
from targets.model.save import save_target_rates




def store_changed_value_in_target_rates(scope, region, metric, changed_value):	
	scope.target_rates[region][metric] = changed_value


def on_change_regos(scope:dict, region:str):	
	
	metric = 'regos'
	changed_value = scope[create_widget_key(scope, region, metric)]

	store_changed_value_in_target_rates(scope, region, metric, changed_value)

	if region == 'Total':
		allocate_total_to_regions(metric)  # TODO - Rob needs to work on this one
	else:
		calc_total_for_metric(scope, metric)

	save_target_rates(scope)

def on_change_active_regos(scope:dict, region:str):	
	
	metric = 'active'
	changed_value = scope[create_widget_key(scope, region, metric)]

	store_changed_value_in_target_rates(scope, region, metric, changed_value)

	if region == 'Total':
		allocate_total_to_regions(metric)  # TODO - Rob needs to work on this one
	else:
		calc_total_for_metric(scope, metric)
		calc_funds_raised(scope, region)
		calc_total_for_metric(scope, 'funds')


	save_target_rates(scope)

def on_change_apam(scope:dict, region:str):	
	print ('APAM has changed')

	metric = 'apam'
	changed_value = scope[create_widget_key(scope, region, metric)]

	store_changed_value_in_target_rates(scope, region, metric, changed_value)

	if region == 'Total':
		allocate_total_to_regions(metric)  # TODO - Rob needs to work on this one
	else:
		calc_funds_raised(scope, region)
		calc_total_for_metric(scope, 'funds')
		calc_total_for_apam(scope, region)

	save_target_rates(scope)

def on_change_funds(scope:dict, region:str):

	metric = 'funds'
	changed_value = scope[create_widget_key(scope, region, metric)]

	store_changed_value_in_target_rates(scope, region, metric, changed_value)

	if region == 'Total':
		allocate_total_to_regions(metric)  # TODO - Rob needs to work on this one
	else:
		calc_total_for_metric(scope, metric)

		if scope.target_selected_tenure == 'Foundation':
			calc_ada(scope, region)
			calc_total_for_ada(scope, region)
		else:
			calc_apam(scope, region)
			calc_total_for_apam(scope, region)

	save_target_rates(scope)

def on_change_donations(scope:dict, region:str):	
	
	metric = 'donations'
	changed_value = scope[create_widget_key(scope, region, metric)]

	store_changed_value_in_target_rates(scope, region, metric, changed_value)

	if region == 'Total':
		allocate_total_to_regions(metric)  # TODO - Rob needs to work on this one
	else:
		calc_total_for_metric(scope, metric)

	save_target_rates(scope)

def on_change_ada(scope:dict, region:str):	
	print ('ADA has changed')

	metric = 'ada'
	changed_value = scope[create_widget_key(scope, region, metric)]

	store_changed_value_in_target_rates(scope, region, metric, changed_value)

	if region == 'Total':
		allocate_total_to_regions(metric)  # TODO - Rob needs to work on this one
	else:
		calc_funds_raised(scope, region)
		calc_total_for_metric(scope, 'funds')
		# calc_total_for_apam(scope, region)

	save_target_rates(scope)




# These are column specific

def calc_funds_raised(scope, changed_region):
	metric = 'funds'

	if scope.target_selected_tenure == 'Foundation':
		base_value = scope.target_rates[changed_region]['donations']
		rate = scope.target_rates[changed_region]['ada']
	else:
		base_value = scope.target_rates[changed_region]['active']
		rate = scope.target_rates[changed_region]['apam']

	funds_raised = round((base_value * rate), 2)
	store_changed_value_in_target_rates(scope, changed_region, metric, funds_raised)

def calc_apam(scope, changed_region):
	metric = 'apam'
	apam = 0.0

	active_regos = scope.target_rates[changed_region]['active']
	funds_raised = scope.target_rates[changed_region]['funds']

	if active_regos > 0:apam = funds_raised / active_regos
		
	store_changed_value_in_target_rates(scope, changed_region, metric, apam)

def calc_ada(scope, changed_region):
	metric = 'ada'
	ada = 0.0

	donations = scope.target_rates[changed_region]['donations']
	funds_raised = scope.target_rates[changed_region]['funds']

	if donations > 0:ada = funds_raised / donations
		
	store_changed_value_in_target_rates(scope, changed_region, metric, ada)


# Total Column Only

def calc_total_for_metric(scope, metric):
	
	metric_total = 0

	for region in scope.target_regions:
		if region not in ['row_heading', 'Total']: 
			region_value = scope.target_rates[region][metric]
			metric_total += region_value

	store_changed_value_in_target_rates(scope, 'Total', metric, metric_total)

def calc_total_for_apam(scope, changed_region):

	metric = 'apam'
	total_active_regos = 0
	total_funds_raised = 0
	total_apam = 0.0

	for region in scope.target_regions:
		if region not in ['row_heading', 'Total']: 
			total_active_regos += scope.target_rates[region]['active']
			total_funds_raised += scope.target_rates[region]['funds']

	if total_active_regos > 0:total_apam = total_funds_raised / total_active_regos
	store_changed_value_in_target_rates(scope, 'Total', metric, total_apam)

def calc_total_for_ada(scope, changed_region):

	metric = 'ada'
	total_donations = 0
	total_funds_raised = 0
	total_ada = 0.0

	for region in scope.target_regions:
		if region not in ['row_heading', 'Total']: 
			total_donations += scope.target_rates[region]['donations']
			total_funds_raised += scope.target_rates[region]['funds']

	if total_donations > 0:total_ada = total_funds_raised / total_donations
		
	store_changed_value_in_target_rates(scope, 'Total', metric, total_ada)






# def calc_average(scope, metric):

# 	average = 0.0

# 	if metric == 'apam':
# 		numerator = scope.target_rates['Total']['funds']
# 		denominator = scope.target_rates['Total']['active']

# 	if metric == 'ada':
# 		numerator = scope.target_rates['Total']['funds']
# 		denominator = scope.target_rates['Total']['donations']

# 	if numerator > 0 and denominator > 0:
# 		average = numerator / denominator

# 	scope.target_rates['Total'][metric] = average


def allocate_total_to_regions(scope, metric):
	total_to_allocate = scope.target_rates['Total'][metric]
	regional_values = {}

	# Store the current values of each region in a dictionary
	for region in scope.target_regions:
		if region not in ['row_heading', 'Total']:
			regional_values[region] = scope.target_rates[region][metric]
	print('initial regional values = ', regional_values)
	# calculate the proprotion of each regional value before the new allocation
	regional_total = sum(regional_values.values())

	for region, region_value in regional_values.items():
		proportion = region_value / regional_total
		new_region_value = total_to_allocate * proportion

		if metric in ['regos', 'active']:
			# round values that have no right to have decimal places 
			# i.e. .63292 of a person is not really possible
			new_region_value = int(new_region_value)

		# Store the proportion in our regional_values dictionary
		regional_values[region] = new_region_value
	print('intial allocation to regions = ', regional_values)
	# Determine if there is any under or over allocation and apply it against 
	# the largest category (or other which is the default)
	total_allocated = sum(regional_values.values())
	under_over_allocated = total_to_allocate - total_allocated
	print( 'under_over_alloc = ', under_over_allocated)
	if under_over_allocated != 0:

		adjusting_region = max(regional_values, key=regional_values.get)
		print('attempting to ajust region > ', adjusting_region)
		regional_values[adjusting_region] = regional_values[adjusting_region] + under_over_allocated
		
	# Store the new values against each regional value
	for region, region_value in regional_values.items():
		scope.target_rates[region][metric] = region_value













# def update_totals(scope):

# 	tenure_metrics = tenure_levels[scope.target_selected_tenure]

# 	if scope.target_setting_method == 'Region':

# 		# Update Totals Records Only - add together each region
# 		reset_totals(scope, tenure_metrics)

# 		# Calculate Line total first - basic cumulative for each metric in each region
# 		if 'regos' in tenure_metrics:
# 			calc_total_for_metric(scope, 'regos')

# 		if 'active' in tenure_metrics:
# 			calc_total_for_metric(scope, 'active')

# 		if 'funds' in tenure_metrics:
# 			calc_total_for_metric(scope, 'funds')

# 		if 'donations' in tenure_metrics:
# 			calc_total_for_metric(scope, 'donations')

# 		# Calculate Ratios after all the Line totals have been calculated	
# 		if 'apam' in tenure_metrics:
# 			calc_average(scope, 'apam')

# 		if 'ada' in tenure_metrics:
# 			calc_average(scope, 'ada')


# 	if scope.target_setting_method == 'Country':

# 		print( 'Allocation based on proportion of total')

# 		if 'regos' in tenure_metrics:
# 			allocate_total_to_regions(scope, 'regos')

















	# total_active = scope.target_rates['Total']['active']
	# total_funds = scope.target_rates['Total']['funds']
	# if total_active > 0 and total_funds > 0:
	# 	total_apam = total_funds / total_active
	# scope.target_rates['Total']['apam'] = total_apam

	# total_donations = scope.target_rates['Total']['donations']
	# total_funds = scope.target_rates['Total']['funds']
	# if total_donations > 0 and total_funds > 0:
	# 	total_ada = total_funds / total_donations
	# scope.target_rates['Total']['ada'] = total_ada
