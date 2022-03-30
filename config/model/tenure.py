

# Metrics Reqired by each Tenure level



regos_ret_prior = 'regos_ret_prior'		# Number of Fundraisers who were Retained 2 campaigns ago
regos_total_prior = 'regos_total_prior'	# Total number of Registrations in all tenure categories (New, Retained and Returning ) excludes Foundation

regos = 'regos'							# Total number of registrations for the tenure category
active = 'active'						# Number of Financialy Active Registrations for the tenure category
funds = 'funds'							# Total Funds Raised by the tenure category including Foundation
apam = 'apam'							# Average Per Active Mo - Ratio of funds /  active

donations = 'donations'					# Total Number of Donations
ada = 'ada'								# Average Donation Amount

tenure_levels = {
					'New'		:[regos, active, funds, apam],
					'Retained'	:[regos, active, funds, apam, regos_ret_prior, regos_total_prior],
					'Returning'	:[regos, active, funds, apam],
					'Foundation':[donations,     funds, ada],
				}



def scope_tenure(scope):
	
	scope.dropdown_tenure = list(tenure_levels.keys())

	scope.target_selected_tenure = 'New'			# set default value for tenure




