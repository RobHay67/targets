
import streamlit as st

from config.model.currency import currency_name, currency_symbol
from targets.view.widgets import render_country_selector, render_target_setting_method


def render_targets_header(scope):

	col1,col2,col3,col4 = st.columns([1,2,1,1])

	with col1:
			st.header('Target Rates')
	with col2:

		render_country_selector(scope)


	with col3: 
		currency = currency_name(scope.user_selected_country)
		dollar_symbol = currency_symbol(scope.user_selected_country)

		st.write('Currency = ' + currency +' ( ' + dollar_symbol + ' )')
	with col4:

		render_target_setting_method(scope)


	st.markdown("""---""")


def tenure_group_header(scope):

	if scope.target_selected_tenure == 'Foundation':
		header_string = (str(scope.target_selected_tenure) + ' Donors')
	else:
		header_string = (str(scope.target_selected_tenure) + ' Fundraisers')


	return header_string