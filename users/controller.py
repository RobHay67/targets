
from users.view.login import render_login_form
from users.view.users import render_user_maintenance




def login_page(scope):
	
	list_of_users = list(scope.user_df.index.values)
	
	render_login_form(scope, list_of_users)




def user_maintenance_page(scope):

	render_user_maintenance(scope)









