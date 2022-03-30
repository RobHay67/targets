
import streamlit as st

from config.model.currency import currency_name, currency_symbol
from config.model.regions import set_regions_for_country



def render_country_selector(scope):

	col1,col2,col3,col4 = st.columns([1,2,1,1])

	with col1:
			st.header('Target Rates')
			
	with col2:
			previous_country = scope.target_selected_country

			scope.target_selected_country = st.selectbox ( 
															label=('Available Countries'), 
															options=scope.dropdown_countries,
															# key='target_selected_country',
															help='Select the country to view and edit the rates.',
															) 

			if previous_country != scope.target_selected_country:
				set_regions_for_country(scope)

	with col3: 
		currency = currency_name(scope.target_selected_country)
		dollar_symbol = currency_symbol(scope.target_selected_country)

		st.write('Currency = ' + currency +' ( ' + dollar_symbol + ' )')
	with col4:
		scope.target_setting_method = st.selectbox(
														label='Budget By', 
														options=['Region', 'Country']
														)

	st.markdown("""---""")
