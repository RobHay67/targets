
import this
from users.view.login import render_login_form, login_message
from users.model.scope import set_user_access
from pages.view.sidebar import render_sidebar
from users.view.users import render_user_maintenance


def login_page(scope):
	
	list_of_users = list(scope.user_df.index.values)
	
	login_button, login_name, login_pword = render_login_form(scope)

	if login_button:

		if login_name in list_of_users:

			user_pword = scope.user_df.loc[login_name].at['pword']

			if login_pword == user_pword:
				login_message(login_name, 'logged_in')
				set_user_access(scope, login_name)
				# render_sidebar(scope)
			else:
				login_message(login_name, 'invalid_pword')
		else:
			login_message(login_name, 'invalid_user')




def user_maintenance_page(scope):

	render_user_maintenance(scope)









