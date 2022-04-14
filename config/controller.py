from config.model.streamlit import set_streamlit_page_config
from config.model.campaigns import scope_campaign
from users.model.scope import scope_user
from config.model.version import scope_version
from config.model.countries import scope_countries
from config.model.folders import scope_folders
from config.model.target_rates import scope_target
from config.model.tenure import scope_tenure


from users.model.load import load_user_table
from targets.model.load import load_target_rates

from config.model.forex_rates import load_forex_rates

def set_scope(scope):
	
	set_streamlit_page_config()					# should only run onetime

	if 'initial_load' not in scope:					
		scope.initial_load = True				# set the initial load state 
												# prevents this section from runnning again and
												# allows the ticker index to load next

		scope.loaded_data = False				# set default status as have not loaded the data at this stage

		scope.page_to_display = 'login'			# page to display on initial load

		scope_campaign(scope)					# The campaign being forecast
		scope_user(scope)						# Store the current user details
		scope_version(scope)					# Store the current version number TODO: this might be changeable, but we need an initial version
		scope_countries(scope)					# add list of countries for selection
		scope_folders(scope)					# Required before we can attempt to load any data
		scope_target(scope)						# Set some target setting params
		scope_tenure(scope)						# establish the tenure levels and defaults

	if scope.initial_load:						# This will only run one time after the initial load has occured
		load_user_table(scope)						# Load the user for this application 
		load_target_rates(scope)				# Load the target rates file > campaign = scope.campaign
		load_forex_rates(scope)					# Load the forex rates
		scope.initial_load = False				# Prevent session_state from re-running during its use


	return scope