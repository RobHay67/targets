import streamlit as st


from targets.model.rates_for_view import target_rates_for_view
from targets.model.copy import copy_prior_year_tenure_rates
from targets.view.header import tenure_group_header
from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from targets.view.widgets import render_regos_widget, render_active_widget, render_apam_widget, render_funds_widget, render_active_ratio, render_comment


def render_returned_fundraisers(scope):

	target_rates_for_view(scope)

	st.subheader(tenure_group_header(scope))

	for region in scope.target_columns:
		col1,col2,col3,col4,col5,col6,col7 = st.columns([2,2,2,2,2,2,4])
		if region == 'row_heading':
			tenure_headings(col1,col2,col3,col4,col5,col6,col7)
		else:
			with col1: 
				st.write('')
				st.write('')
				st.write('**'+region+'**')
			with col2: render_regos_widget(scope, region)
			with col3: render_active_widget(scope, region)
			with col4: render_apam_widget(scope, region)
			with col5: render_funds_widget(scope, region)
			with col6: render_active_ratio(scope, region)
			with col7: render_comment(scope, region)

	st.button( 	label='Copy Last Years Rates ( over-writes all of the above rates )', 
				on_click=copy_prior_year_tenure_rates, 
				args=(scope, )
				)

	st.markdown("""---""")

	previous_campaign = str(scope.campaign - 1)
	st.subheader(tenure_group_header(scope) + ' ( base values from ' + previous_campaign + ')')

	for region in scope.target_columns:
		col1,col2,col3,col4,col5,col6,col7 = st.columns([2,2,2,2,2,2,4])
		if region == 'row_heading':
			tenure_headings(col1,col2,col3,col4,col5,col6,col7)
		else:
			rates = scope.target_base_rates[region]
			active_ratio = 0.0

			if rates['regos'] != 0:
				active_ratio = rates['active'] / rates['regos']			

			with col1: st.markdown(format_string(region, align='Left', bold=False), unsafe_allow_html=True)
			with col2: st.markdown(format_regos(rates['regos'], align='Right'), unsafe_allow_html=True)
			with col3: st.markdown(format_regos(rates['active'], align='Right'), unsafe_allow_html=True)
			with col4: st.markdown(format_dolls(rates['apam'], align='Right'), unsafe_allow_html=True)
			with col5: st.markdown(format_dolls(rates['funds'], align='Right'), unsafe_allow_html=True)
			with col6: st.markdown(format_percent(active_ratio, align='Center'), unsafe_allow_html=True)




def tenure_headings(col1,col2,col3,col4,col5,col6,col7):
	with col1: st.write('**Region**')
	with col2: st.markdown(format_string('Registrations',align='Right'), unsafe_allow_html=True)
	with col3: st.markdown(format_string('Active Registrations',align='Right'), unsafe_allow_html=True)
	with col4: st.markdown(format_string('Average Per Active Mo (APAM)', align='Right'), unsafe_allow_html=True)
	with col5: st.markdown(format_string('Funds Raised', align='Right'), unsafe_allow_html=True)
	with col6: st.markdown(format_string('Active Ratio (%))', align='Center'), unsafe_allow_html=True)
	with col7: st.markdown(format_string('Comments', align='Left'), unsafe_allow_html=True)





