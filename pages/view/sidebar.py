import streamlit as st

from config.model.page import set_page


def render_sidebar(scope):
	st.sidebar.title('Target Setting Application')
	
	st.sidebar.write('Peer to Peer and Foundation')
	st.sidebar.write('---------')
	st.sidebar.write('Financial Year : **1 May ' + str(scope.campaign) + ' to 30 April ' + str(scope.campaign + 1) + '**')
	st.sidebar.write('Campaign (November) : ' + '**' + str(scope.campaign) + '**')
	st.sidebar.write('Budget Version : ' + '**' + scope.budget_version + '**')

	st.sidebar.write('---------')

	st.sidebar.write('Welcome : ' + '**' + scope.user_name + '**')

	previous_country = scope.selected_country

	scope.selected_country = st.sidebar.selectbox ( 
												label=('Available Countries'), 
												options=scope.dropdown_countries,
												# key='91',
												) 

	if scope.selected_country != previous_country : 
		scope.page_to_display = 'targets'

	st.sidebar.write('---------')

	if scope.user_can_edit_forex_rates:
		st.sidebar.button('Forex Rates', on_click=set_page, args=('forex', ))
	if scope.user_can_edit_config:
		st.sidebar.button('System Settings', on_click=set_page, args=('config', ))


