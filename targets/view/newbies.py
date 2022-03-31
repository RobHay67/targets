import streamlit as st


from config.model.target_rates import target_rates_for_view


from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from targets.view.tenure_selector import tenure_group_header

from config.model.countries import country_key_from_name

from targets.model.save import save_target_rates

from targets.model.totals import update_totals

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
			# rates = scope.target_base_rates[region]
			
			disable_col_for_edits = False

			# Determine if Column is editable or not
			if scope.target_setting_method == 'Region' and region == 'Total':
				disable_col_for_edits = True
			elif scope.target_setting_method == 'Country' and region != 'Total':
				disable_col_for_edits = True
			
			if region == 'row_heading':
				# This is an empty column to better align cols with the base rate cols
				col.write('')
			else:
				col.write('**'+region+'**')

				widget_key_regos = 'widget_target_' + payment_country + '_' + region + '_' + scope.target_selected_tenure + '_regos'
				with col:
					scope.target_rates[region]['regos'] = st.number_input(
																		label='Registrations', 
																		value=scope.target_rates[region]['regos'], 
																		format="%.0f", 
																		step=1.0, 
																		# disabled=disable_col_for_edits,
																		key=(widget_key_regos)
																		)



		
		if scope.target_setting_method == 'Region':
			submit_label = 'Save Regional Changes'
		else:
			submit_label = 'Save Totals and Allocate Changes to Regions'

		submit_button = st.form_submit_button(label=submit_label)

		if submit_button: 
			print('pressed submit button')
			update_totals(scope)
			# allocate_totals
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


	

	





