import streamlit as st


from targets.model.rates_for_view import target_rates_for_view

from targets.view.header import tenure_group_header
from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from targets.view.widgets import render_donations_widget, render_ada_widget, render_funds_widget


def render_foundation_donations(scope):

	target_rates_for_view(scope)

	header_string = tenure_group_header(scope)
	no_of_columns = len(scope.target_columns)

		
	st.subheader(header_string)
	cols = st.columns(no_of_columns)
	for i, col in enumerate(cols):
		region = scope.target_columns[i]

		if region == 'row_heading':
			col.write('Region')	# This is an empty column to better align cols with the base rate cols
		else:
			with col:
				st.write('**'+region+'**')
				render_donations_widget(scope, region)
				render_ada_widget(scope, region)
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
			col.markdown(format_string('Donations' ,align='Left'), unsafe_allow_html=True)
			col.markdown(format_string('ADA' ,align='Left'), unsafe_allow_html=True)
			col.markdown(format_string('Funds Raised' ,align='Left'), unsafe_allow_html=True)
		else:
			rates = scope.target_base_rates[region]

			col.markdown(format_string(region, align='Right', bold=False), unsafe_allow_html=True)
			# col.markdown("""---""")
			col.markdown(format_regos(rates['donations'], align='right'), unsafe_allow_html=True)
			col.markdown(format_regos(rates['ada'], align='right'), unsafe_allow_html=True)
			col.markdown(format_dolls(rates['funds'], align='right'), unsafe_allow_html=True)
				




