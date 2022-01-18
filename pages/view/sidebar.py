import streamlit as st

from config.model.page import set_page


def render_sidebar(scope):

	st.sidebar.write('User : ' + '**' + scope.user_name + '**')
	st.sidebar.write('Campaign (November) : ' + '**' + str(scope.campaign) + '**')
	st.sidebar.write('Budget Version : ' + '**' + scope.budget_version + '**')
	
	st.sidebar.write('---------')

	previous_country = scope.selected_country

	scope.selected_country = st.sidebar.selectbox ( 
												label=('Country / Market'), 
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


