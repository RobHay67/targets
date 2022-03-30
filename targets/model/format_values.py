



# Allowable alignments
# center
# left
# right
# justify



def format_string(string, align=None, bold=False ):

	formatted_string = str(string)

	# if bold == True:								# TODO - bold does not seem to be working correctly
	# 	formatted_string = f"""
	# 							__{formatted_string}__
	# 						"""
	if align != None:
		formatted_string = f"""
							<div style="text-align: {align};">{formatted_string}</div>
						"""
	return formatted_string


def format_regos(regos, align=None):

	regos = int(regos)

	formatted_regos = "{:,}".format(regos) 

	if align != None:
		formatted_regos = f"""
							<div style="text-align: {align};">{formatted_regos}</div>
						"""

	return formatted_regos


def format_dolls(dolls, align=None):

	formatted_dollars = "$ {:,.2f}".format(dolls)

	if align != None:
		formatted_dollars = f"""
							<div style="text-align: {align};">{formatted_dollars}</div>
						"""

	return formatted_dollars


def format_percent(percentage, align=None):

	percentage = percentage * 100

	formatted_percentage = "{:,.2f} %".format(percentage)

	if align != None:
		formatted_percentage = f"""
							<div style="text-align: {align};">{formatted_percentage}</div>
						"""

	return formatted_percentage