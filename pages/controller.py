

from targets.controller import view_targets
from forex.controller import view_forex
# from targets.model.export import export_rates_df





def render_selected_page(scope):
	
	page = scope.page_to_display
	# print( 'Rendering > ', page)
	
	page_map = {
						# 'welcome'			:view_project_welcome,
						'targets'			:view_targets,

						'forex'				:view_forex,

						# 'export_rates'		:export_rates_df,

					}

	if page in list(page_map.keys()):
		page_map[page](scope)


