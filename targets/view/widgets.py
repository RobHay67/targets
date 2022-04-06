
import streamlit as st

from targets.model.widget_key import create_widget_key
from targets.model.can_edit import is_column_editable

from targets.model.update_values import on_change_regos, on_change_active_regos, on_change_apam, on_change_funds, on_change_donations, on_change_ada
from targets.model.format_values import format_regos, format_dolls, format_percent, format_string



# rates = scope.target_rates[region]


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