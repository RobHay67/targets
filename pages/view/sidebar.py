import streamlit as st


# from set_page import set_page
from config.model.page import set_page



# st.sidebar.button('Country', on_click=set_page, args=('country', ))

def render_sidebar(scope):
	st.sidebar.write('User : ' + 'Rob Hay')
	st.sidebar.write('Campaign (November) : ' + '2022')
	st.sidebar.write('Budget Version : ' + 'Version 1.0')
	
	st.sidebar.write('---------')


	previous_country = scope.selected_country

	scope.selected_country = st.sidebar.selectbox ( 
											label=('Country / Market'), 
											options=scope.dropdown_countries,
											# index=scope.dropdown_countries.index(previous_country), 
											key='91',
											) 

	print(scope.selected_country)

	if scope.selected_country != previous_country : 
		print('Country has changed')
		if scope.selected_country != 'select country / market':
			# scope.selected_country = scope.selected_country
			print('Change Pages Here')
			scope.page_to_display = 'targets'
		# set_refresh_charts_for_all_pages(scope)


	# set the current country if it has chnaged and render that page

	print (scope.page_to_display)




	st.sidebar.write('---------')
	st.sidebar.button('Config', on_click=set_page, args=('config', ))

