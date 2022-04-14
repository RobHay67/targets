
import streamlit as st

from config.model.currency import currency_name, currency_symbol
# from config.model.regions import set_regions_for_country
from targets.model.update_values import on_change_country, on_change_target_setting_method
from targets.view.widgets import render_country_selector, render_target_setting_method


def render_targets_header(scope):

	col1,col2,col3,col4 = st.columns([1,2,1,1])

	with col1:
			st.header('Target Rates')
	with col2:

		render_country_selector(scope)

			# list_of_countries = scope.dropdown_countries
			# index_pos = list_of_countries.index(scope.user_selected_country)
			# scope.user_selected_country = st.selectbox ( 
			# 												label=('Available Countries'), 
			# 												options=list_of_countries,
			# 												index=index_pos,
			# 												key='widget_target_selected_country',
			# 												help='Select the country to view and edit the rates.',
			# 												on_change=on_change_country,
			# 												args=(scope, ),
			# 												) 

			# if previous_country != scope.user_selected_country:
			# 	set_regions_for_country(scope)

	with col3: 
		currency = currency_name(scope.user_selected_country)
		dollar_symbol = currency_symbol(scope.user_selected_country)

		st.write('Currency = ' + currency +' ( ' + dollar_symbol + ' )')
	with col4:

		render_target_setting_method(scope)

		# select_box_options = ['Region', 'Country']
		# index_pos = select_box_options.index(scope.user_target_setting_method)

		# scope.user_target_setting_method = st.selectbox(
		# 												label='Budget By', 
		# 												options=select_box_options,
		# 												index=index_pos,
		# 												key='widget_target_setting_method',
		# 												on_change=on_change_target_setting_method,
		# 												args=(scope, ),
		# 												)

	st.markdown("""---""")


def tenure_group_header(scope):

	if scope.target_selected_tenure == 'Foundation':
		header_string = (str(scope.target_selected_tenure) + ' Donors')
	else:
		header_string = (str(scope.target_selected_tenure) + ' Fundraisers')


	return header_string