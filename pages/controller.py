

from targets.controller import view_targets
from forex.controller import view_forex
from users.controller import login_page, user_maintenance_page
from pages.view.welcome import render_welcome



def render_selected_page(scope):
	
	page = scope.page_to_display
	print( 'Rendering > ', page)
	
	page_map = {
						# 'welcome'			:view_project_welcome,
						'targets'			:view_targets,

						'forex'				:view_forex,

						'login'				:login_page,

						'users'				:user_maintenance_page,

						'welcome'			:render_welcome,

					}

	if page in list(page_map.keys()):
		page_map[page](scope)


