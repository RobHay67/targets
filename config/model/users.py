



# TODO : Expect this to be loaded from somewhere - txt file or a database

def scope_user(scope):
	scope.user_name = 'Rob Hay'
	scope.user_pword = 'Bella12'
	
	# scope.user_country_codes = ['ca', 'au', 'be']			# List of Countries the User can See or Edit
	# scope.user_country_codes = ['au']
	scope.user_country_codes = ['all']			# lowercase all just to be safe

	scope.user_can_edit_targets = True				# User can make changes to the Targets

	# Special Admin Code
	scope.user_can_see_total_movember = False
	scope.user_can_edit_forex_rates = True


	
	
	# This will be just for the Insights team so we can set specal params - maybe finance
	scope.user_can_edit_previous_rates = True
	scope.user_can_edit_config = True


