
from config.model.tenure import tenure_levels


# regos > sum each region
# active > sum each region
# funds > sum each region
# donations > sum each region
# apam > ratio based on other sums - so do this last
# ada  > ratio based on other sums - so do this last


def reset_totals(scope, tenure_metrics):

	for metric in tenure_metrics:
		scope.target_rates['Total'][metric] = 0.0


def total_metric(scope, metric):

	total = scope.target_rates['Total'][metric]

	for region in scope.target_regions:
		if region not in ['row_heading', 'Total']: 
			region_value = scope.target_rates[region][metric]
			total += region_value
	
	scope.target_rates['Total'][metric] = total


def calc_average(scope, metric):

	average = 0.0

	if metric == 'apam':
		numerator = scope.target_rates['Total']['funds']
		denominator = scope.target_rates['Total']['active']

	if metric == 'ada':
		numerator = scope.target_rates['Total']['funds']
		denominator = scope.target_rates['Total']['donations']

	if numerator > 0 and denominator > 0:
		average = numerator / denominator

	scope.target_rates['Total'][metric] = average


def allocate_metric(scope, metric):

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





def update_totals(scope):

	tenure_metrics = tenure_levels[scope.target_selected_tenure]

	if scope.target_setting_method == 'Region':

		# Update Totals Records Only - add together each region
		reset_totals(scope, tenure_metrics)

		# Calculate Line total first - basic cumulative for each metric in each region
		if 'regos' in tenure_metrics:
			total_metric(scope, 'regos')

		if 'active' in tenure_metrics:
			total_metric(scope, 'active')

		if 'funds' in tenure_metrics:
			total_metric(scope, 'funds')

		if 'donations' in tenure_metrics:
			total_metric(scope, 'donations')

		# Calculate Ratios after all the Line totals have been calculated	
		if 'apam' in tenure_metrics:
			calc_average(scope, 'apam')

		if 'ada' in tenure_metrics:
			calc_average(scope, 'ada')


	if scope.target_setting_method == 'Country':

		print( 'Allocation based on proportion of total')

		if 'regos' in tenure_metrics:
			allocate_metric(scope, 'regos')

















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

