from targets.model.save import save_target_rates


def copy_prior_year_tenure_rates(scope):
	print('lets copy last years rates')
	scope.target_rates = scope.target_base_rates

	# In the case where tenure = Retained, we need to swap around the campaign totals
	if scope.target_selected_tenure == 'Retained':
		for region, values in scope.target_rates.items():
			previous_campaign_total_regos = scope.target_rates[region]['regos_total_curnt']
			scope.target_rates[region]['regos_total_prior'] = previous_campaign_total_regos
			# we do not know what this value is yet
			scope.target_rates[region]['regos_total_curnt'] = 0



	save_target_rates(scope)


