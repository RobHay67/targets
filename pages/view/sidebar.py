import streamlit as st

from config.model.page import set_page


def render_sidebar(scope):
	st.sidebar.title('Target Setting Application')
	st.sidebar.write('Peer to Peer and Foundation')
	st.sidebar.write('Welcome : ' + '**' + scope.user_name + '**')
	st.sidebar.write('Does not split by Team')
	st.sidebar.write('---------')
	
	st.sidebar.write('Financial Year : **1 May ' + str(scope.campaign) + ' to 30 April ' + str(scope.campaign + 1) + '**')
	st.sidebar.write('Campaign : ' + '**' + str(scope.campaign) + '**')
	st.sidebar.write('Application Version : ' + '**' + scope.budget_version + '**')

	st.sidebar.write('---------')
	
	if len(scope.user_country_codes) > 0:
		st.sidebar.button('Target Rates', on_click=set_page, args=('targets', ))
		st.sidebar.write('---------')

	if scope.user_can_edit_forex_rates:
		st.sidebar.button('Forex Rates', on_click=set_page, args=('forex', ))

	if scope.user_can_edit_previous_rates:
		help_string = 'Edit the rates for previous campaigns.'
		st.sidebar.button('Campaign Rates', on_click=set_page, args=('rates', ), help=help_string)

	if scope.user_can_edit_config:
		st.sidebar.button('System Settings', on_click=set_page, args=('config', ))


