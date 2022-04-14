

def submit_label(scope):
	if scope.user_target_setting_method == 'Region':
		submit_label = 'Save Regional Changes'
	else:
		submit_label = 'Save Totals and Allocate Changes to Regions'

	
	return submit_label