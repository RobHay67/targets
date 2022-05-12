

# Metrics Reqired by each Tenure level



regos = 'regos'							# Total number of registrations for the tenure category
active = 'active'						# Number of Financialy Active Registrations for the tenure category
funds = 'funds'							# Total Funds Raised by the tenure category including Foundation
apam = 'apam'							# Average Per Active Mo - Ratio of funds /  active

regos_total_prior = 'regos_total_prior'	# Total number of Registrations in all tenure categories in the campaign ONE years prior
regos_total_curnt = 'regos_total_curnt'	# Total number of Registrations in all tenure categories in the current campaign - used for current target rates

donations = 'donations'					# Total Number of Donations
ada = 'ada'								# Average Donation Amount

comment = 'comment'						# A place for the user to leave some words
tenure_levels = {
					'New'		:[regos, active, funds, apam, comment],
					'Returned'	:[regos, active, funds, apam, comment],
					'Retained'	:[regos, active, funds, apam, comment, regos_total_prior, regos_total_curnt],
					'Foundation':[donations,     funds, ada , comment],
				}





def scope_tenure(scope):
	
	scope.dropdown_tenure = list(tenure_levels.keys())

	scope.target_selected_tenure = 'New'			# set default value for tenure




