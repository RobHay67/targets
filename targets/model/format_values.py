



	
	

# close 			= "$ {:6,.2f}".format(last_row_df.iloc[0]['close'])



def format_regos(regos):

	formatted_regos = "{:,}".format(regos) 

	return formatted_regos


def format_dolls(dolls):

	formatted_dollars = "$ {:,.2f}".format(dolls)

	return formatted_dollars


def format_percent(percentage):

	percentage = percentage * 100

	formatted_percentage = "{:,.2f} %".format(percentage)

	return formatted_percentage