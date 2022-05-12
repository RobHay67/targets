import streamlit as st


from targets.model.rates_for_view import target_rates_for_view
from targets.model.copy import copy_prior_year_tenure_rates
from targets.view.header import tenure_group_header
from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from targets.view.widgets import render_donations_widget, render_ada_widget, render_funds_widget


def render_foundation_donations(scope):

	target_rates_for_view(scope)

	st.subheader(tenure_group_header(scope))

	for region in scope.target_columns:
		col1,col2,col3,col4 = st.columns([2,2,2,2])
		if region == 'row_heading':
			tenure_headings(col1,col2,col3,col4)
		else:
			with col1: 
				st.write('')
				st.write('')
				st.write('**'+region+'**')
			with col2: render_donations_widget(scope, region)
			with col3: render_ada_widget(scope, region)
			with col4: render_funds_widget(scope, region)

	st.button( 	label='Copy Last Years Rates ( over-writes all of the above rates )', 
				on_click=copy_prior_year_tenure_rates, 
				args=(scope, )
				)

	st.markdown("""---""")


	previous_campaign = str(scope.campaign - 1)
	st.subheader(tenure_group_header(scope) + ' ( base values from ' + previous_campaign + ')')

	for region in scope.target_columns:
		col1,col2,col3,col4 = st.columns([2,2,2,2])
		if region == 'row_heading':
			tenure_headings(col1,col2,col3,col4)
		else:
			rates = scope.target_base_rates[region]

			with col1: st.markdown(format_string(region, align='Left', bold=False), unsafe_allow_html=True)
			with col2: st.markdown(format_regos(rates['donations'], align='right'), unsafe_allow_html=True)
			with col3: st.markdown(format_dolls(rates['ada'], align='right'), unsafe_allow_html=True)
			with col4: st.markdown(format_dolls(rates['funds'], align='right'), unsafe_allow_html=True)



def tenure_headings(col1,col2,col3,col4):
	with col1: st.write('**Region**')
	with col2: st.markdown(format_string('Donations',align='Right'), unsafe_allow_html=True)
	with col3: st.markdown(format_string('Average Donation Amount (ADA)',align='Right'), unsafe_allow_html=True)
	with col4: st.markdown(format_string('Funds Raised', align='Right'), unsafe_allow_html=True)






	# header_string = tenure_group_header(scope)






	# no_of_columns = len(scope.target_columns)

		
	# st.subheader(header_string)
	# cols = st.columns(no_of_columns)
	# for i, col in enumerate(cols):
	# 	region = scope.target_columns[i]

	# 	if region == 'row_heading':
	# 		col.write('Region')	# This is an empty column to better align cols with the base rate cols
	# 	else:
	# 		with col:
	# 			st.write('**'+region+'**')
	# 			render_donations_widget(scope, region)
	# 			render_ada_widget(scope, region)
	# 			render_funds_widget(scope, region)


	# st.markdown("""---""")
	# previous_campaign = str(scope.campaign - 1)
	# st.subheader(header_string + ' ( base values from ' + previous_campaign + ')')

	# cols = st.columns(no_of_columns)

	# for i, col in enumerate(cols):

	# 	region = scope.target_columns[i]
		

	# 	if region == 'row_heading':
	# 		col.markdown(format_string('Metrics' ,align='Left'), unsafe_allow_html=True)
	# 		# col.markdown("""---""")
	# 		col.markdown(format_string('Donations' ,align='Left'), unsafe_allow_html=True)
	# 		col.markdown(format_string('ADA' ,align='Left'), unsafe_allow_html=True)
	# 		col.markdown(format_string('Funds Raised' ,align='Left'), unsafe_allow_html=True)
	# 	else:
	# 		rates = scope.target_base_rates[region]

	# 		col.markdown(format_string(region, align='Right', bold=False), unsafe_allow_html=True)
	# 		# col.markdown("""---""")
	# 		col.markdown(format_regos(rates['donations'], align='right'), unsafe_allow_html=True)
	# 		col.markdown(format_regos(rates['ada'], align='right'), unsafe_allow_html=True)
	# 		col.markdown(format_dolls(rates['funds'], align='right'), unsafe_allow_html=True)
