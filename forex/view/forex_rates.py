import streamlit as st

from config.model.countries import country_dict
from forex.model.save import save_forex_rates


def render_forex_rates(scope):

	st.subheader(str(scope.campaign_forex) + ' Forex Rates for all Countries')
	with st.form(key='my_form'):
		for country_code in scope.country_code_list:
			country_name = country_dict[country_code]['country_name']
			currency = country_dict[country_code]['currency_name']
			dollar_symbol = country_dict[country_code]['currency_symbol']

			col1,col2,col3,col4 = st.columns([3,3,3,3])

			with col1: 
				st.subheader(country_name)
				st.write('Local Currency = ' + currency +' ( ' + dollar_symbol + ' )')

			with col2: 
				widget_key_sub = 'widget_forex_rate_' + country_code + '_sub'
				scope.forex_rates_maintenance[country_code]['sub'] = st.number_input(
																					label='Rate to convert Local to Subsidiary', 
																					value=scope.forex_rates_maintenance[country_code]['sub'], 
																					format="%.7f", 
																					step=0.0000001, 
																					key=(widget_key_sub)
																					)

			with col3: 
				widget_key_aud = 'widget_forex_rate_' + country_code + '_aud'
				scope.forex_rates_maintenance[country_code]['aud'] = st.number_input(
																					label='Rate to convert Subsidiary to AUD', 
																					value=scope.forex_rates_maintenance[country_code]['aud'], 
																					format="%.7f", 
																					step=0.0000001, 
																					key=(widget_key_aud)
																					)
		
			st.markdown("""---""")
		submit_button = st.form_submit_button(label='Save Changes to Forex Rates Table')

	if submit_button:
		print('we are saving here')
		save_forex_rates(scope)