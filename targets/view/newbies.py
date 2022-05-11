import streamlit as st


from targets.model.rates_for_view import target_rates_for_view
from targets.model.save import save_target_rates

from targets.view.header import tenure_group_header
from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from targets.view.widgets import render_regos_widget, render_active_widget, render_apam_widget, render_funds_widget

def render_new_fundraisers(scope):

	target_rates_for_view(scope)

	header_string = tenure_group_header(scope)
	no_of_columns = len(scope.target_columns)
		
	st.subheader(header_string)
	cols = st.columns(no_of_columns)
	for i, col in enumerate(cols):

		region = scope.target_columns[i]

		if region == 'row_heading':
			col.write('Region')	# This is an empty column to better align cols with the base rate cols
			copy_rates = col.button('Copy Last years Rates')
		else:
			with col:
				st.write('**'+region+'**')
				render_regos_widget(scope, region)
				render_active_widget(scope, region)
				render_apam_widget(scope, region)
				render_funds_widget(scope, region)


	st.markdown("""---""")

	previous_campaign = str(scope.campaign - 1)
	st.subheader(header_string + ' ( base values from ' + previous_campaign + ')')

	cols = st.columns(no_of_columns)
	for i, col in enumerate(cols):
		region = scope.target_columns[i]
		
		if region == 'row_heading':
			col.markdown(format_string('Metrics' ,align='Left'), unsafe_allow_html=True)
			# col.markdown("""---""")
			col.markdown(format_string('Registrations' ,align='Left'), unsafe_allow_html=True)
			col.markdown(format_string('Active' 	,align='Left'), unsafe_allow_html=True)
			col.markdown(format_string('(APAM)' 	,align='Left'), unsafe_allow_html=True)
			col.markdown(format_string('Fund$' 		,align='Left'), unsafe_allow_html=True)
			col.markdown(format_string('Active %' 	,align='Left'), unsafe_allow_html=True)
		else:
			rates = scope.target_base_rates[region]
			active_ratio = 0.0

			if rates['regos'] != 0:
				active_ratio = rates['active'] / rates['regos']			

			col.markdown(format_string(region, align='Right', bold=False), unsafe_allow_html=True)
			# col.markdown("""---""")
			col.markdown(format_regos(rates['regos'], align='right'), unsafe_allow_html=True)
			col.markdown(format_regos(rates['active'], align='right'), unsafe_allow_html=True)
			col.markdown(format_dolls(rates['apam'], align='right'), unsafe_allow_html=True)
			col.markdown(format_dolls(rates['funds'], align='right'), unsafe_allow_html=True)
			col.markdown(format_percent(active_ratio, align='right'), unsafe_allow_html=True)
				

	if copy_rates:
		print('lets copy last years rates')
		scope.target_rates = scope.target_base_rates
		save_target_rates(scope)










	

	


