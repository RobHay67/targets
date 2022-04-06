

# Metrics Reqired by each Tenure level



regos_campaign_two_ago = 'regos_campaign_two_ago'	# Total number of Registrations in all tenure categories in the campaign TWO years prior
regos_campaign_one_ago = 'regos_campaign_one_ago'	# Total number of Registrations in all tenure categories in the campaign ONE years prior

regos = 'regos'							# Total number of registrations for the tenure category
active = 'active'						# Number of Financialy Active Registrations for the tenure category
funds = 'funds'							# Total Funds Raised by the tenure category including Foundation
apam = 'apam'							# Average Per Active Mo - Ratio of funds /  active

donations = 'donations'					# Total Number of Donations
ada = 'ada'								# Average Donation Amount

tenure_levels = {
					'New'		:[regos, active, funds, apam],
					'Retained'	:[regos, active, funds, apam, regos_campaign_one_ago, regos_campaign_two_ago],
					'Returning'	:[regos, active, funds, apam],
					'Foundation':[donations,     funds, ada],
				}


# TODO - I dont think this value is used - regos_campaign_one_ago


def scope_tenure(scope):
	
	scope.dropdown_tenure = list(tenure_levels.keys())

	scope.target_selected_tenure = 'New'			# set default value for tenure




