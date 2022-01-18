import streamlit as st


# from set_page import set_page
from config.model.page import set_page



# st.sidebar.button('Country', on_click=set_page, args=('country', ))

def render_sidebar(scope):

	st.sidebar.write('User : ' + '**' + scope.user_name + '**')
	st.sidebar.write('Campaign (November) : ' + '**' + str(scope.campaign) + '**')
	st.sidebar.write('Budget Version : ' + '**' + scope.budget_version + '**')
	
	st.sidebar.write('---------')

	previous_country = scope.selected_country

	print('previous_country = ', previous_country)

	print('Initial Load = ', scope.initial_load)

	if scope.initial_load:
		print('This is the initial load')
		scope.initial_load = False			# Prevent session_state from re-running during its use

		 
		scope.selected_country = st.sidebar.selectbox ( 
													label=('Country / Market'), 
													options=scope.dropdown_countries,
													# index=scope.dropdown_countries.index(scope.selected_country),
													index=0,
													# key='91',
													) 

	else:
		scope.selected_country = st.sidebar.selectbox ( 
													label=('Country / Market'), 
													options=scope.dropdown_countries,
													# key='91',
													) 

	if scope.selected_country != previous_country : 
		scope.page_to_display = 'targets'
	# 	print('Country has changed')
	# 	if scope.selected_country != 'select country / market':
	# 		print('Change Pages Here')
	# 		scope.page_to_display = 'targets'


	# set the current country if it has chnaged and render that page

	print ('Sidebar Page to display = ', scope.page_to_display)




	st.sidebar.write('---------')

	if scope.user_can_edit_forex_rates:
		st.sidebar.button('Forex Rates', on_click=set_page, args=('forex', ))
	if scope.user_can_edit_config:
		st.sidebar.button('System Settings', on_click=set_page, args=('config', ))


