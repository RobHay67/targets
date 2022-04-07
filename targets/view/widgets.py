
import streamlit as st

from targets.model.widget_key import create_widget_key
from targets.model.can_edit import is_column_editable

from targets.model.update_values import on_change_regos
from targets.model.update_values import on_change_active_regos
from targets.model.update_values import on_change_apam
from targets.model.update_values import on_change_funds
from targets.model.update_values import on_change_donations
from targets.model.update_values import on_change_ada
from targets.model.update_values import on_change_country
from targets.model.update_values import on_change_target_setting_method
from targets.model.update_values import on_change_target_selected_tenure


from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from config.model.countries import country_key_from_name





def render_regos_widget(scope, region):

	col_name = 'Registrations'
	metric = 'regos'
	widget_key = create_widget_key(scope, region, metric)

	editable_column = is_column_editable(scope, region)
	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label=col_name, 
														value=scope.target_rates[region][metric], 
														format="%.0i", # format="%.0f",
														step=1.0,
														on_change=on_change_regos,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write(col_name)
		st.markdown(format_regos(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		st.write('')
		st.write('')




def render_active_widget(scope, region):

	col_name = 'Active Registrations'
	metric = 'active'
	widget_key = create_widget_key(scope, region, metric)

	editable_column = is_column_editable(scope, region)
	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label=col_name, 
														value=scope.target_rates[region][metric], 
														format="%.0f", # format="%.0f",
														step=1.0,
														on_change=on_change_active_regos,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write(col_name)
		st.markdown(format_regos(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		st.write('')
		st.write('')



def render_apam_widget(scope, region):

	col_name = 'APAM - Average Per Active Mo'
	metric = 'apam'
	widget_key = create_widget_key(scope, region, metric)
	editable_column = is_column_editable(scope, region)

	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label=col_name, 
														value=scope.target_rates[region][metric], 
														format="%.2f", # format="%.0f",
														step=0.01,
														on_change=on_change_apam,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write(col_name)
		st.markdown(format_dolls(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		st.write('')
		st.write('')


def render_funds_widget(scope, region):

	col_name = 'Funds Raised'
	metric = 'funds'
	widget_key = create_widget_key(scope, region, metric)
	editable_column = is_column_editable(scope, region)

	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label=col_name, 
														value=scope.target_rates[region][metric], 
														format='%.2f', # format="%.0f",
														step=1.0,
														on_change=on_change_funds,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write(col_name)
		st.markdown(format_dolls(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		st.write('')
		st.write('')



def render_donations_widget(scope, region):

	col_name = 'Donations'
	metric = 'donations'
	widget_key = create_widget_key(scope, region, metric)

	editable_column = is_column_editable(scope, region)
	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label=col_name, 
														value=scope.target_rates[region][metric], 
														format="%.0i", # format="%.0f",
														step=1.0,
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
	editable_column = is_column_editable(scope, region)

	if editable_column:
		scope.target_rates[region][metric] = st.number_input(
														label=col_name, 
														value=scope.target_rates[region][metric], 
														format="%.2f", # format="%.0f",
														step=0.01,
														on_change=on_change_ada,
														args=(scope, region, ),
														key=(widget_key)
														)
	else:
		st.write(col_name)
		st.markdown(format_dolls(scope.target_rates[region][metric], align='left'), unsafe_allow_html=True)
		st.write('')
		st.write('')


def render_country_selector(scope):

	list_of_countries = scope.dropdown_countries
	index_pos = list_of_countries.index(scope.target_selected_country)
	scope.target_selected_country = st.selectbox ( 
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
	
	index_pos = select_box_options.index(scope.target_setting_method)

	scope.target_setting_method = st.selectbox(
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