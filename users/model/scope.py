from re import S
import pandas as pd
import os
import streamlit as st

from config.model.countries import country_dict



def scope_user(scope:dict):
	
	scope.page_to_display = 'login'

	scope.user_name = 'Login to Use the Application'
	# scope.user_pword = None
	# Access to which Countries
	scope.user_country_codes = []
	# User can make changes to the Targets
	scope.user_can_edit_targets = False
	# Special Admin Settings
	scope.user_can_see_total_movember = False
	scope.user_can_edit_forex_rates = False
	# For the Insights team so we can set specal params - maybe finance
	scope.user_can_edit_previous_rates = False
	scope.user_can_edit_config = False
	scope.user_can_edit_users = False
	scope.user_can_download_rates_table = False

	# User Specific Settings
	scope.user_selected_country = None
	scope.user_target_setting_method = None



def set_user_access(scope:dict, login_name:str):
	
	scope.page_to_display = 'welcome'

	scope.user_name = login_name
	# scope.user_pword = None

	# User can make changes to the Targets
	scope.user_can_edit_targets = scope.user_df.loc[login_name].at['can_edit_targets']
	
	# Special Admin Settings
	scope.user_can_see_total_movember = scope.user_df.loc[login_name].at['can_see_total_movember']
	scope.user_can_edit_forex_rates = scope.user_df.loc[login_name].at['can_edit_forex_rates']
	
	# For the Insights team so we can set specal params - maybe finance
	scope.user_can_edit_previous_rates = scope.user_df.loc[login_name].at['can_edit_previous_rates']
	scope.user_can_edit_config = scope.user_df.loc[login_name].at['can_edit_config']
	scope.user_can_edit_users = scope.user_df.loc[login_name].at['can_edit_users']
	scope.user_can_download_rates_table = scope.user_df.loc[login_name].at['can_download_rates_table']

	# User Specific Settings
	scope.user_selected_country = scope.user_df.loc[login_name].at['selected_country']
	scope.user_target_setting_method = scope.user_df.loc[login_name].at['target_setting_method']


	# Access to which Countries
	country_codes = scope.user_df.loc[login_name].at['country_codes']
	country_code_list = country_codes.split()
	scope.user_country_codes = country_code_list

	dropdown_list = []

	if 'all' in scope.user_country_codes:
		# Add every country to the list of dropdown_list countries (not total Movember)
		for key in scope.country_code_list:
			country_name = country_dict[key]['country_name']
			dropdown_list.append(country_name)
	else:
		# Add specific countries to the dropdown_list
		for country in scope.user_country_codes:
			# prevent access to total Movember - this is 
			# handled by scope.user_can_see_total_movember
			if country in country_dict.keys():
				country_name = country_dict[country]['country_name']
				dropdown_list.append(country_name)


	# Add Total_Movember to the dropdown list if user has this privaledge
	if scope.user_can_see_total_movember:
		country_name = country_dict['all']['country_name']
		dropdown_list.insert(0, country_name)

	scope.dropdown_countries = dropdown_list




















# This was the testing code
# def scope_user(scope):
# 	scope.user_name = 'Rob Hay'
# 	scope.user_pword = 'password'
	
# 	# scope.user_country_codes = ['ca', 'au', 'be']			# List of Countries the User can See or Edit
# 	scope.user_country_codes = ['au']
# 	# scope.user_country_codes = ['all']			# lowercase all just to be safe

# 	scope.user_can_edit_targets = True				# User can make changes to the Targets

# 	# Special Admin Code
# 	scope.user_can_see_total_movember = False
# 	scope.user_can_edit_forex_rates = True

# 	# This will be just for the Insights team so we can set specal params - maybe finance
# 	scope.user_can_edit_previous_rates = True
# 	scope.user_can_edit_config = True