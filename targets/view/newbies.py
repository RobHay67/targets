import streamlit as st


from config.model.target_rates import target_rates_for_view


from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from targets.view.tenure_selector import tenure_group_header

from config.model.countries import country_key_from_name

from targets.model.save import save_target_rates

from targets.model.totals import update_totals
from targets.model.can_edit import is_column_editable
from targets.view.submit_button import submit_label

# TODO - ensure we have these variables

	# campaigns 2			ok	scope.campaign	
	# country	1			ok	scope.target_selected_country
	# tenure	1			ok 	scope.target_selected_tenure
	# regions	multiple	ok	scope.target_regions
	# metrics	multiple		hard coded
	# values	multiple		hard coded











def render_new_fundraisers(scope):

	target_rates_for_view(scope)

	header_string = tenure_group_header(scope)
	no_of_columns = len(scope.target_regions)
	payment_country = country_key_from_name(scope.target_selected_country)

	# Update Values Section
	with st.form(key='newbies_form'):
		
		st.subheader(header_string)
		cols = st.columns(no_of_columns)
		for i, col in enumerate(cols):
			region = scope.target_regions[i]
			editable_column = is_column_editable(scope, region)

			if region == 'row_heading':
				# This is an empty column to better align cols with the base rate cols
				col.write('')
			else:
				# Add the Region or Total to the top row of each column
				col.write('**'+region+'**')

				rates = scope.target_rates[region]

				col_name = 'Registrations'
				widget_key_regos = 'widget_target_' + payment_country + '_' + region + '_' + scope.target_selected_tenure + '_regos'
				
				with col:
					if editable_column:
						scope.target_rates[region]['regos'] = st.number_input(
																		label=col_name, 
																		value=scope.target_rates[region]['regos'], 
																		format="%.0i", # format="%.0f",
																		step=1.0, 
																		key=(widget_key_regos)
																		)
					else:
						st.write(col_name)
						col.markdown(format_regos(rates['regos'], align='left'), unsafe_allow_html=True)
						st.write('')
						st.write('')

				col_name = 'Active Registrations'
				widget_key_regos = 'widget_target_' + payment_country + '_' + region + '_' + scope.target_selected_tenure + '_active'
				with col:
					if editable_column:
						scope.target_rates[region]['active'] = st.number_input(
																		label=col_name, 
																		value=scope.target_rates[region]['active'], 
																		format="%.0i", # format="%.0f",
																		step=1.0, 
																		key=(widget_key_regos)
																		)
					else:
						st.write(col_name)
						col.markdown(format_regos(rates['active'], align='left'), unsafe_allow_html=True)
						st.write('')
						st.write('')

				col_name = 'APAM - Average Per Active Mo'
				widget_key_regos = 'widget_target_' + payment_country + '_' + region + '_' + scope.target_selected_tenure + '_apam'
				with col:
					if editable_column:
						scope.target_rates[region]['apam'] = st.number_input(
																		label=col_name, 
																		value=scope.target_rates[region]['apam'], 
																		format='%.2f', # format="%.0f",
																		step=1.0, 
																		key=(widget_key_regos)
																		)
					else:
						st.write(col_name)
						col.markdown(format_dolls(rates['apam'], align='left'), unsafe_allow_html=True)
						st.write('')
						st.write('')

				col_name = 'Funds Raised'
				widget_key_regos = 'widget_target_' + payment_country + '_' + region + '_' + scope.target_selected_tenure + '_funds'
				with col:
					if editable_column:
						scope.target_rates[region]['funds'] = st.number_input(
																		label=col_name, 
																		value=scope.target_rates[region]['funds'], 
																		format='%.2f', # format="%.0f",
																		step=1.0, 
																		key=(widget_key_regos)
																		)
					else:
						st.write(col_name)
						col.markdown(format_dolls(rates['funds'], align='left'), unsafe_allow_html=True)
						st.write('')
						st.write('')


		submit_button = st.form_submit_button(label=submit_label(scope))

		if submit_button: 
			update_totals(scope)
			save_target_rates(scope)



	# st.slider(label='Active Fundraisers', value=50, key='this')


	with st.form(key='base_data_form'):
	
		st.subheader(header_string + ' ( base values )')

		cols = st.columns(no_of_columns)

		for i, col in enumerate(cols):

			region = scope.target_regions[i]
			

			if region == 'row_heading':
				col.markdown(format_string('Metrics' ,align='Left'), unsafe_allow_html=True)
				col.markdown("""---""")
				col.markdown(format_string('Registrations' ,align='Left'), unsafe_allow_html=True)
				col.markdown(format_string('Active Registrations' ,align='Left'), unsafe_allow_html=True)
				col.markdown(format_string('Average Per Active Mo (APAM)' ,align='Left'), unsafe_allow_html=True)
				col.markdown(format_string('Funds Raised' ,align='Left'), unsafe_allow_html=True)
				col.markdown(format_string('Active Ratio/Rate (%)' ,align='Left'), unsafe_allow_html=True)
			else:
				rates = scope.target_base_rates[region]

				if rates['regos'] != 0:
					active_ratio = rates['active'] / rates['regos']
				else:
					active_ratio = 0.0

				col.markdown(format_string(region, align='Right', bold=False), unsafe_allow_html=True)
				col.markdown("""---""")
				col.markdown(format_regos(rates['regos'], align='right'), unsafe_allow_html=True)
				col.markdown(format_regos(rates['active'], align='right'), unsafe_allow_html=True)
				col.markdown(format_dolls(rates['apam'], align='right'), unsafe_allow_html=True)
				col.markdown(format_dolls(rates['funds'], align='right'), unsafe_allow_html=True)
				col.markdown(format_percent(active_ratio, align='right'), unsafe_allow_html=True)
				

		print('='*100)

		st.markdown("""---""")

		submit_button = st.form_submit_button(label='Refresh')





	# 	st.write('This is something')

	# TODO this method will only work if all the values are there!!

	regos = int(scope.target_df.loc[  
								  (scope.target_df['payment_country'] 	== 'au') 
								& (scope.target_df['region'] 			== 'Total') 
								& (scope.target_df['tenure'] 			== 'New') 
								& (scope.target_df['metric'] 			== 'regos') 
								]['result'].values[0])




	# we will need to format the values as appropriate - so regos is and integer and apam is displayed as 2 decimal places, but is a float

	# they can serve as defaults for the current campaign, but only if the current campaign is missing these rates??

	# we need to create widgets with appropriate names

	# this should all be in a form - right????


	

	





