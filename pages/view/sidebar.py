import streamlit as st

from config.model.page import set_page
from users.model.scope import scope_user
from targets.model.export import convert_df


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
		widget_key = scope.user_name + '_target_rates'
		st.sidebar.button(	
							'Target Rates',
							 on_click=set_page, 
							 args=('targets', ), 
							 key=widget_key
							 )
		
		
		st.sidebar.write('---------')

	if scope.user_can_edit_forex_rates:
		widget_key = scope.user_name + '_forex_rates'
		st.sidebar.button(	
							'Forex Rates', 
							on_click=set_page, 
							args=('forex', ), 
							key=widget_key
							)

	if scope.user_can_edit_previous_rates:
		widget_key = scope.user_name + '_campaign_rates'
		help_string = 'Edit the rates for previous campaigns.'
		st.sidebar.button(	
							'Campaign Rates', 
							on_click=set_page, 
							args=('rates', ), 
							key=widget_key, 
							help=help_string
							)

	if scope.user_can_edit_config:
		widget_key = scope.user_name + '_system_settings'
		st.sidebar.button(	
							'System Settings', 
							on_click=set_page, 
							args=('config', ), 
							key=widget_key
							)

	if scope.user_can_edit_users:
		widget_key = scope.user_name + '_users'
		st.sidebar.button(	
							'Users', 
							on_click=set_page, 
							args=('users', ), 
							key=widget_key 
							)

	if scope.user_can_download_rates_table:
		widget_key = scope.user_name + '_download_rates'
		st.sidebar.download_button( 
									"Download Target Rates", 
									data=convert_df(scope.target_df),
									file_name='target_rates_2022.csv', 
									mime='text/csv', 
									key=widget_key,
									)

	if scope.user_name != 'Login to Use the Application':
		widget_key = 'logout_button'
		st.sidebar.button( 
							'Logout', 
							on_click=scope_user, 
							args=(scope, ), 
							key=widget_key 
							)

