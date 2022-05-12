
import streamlit as st

from targets.model.widget_key import create_widget_key
from targets.model.can_edit import is_widget_editable

from targets.model.update_values import on_change_regos
from targets.model.update_values import on_change_active_regos
from targets.model.update_values import on_change_apam
from targets.model.update_values import on_change_funds
from targets.model.update_values import on_change_donations
from targets.model.update_values import on_change_ada
from targets.model.update_values import on_change_country
from targets.model.update_values import on_change_target_setting_method
from targets.model.update_values import on_change_target_selected_tenure
from targets.model.update_values import on_change_comment


from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from config.model.countries import country_key_from_name
from targets.model.format_values import format_regos, format_dolls, format_percent, format_string


def render_comment(scope, region):
	col_name = 'Comments'
	metric = 'comment'
	widget_key = create_widget_key(scope, region, metric)
	widget_value = scope.target_rates[region][metric]
	editable_column = is_widget_editable(scope, region)

	
	if editable_column:
		scope.target_rates[region][metric] = st.text_input(
															label='',
															value=widget_value, 
															on_change=on_change_comment,
															max_chars=500,
															args=(scope, region, ),
															key=(widget_key)
															)
	else:
		st.write('')
		st.write('')
		st.markdown(format_string(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		# st.write('this is a comment')




def render_prior_regos(scope, region):
	st.write('')
	st.write('')
	st.markdown(format_regos(scope.target_rates[region]['regos_total_prior'], align='left'), unsafe_allow_html=True)
	

def render_regos_widget(scope, region):

	col_name = 'Registrations'
	metric = 'regos'
	widget_key = create_widget_key(scope, region, metric)
	widget_value = int(scope.target_rates[region][metric])
	widget_step = int(widget_value * .05)
	editable_column = is_widget_editable(scope, region)

	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label='',
														min_value=0,
														value=widget_value, 
														format="%.0i", # format="%.0f",
														step=widget_step,
														on_change=on_change_regos,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write('')
		st.write('')
		st.markdown(format_regos(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		

def render_active_widget(scope, region):

	col_name = 'Active Registrations'
	metric = 'active'
	widget_key = create_widget_key(scope, region, metric)
	widget_value = int(scope.target_rates[region][metric])
	widget_step = int(widget_value * .05)
	# Cannot exceed the registrations number
	widget_max_value = int(scope.target_rates[region]['regos'])

	editable_column = is_widget_editable(scope, region)
	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label='',
														min_value=0,
														max_value=widget_max_value,
														value=int(scope.target_rates[region][metric]), 
														format="%.0i", # format="%.0f",
														step=widget_step,
														on_change=on_change_active_regos,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write('')
		st.write('')
		st.markdown(format_regos(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		

def render_apam_widget(scope, region):

	col_name = 'APAM - Average Per Active Mo'
	metric = 'apam'
	widget_key = create_widget_key(scope, region, metric)
	widget_value = float(scope.target_rates[region][metric])
	widget_step = round((widget_value * .05), 2)
	editable_column = is_widget_editable(scope, region)

	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label='',
														min_value=0.0,
														value=widget_value, 
														format="%.2f", # format="%.0f",
														step=widget_step,
														on_change=on_change_apam,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write('')
		st.write('')
		st.markdown(format_dolls(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)


def render_funds_widget(scope, region):

	col_name = 'Funds Raised'
	metric = 'funds'
	widget_key = create_widget_key(scope, region, metric)
	widget_value=float(scope.target_rates[region][metric])
	widget_step = round((widget_value * .05), 2)
	editable_column = is_widget_editable(scope, region)

	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label='', 
														min_value=0.0,
														value=widget_value, 
														format="%.2f", # format="%.0f",
														step=widget_step,
														on_change=on_change_funds,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write('')
		st.write('')
		st.markdown(format_dolls(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)


def render_active_ratio(scope, region):
	
	rates = scope.target_rates[region]
	active_ratio = 0.0

	if rates['regos'] != 0:
		active_ratio = rates['active'] / rates['regos']

	st.write('')
	st.write('')
	st.markdown(format_percent(active_ratio, align='center'), unsafe_allow_html=True)


def render_retention_ratio(scope, region):

	rates = scope.target_rates[region]
	retention_ratio = 0.0

	if rates['regos'] != 0:
		retention_ratio = rates['regos'] / rates['regos_total_prior']

	st.write('')
	st.write('')
	st.markdown(format_percent(retention_ratio, align='center'), unsafe_allow_html=True)
	


def render_donations_widget(scope, region):

	col_name = 'Donations'
	metric = 'donations'
	widget_key = create_widget_key(scope, region, metric)
	widget_value = int(scope.target_rates[region][metric])
	widget_step = int(widget_value * .05)
	editable_column = is_widget_editable(scope, region)
	
	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label='', 
														value=widget_value, 
														format="%.0i", # format="%.0f",
														step=widget_step,
														on_change=on_change_donations,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write(col_name)
		st.markdown(format_regos(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		st.write('')
		st.write('')


def render_ada_widget(scope, region):

	col_name = 'ADA - Average Donation Amount'
	metric = 'ada'
	widget_key = create_widget_key(scope, region, metric)
	widget_value = float(scope.target_rates[region][metric])
	widget_step = round(widget_value * .05,2)
	editable_column = is_widget_editable(scope, region)

	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label='', 
														value=widget_value, 
														format="%.2f", # format="%.0f",
														step=widget_step,
														on_change=on_change_ada,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write(col_name)
		st.markdown(format_dolls(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		st.write('')
		st.write('')


# Selectors at the top of each tenure page

def render_country_selector(scope):

	list_of_countries = scope.dropdown_countries
	index_pos = list_of_countries.index(scope.user_selected_country)
	scope.user_selected_country = st.selectbox ( 
													label=('Available Countries'), 
													options=list_of_countries,
													index=index_pos,
													key='widget_target_selected_country',
													help='Select the country to view and edit the rates.',
													on_change=on_change_country,
													args=(scope, ),
													) 


def render_target_setting_method(scope):

	select_box_options = ['Region', 'Country']
	
	index_pos = select_box_options.index(scope.user_target_setting_method)

	scope.user_target_setting_method = st.selectbox(
													label='Budget By', 
													options=select_box_options,
													index=index_pos,
													key='widget_target_setting_method',
													on_change=on_change_target_setting_method,
													args=(scope, ),
													)


def render_tenure_selector(scope):

	col1,col2 = st.columns([1,3])

	select_box_options = scope.dropdown_tenure

	index_pos = select_box_options.index(scope.target_selected_tenure)

	with col1:

		scope.target_selected_tenure = st.selectbox ( 
													label=('Tenure Category'), 
													options=select_box_options,
													index=index_pos,
													help='Select the tenure level to view and edit the rates.',
													key='widget_target_selected_tenure',
													on_change=on_change_target_selected_tenure,
													args=(scope, ),
													) 



# target_base_rates  {'NSW': {'regos': 4250.0, 'active': 2682.0, 'funds': 1597072.14, 'apam': 595.48, 'regos_total_prior': 23955.0, 'regos_total_curnt': 17874.0}, 'VIC': {'regos': 3863.0, 'active': 2510.0, 'funds': 1673736.29, 'apam': 666.83, 'regos_total_prior': 18709.0, 'regos_total_curnt': 16967.0}, 'QLD': {'regos': 3543.0, 'active': 2340.0, 'funds': 1370539.65, 'apam': 585.7, 'regos_total_prior': 15814.0, 'regos_total_curnt': 15704.0}, 'WA': {'regos': 1687.0, 'active': 1119.0, 'funds': 680258.23, 'apam': 607.92, 'regos_total_prior': 7719.0, 'regos_total_curnt': 7981.0}, 'SA': {'regos': 1031.0, 'active': 672.0, 'funds': 340362.75, 'apam': 506.49, 'regos_total_prior': 4887.0, 'regos_total_curnt': 5278.0}, 'ACT': {'regos': 431.0, 'active': 281.0, 'funds': 159398.1, 'apam': 567.25, 'regos_total_prior': 2198.0, 'regos_total_curnt': 1589.0}, 'TAS': {'regos': 383.0, 'active': 270.0, 'funds': 149503.3, 'apam': 553.72, 'regos_total_prior': 1566.0, 'regos_total_curnt': 1596.0}, 'NT': {'regos': 96.0, 'active': 55.0, 'funds': 31396.71, 'apam': 570.85, 'regos_total_prior': 668.0, 'regos_total_curnt': 563.0}, 'Other': {'regos': 2212.0, 'active': 1558.0, 'funds': 900335.56, 'apam': 577.88, 'regos_total_prior': 22074.0, 'regos_total_curnt': 51821.0}, 'Total': {'regos': 17496.0, 'active': 11487.0, 'funds': 6902602.73, 'apam': 600.91, 'regos_total_prior': 97590.0, 'regos_total_curnt': 119373.0}}
# target_rates       {'NSW': {'regos': 4250.0, 'active': 2682.0, 'funds': 1597072.14, 'apam': 595.48, 'regos_total_prior': 23955.0, 'regos_total_curnt': 17874.0}, 'VIC': {'regos': 3863.0, 'active': 2510.0, 'funds': 1673736.29, 'apam': 666.83, 'regos_total_prior': 18709.0, 'regos_total_curnt': 16967.0}, 'QLD': {'regos': 3543.0, 'active': 2340.0, 'funds': 1370539.65, 'apam': 585.7, 'regos_total_prior': 15814.0, 'regos_total_curnt': 15704.0}, 'WA': {'regos': 1687.0, 'active': 1119.0, 'funds': 680258.23, 'apam': 607.92, 'regos_total_prior': 7719.0, 'regos_total_curnt': 7981.0}, 'SA': {'regos': 1031.0, 'active': 672.0, 'funds': 340362.75, 'apam': 506.49, 'regos_total_prior': 4887.0, 'regos_total_curnt': 5278.0}, 'ACT': {'regos': 431.0, 'active': 281.0, 'funds': 159398.1, 'apam': 567.25, 'regos_total_prior': 2198.0, 'regos_total_curnt': 1589.0}, 'TAS': {'regos': 383.0, 'active': 270.0, 'funds': 149503.3, 'apam': 553.72, 'regos_total_prior': 1566.0, 'regos_total_curnt': 1596.0}, 'NT': {'regos': 96.0, 'active': 55.0, 'funds': 31396.71, 'apam': 570.85, 'regos_total_prior': 668.0, 'regos_total_curnt': 563.0}, 'Other': {'regos': 2212.0, 'active': 1558.0, 'funds': 900335.56, 'apam': 577.88, 'regos_total_prior': 22074.0, 'regos_total_curnt': 51821.0}, 'Total': {'regos': 17496.0, 'active': 11487.0, 'funds': 6902602.73, 'apam': 600.91, 'regos_total_prior': 97590.0, 'regos_total_curnt': 119373.0}}
