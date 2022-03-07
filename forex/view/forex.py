import streamlit as st
import pandas as pd


from config.model.countries import country_dict
from forex.model.maintenance import forex_rates_maintenance
from forex.model.save import save_forex_rates

def view_forex(scope):

	st.header('Forex Maintenance Screen')
	
	copy_rates = False

	col1,col2,col3 = st.columns([1,9,2])

	with col1: 
		scope.campaign_forex = st.selectbox ( 
											label=('Available Campaigns'), 
											options=scope.dropdown_campaigns,
											# index=pos_of_campiagn - dont bother setting - user can work it out
											# key='campaign_forex_1', - dont add as it create another object in scope
											help='Select the campaign to view and edit the forex rates.',
											) 

	# check if the forex df contains any rates for the selected campaign
	if scope.campaign_forex not in scope.forex_df.campaign.values:
		with col3:
			copy_rates = st.button (
									label='Copy Previous Years Rates',
									help='Press to copy prior years rates into the current years - will not work if data already exists'
									)
			
		st.warning ('Forex Rates do not exist for ' + str(scope.campaign_forex) + ' campaign year')
	else:
		forex_rates_maintenance(scope)

	st.markdown("""---""")



	if copy_rates:
		# The COPY Button only appears if we do not have any rates for the selected forex campaign year
		
		new_forex_rates = pd.DataFrame
		current_campaign = int(scope.campaign_forex)
		prior_campaign = current_campaign - 1

		st.warning ('Attempting to add forex rates for ' + str(current_campaign) + ' to the forex dataset')
		
		new_forex_rates = scope.forex_df.loc[scope.forex_df['campaign'] == prior_campaign].copy()

		if new_forex_rates.empty:
			st.error('The ' + str(prior_campaign) + ' campaign does not contain any forex rates.')
			st.info('You can only copy from the immediately preceeding campaign year, which must contain some rates to copy.')
		else:
			st.success('Finished copying ' + str(prior_campaign) + ' forex rates. You now have a base set of rates for ' + str(current_campaign))
			new_forex_rates['campaign'] = current_campaign
			scope.forex_df = pd.concat([scope.forex_df, new_forex_rates])
			forex_rates_maintenance(scope)
			save_forex_rates(scope)


	if scope.campaign_forex in scope.forex_df.campaign.values:
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



