
# ------------------------------------------------- Execute Application
# streamlit run app.py
# ------------------------------------------------- GitHub
# git push -u origin <branch>
# ------------------------------------------------- Pipenv
# cd into project folder 
# activate Pipenv 	- pipenv shell
# deactivate env	- exit
# add a package 	- pipenv install django
# specify ver   	- pipenv install django==2.2
# latest ver		- pipenv update pandas
# delete pkg		- pipenv uninstall django

# ------------------------------------------------- Package Management
# pip3 install --user --upgrade django
# pipenv install flask==0.12.1
# pipenv install mplfinance===0.12.7a5
# ------------------------------------------------- 

# Testing Code - TODO - delete later
import pandas as pd
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


import streamlit as st



from config.controller import set_scope
from pages.view.sidebar import render_sidebar
from pages.controller import render_selected_page

print ( '\033[94m' + 'Target Setting App Re-Rendering Now ' + '>'*50 + '\033[0m')
scope = set_scope(st.session_state)
render_sidebar(scope)						# Render the Sidebar
render_selected_page(scope)					# Render the selected Page





print('-'*100)
print( 'List of all keys in the st.session_state')
print('-'*100)
if 'initial_load' in st.session_state:
	to_much_data = ['target_df', 'forex_df', 'forex_rates', 'forex_rates_for_view', 'country_code_list']
	folders_and_paths = ['folder_files', 'folder_project', 'path_forex_file', 'path_target_file']
	status_vars = ['initial_load', 'loaded_data', 'loaded_forex_table', 'loaded_target_table']
	dropdowns = ['dropdown_campaigns','dropdown_tenure']

	ignore_params = to_much_data + folders_and_paths +  status_vars + dropdowns
	for key in sorted(st.session_state):
		if key not in  ignore_params:
			print ( key.ljust(40), scope[key])
		# else:
		# 	print ( key.ljust(40), 'too much data to print')
		# print(scope[key])
print ( '-'*100)
















# # Set Up the Initial Streamlit Environment ======================================================================
# from config.streamlit import set_streamlit_page_config
# from scope.scope import set_scope
# from pages.controller import set_initial_scope
# from scope.dropdowns.refresh_selectors import update_dropdowns


# set_streamlit_page_config()
# scope = set_scope(st.session_state, project_description)

# if scope.dropdown_lists_need_updating: 
# 	update_dropdowns(scope)

# print ( '\033[94mApplication Refreshed >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \033[0m')

# render_selected_page(scope)
# render_sidebar(scope)













