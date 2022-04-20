
import streamlit as st

from users.model.scope import set_user_access



def render_login_form(scope, list_of_users):

	col1,col2 = st.columns([2,8])
	
	with col1:

		st.header('Login to Target Setting Application')

		login_name = st.text_input('User Name (movember email address)')
		login_pword = st.text_input('Password', type='password')
		
		if login_name in list_of_users:
			user_pword = scope.user_df.loc[login_name].at['pword']

			if login_pword == user_pword:
				st.button(	
							'login', 
							on_click=set_user_access, 
							args=(scope, login_name, ), 
							key='login_button',
							)
			else:
				if login_pword != '':
					login_message(login_name, 'invalid_pword')
		else:
			if login_name != '':
				login_message(login_name, 'invalid_user')








def login_message(login_name, status):

	if status == 'logged_in':
		st.success(login_name + ' Logged In')

	if status == 'invalid_pword':
		st.error('Password is invalid for ' + login_name)

	if status == 'invalid_user':
		st.error('User Name ' + login_name + ' does not exist')