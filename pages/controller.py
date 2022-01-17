

from pages.view.welcome import view_project_welcome
# from pages.view.targets import view_targets
from targets.view.targets import view_targets
# from pages.view.comics import view_comics_star_wars

# from pages.view.cards import view_cards_star_wars





def render_selected_page(scope):
	
	page = scope.page_to_display
	print( 'Rendering > ', page)
	
	page_map = {
						'welcome'			:view_project_welcome,
						'targets'			:view_targets,
						# 'sw_cards'			:view_cards_star_wars,
						# 'dr_who'			:view_dr_who_dvds,

					}

	if page in list(page_map.keys()):
		page_map[page](scope)


