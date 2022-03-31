import streamlit as st


from config.model.target_rates import target_rates_for_view

from targets.view.tenure_selector import tenure_group_header
from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from targets.view.metrics import render_regos_widget, render_active_widget, render_apam_widget, render_funds_widget

# from config.model.countries import country_key_from_name
# from targets.model.save import save_target_rates
# from targets.model.totals import update_totals
# from targets.model.can_edit import is_column_editable
# from targets.view.submit_button import submit_label
# from targets.model.totals import on_change_regos, on_change_active_regos, on_change_apam, on_change_funds


# last years value can serve as defaults for the current campaign, but only if the current campaign is missing these rates??




def render_new_fundraisers(scope):

	target_rates_for_view(scope)

	header_string = tenure_group_header(scope)
	no_of_columns = len(scope.target_regions)
		
	st.subheader(header_string)
	cols = st.columns(no_of_columns)
	for i, col in enumerate(cols):
		region = scope.target_regions[i]

		if region == 'row_heading':
			col.write('')	# This is an empty column to better align cols with the base rate cols
		else:
			with col:
				st.write('**'+region+'**')
				render_regos_widget(scope, region)
				render_active_widget(scope, region)
				render_apam_widget(scope, region)
				render_funds_widget(scope, region)


	st.markdown("""---""")

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
				


	# st.markdown("""---""")










	

	



				# col_name = 'Registrations'
			# metric = 'regos'
			# widget_key_regos = create_widget_key(scope, region, metric)

			
			# with col:
			# 	if editable_column:
			# 		scope.target_rates[region]['regos'] = st.number_input(
			# 														label=col_name, 
			# 														value=scope.target_rates[region]['regos'], 
			# 														format="%.0i", # format="%.0f",
			# 														step=1.0,
			# 														on_change=on_change_regos,
			# 														args=(region, ),
			# 														key=(widget_key_regos)
			# 														)
			# 	else:
			# 		st.write(col_name)
			# 		col.markdown(format_regos(rates['regos'], align='left'), unsafe_allow_html=True)
			# 		st.write('')
			# 		st.write('')

			# col_name = 'Active Registrations'
			# metric = 'active'
			# widget_key_active = create_widget_key(scope, region, metric)

			# with col:
			# 	if editable_column:
			# 		scope.target_rates[region][metric] = st.number_input(
			# 														label=col_name, 
			# 														value=scope.target_rates[region][metric], 
			# 														format="%.0i", # format="%.0f",
			# 														step=1.0, 
			# 														on_change=on_change_active_regos,
			# 														args=(region, ),
			# 														key=(widget_key_active)
			# 														)
			# 	else:
			# 		st.write(col_name)
			# 		col.markdown(format_regos(rates['active'], align='left'), unsafe_allow_html=True)
			# 		st.write('')
			# 		st.write('')

			# col_name = 'APAM - Average Per Active Mo'
			# widget_key_regos = 'widget_target_' + payment_country + '_' + region + '_' + scope.target_selected_tenure + '_apam'
			# with col:
			# 	if editable_column:
			# 		scope.target_rates[region]['apam'] = st.number_input(
			# 														label=col_name, 
			# 														value=scope.target_rates[region]['apam'], 
			# 														format='%.2f', # format="%.0f",
			# 														step=1.0, 
			# 														key=(widget_key_regos)
			# 														)
			# 	else:
			# 		st.write(col_name)
			# 		col.markdown(format_dolls(rates['apam'], align='left'), unsafe_allow_html=True)
			# 		st.write('')
			# 		st.write('')

			# col_name = 'Funds Raised'
			# widget_key_regos = 'widget_target_' + payment_country + '_' + region + '_' + scope.target_selected_tenure + '_funds'
			# with col:
			# 	if editable_column:
			# 		scope.target_rates[region]['funds'] = st.number_input(
			# 														label=col_name, 
			# 														value=scope.target_rates[region]['funds'], 
			# 														format='%.2f', # format="%.0f",
			# 														step=1.0, 
			# 														key=(widget_key_regos)
			# 														)
			# 	else:
			# 		st.write(col_name)
			# 		col.markdown(format_dolls(rates['funds'], align='left'), unsafe_allow_html=True)
			# 		st.write('')
			# 		st.write('')


		# submit_button = st.form_submit_button(label=submit_label(scope))

		# if submit_button: 
		# 	update_totals(scope)
		# 	save_target_rates(scope)



	# st.slider(label='Active Fundraisers', value=50, key='this')





