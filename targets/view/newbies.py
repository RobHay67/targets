import streamlit as st


from targets.model.rates_for_view import target_rates_for_view
from targets.model.save import save_target_rates

from targets.view.header import tenure_group_header
from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from targets.view.widgets import render_regos_widget, render_active_widget, render_apam_widget, render_funds_widget






def render_new_fundraisers(scope):

	target_rates_for_view(scope)

	header_string = tenure_group_header(scope)
	# no_of_columns = len(scope.target_columns)
	

	st.subheader(header_string)


	for region in scope.target_columns:
		col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])
		if region == 'row_heading':
			tenure_headings(col1,col2,col3,col4,col5,col6)
		else:
			with col1: st.write('**'+region+'**')
			with col2: render_regos_widget(scope, region)
			with col3: render_active_widget(scope, region)
			with col4: render_apam_widget(scope, region)
			with col5: render_funds_widget(scope, region)

	copy_rates = st.button('Copy Last Years Rates')



	st.markdown("""---""")

	previous_campaign = str(scope.campaign - 1)
	st.subheader(header_string + ' ( base values from ' + previous_campaign + ')')

	for region in scope.target_columns:
		col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])
		if region == 'row_heading':
			tenure_headings(col1,col2,col3,col4,col5,col6)
		else:
			rates = scope.target_base_rates[region]
			active_ratio = 0.0

			if rates['regos'] != 0:
				active_ratio = rates['active'] / rates['regos']			

			with col1: st.markdown(format_string(region, align='Left', bold=False), unsafe_allow_html=True)
			with col2: st.markdown(format_regos(rates['regos'], align='right'), unsafe_allow_html=True)
			with col3: st.markdown(format_regos(rates['active'], align='right'), unsafe_allow_html=True)
			with col4: st.markdown(format_dolls(rates['apam'], align='right'), unsafe_allow_html=True)
			with col5: st.markdown(format_dolls(rates['funds'], align='right'), unsafe_allow_html=True)
			with col6: st.markdown(format_percent(active_ratio, align='right'), unsafe_allow_html=True)





	if copy_rates:
		print('lets copy last years rates')
		scope.target_rates = scope.target_base_rates
		save_target_rates(scope)










def tenure_headings(col1,col2,col3,col4,col5,col6):
	with col1: st.write('**Region**')
	with col2: st.markdown(format_string('Registrations',align='Center'), unsafe_allow_html=True)
	with col3: st.markdown(format_string('Active Registrations',align='Center'), unsafe_allow_html=True)
	with col4: st.markdown(format_string('Average Per Active Mo (APAM)', align='Center'), unsafe_allow_html=True)
	with col5: st.markdown(format_string('Funds Raised', align='Center'), unsafe_allow_html=True)
	with col6: st.markdown(format_string('Active Ratio (%))', align='Center'), unsafe_allow_html=True)

	


