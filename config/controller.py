

from config.model.streamlit import set_streamlit_page_config

from pages.view.welcome import view_project_welcome
from config.model.folders import scope_folders

from config.model.countries import scope_countries
from config.model.campaigns import scope_campaign
from config.model.users import scope_user
from config.model.version import scope_version

# user
# budget version
# campaign


def set_scope(scope):
	
	set_streamlit_page_config()					# should only run onetime

	if 'initial_load' not in scope:					
		scope.initial_load = True				# set the initial load state 
												# prevents this section from runnning again and
												# allows the ticker index to load next

		scope.loaded_data = False				# set default status as have not loaded the data at this stage
		# scope.campaign = 2022					# The campaign being forecast
		scope_campaign(scope)					# The campaign being forecast
		scope_user(scope)						# Store the current user details
		scope_version(scope)					# Store the current version number TODO: this might be changeable, but we need an initial version
		scope_countries(scope)					# add list of countries for selection


		# scope_app(scope)						# This contains all the application settings
		# scope_pages(scope)					# This contains all the page Specific settings
		scope_folders(scope)					# Required before we can attempt to load any data
		# scope_download(scope)

		view_project_welcome(scope)				# Render the home page

	if scope.initial_load:					# This will only run one time after the initial load has occured
		scope.initial_load = False			# Prevent session_state from re-running during its use


	return scope