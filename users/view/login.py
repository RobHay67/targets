
import streamlit as st



def render_login_form(scope):

	col1,col2 = st.columns([2,8])
	
	with col1:
		st.header('Login to Target Setting Application')

		login_name = st.text_input('User Name (movember email address)')
		login_pword = st.text_input('Password', type='password')

		login_button = st.button('login')


	return login_button, login_name, login_pword




def login_message(login_name, status):

	if status == 'logged_in':
		st.success(login_name + ' Logged In')

	if status == 'invalid_pword':
		st.error('Password is invalid for ' + login_name)

	if status == 'invalid_user':
		st.error('User Name ' + login_name + ' does not exist')