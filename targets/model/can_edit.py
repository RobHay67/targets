



def is_column_editable(scope, region):
	if scope.target_setting_method == 'Region' and region == 'Total':
		# We are updates rates for each Region, therefore
		# the Total column is just an output of this process
		# and given that this is the Total column, we dont want to allow edits
		editable_column = False
	elif scope.target_setting_method == 'Country' and region != 'Total':
		# see above, but this one is essentially the opposite, we are
		# looking at a regional column, but we only want to target set 
		# by the total column (which this is not)
		editable_column = False
	else:
		# see above, but we can edit this column
		editable_column = True

	return editable_column