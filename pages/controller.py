

# from pages.view.welcome import view_project_welcome
from forex.view.forex import view_forex
from targets.view.targets import view_targets





def render_selected_page(scope):
	
	page = scope.page_to_display
	# print( 'Rendering > ', page)
	
	page_map = {
						# 'welcome'			:view_project_welcome,
						'targets'			:view_targets,
						'forex'				:view_forex

					}

	if page in list(page_map.keys()):
		page_map[page](scope)


