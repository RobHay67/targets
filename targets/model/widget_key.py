# import streamlit as st

from config.model.countries import country_key_from_name




def create_widget_key(scope, region, metric):

	payment_country = country_key_from_name(scope.user_selected_country)

	widget_key = 'widget_target_' + payment_country + '_' + region + '_' + scope.target_selected_tenure + '_' + metric

	return widget_key