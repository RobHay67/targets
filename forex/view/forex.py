import streamlit as st
import pandas as pd


from config.model.countries import country_dict
from config.model.forex_rates import save_forex_rates

def view_forex(scope):
	st.header('Forex Maintenance Screen')
	
	
	# previous_campaign = scope.campaign_forex
	copy_rates = False

	col1,col2,col3 = st.columns([1,9,2])

	with col1: 
		scope.campaign_forex = st.selectbox ( 
											label=('Available Campaigns'), 
											options=scope.dropdown_campaigns,
											# index=default_campaign,
											key='campaign_forex_1',
											help='Select the campaign to view and edit the forex rates.',
											) 

	# check if the forex df contains any rates for the selected campaign
	if scope.campaign_forex not in scope.forex_rates.campaign.values:
		with col3:
			copy_rates = st.button (
									label='Copy Previous Years Rates',
									help='Press to copy prior years rates into the current years - will not work if data already exists'
									)
			
		st.warning ('Forex Rates do not exist for this campaign year')


	st.markdown("""---""")



	if copy_rates:
		# Button only appears if we do not have any rates for the selected campaign year
		
		new_forex_rates = pd.DataFrame

		current_campaign = int(scope.campaign_forex)
		prior_campaign = current_campaign - 1

		st.warning ('Attempting to add forex rates for ' + str(current_campaign) + ' to the forex dataset')
		
		new_forex_rates = scope.forex_rates.loc[scope.forex_rates['campaign'] == prior_campaign].copy()

		if new_forex_rates.empty:
			st.error('The ' + str(prior_campaign) + ' campaign does not contain any forex rates.')
			st.info('You can only copy from the immediately preceeding campaign year, which must contain some rates to copy.')
		else:
			st.success('Finished copying ' + str(prior_campaign) + ' forex rates. You now have a base set of rates for ' + str(current_campaign))
			new_forex_rates['campaign'] = current_campaign
			scope.forex_rates = pd.concat([scope.forex_rates, new_forex_rates])
		

	# Display the appropriate rates
	# TODO - we need to add a save somehow??
	# TODO - lets put this into a form


		









	with st.form(key='my_form'):
		text_input = st.text_input(label='Forex Rates for all Countries')

		

		for i, row in scope.forex_rates.iterrows():
			if row['campaign'] == scope.campaign_forex:
				# print('i =', i)
				# print('row = ', row)

				key_country = row['country']

				

				country_code = row['country']
				country_name = country_dict[country_code]['country_name']
				currency 	= country_dict[country_code]['currency_name']
				dollar_symbol = country_dict[country_code]['currency_symbol']

				sub_value = 'sub_'+country_code

				col1,col2,col3,col4 = st.columns([3,3,3,3])

				with col1: 
					st.subheader(country_name)
					st.write('Local Currency = ' + currency +' ( ' + dollar_symbol + ' )')

				with col2: 
					sub_value = st.number_input(label='Rate to convert Local to Subsidiary', value=row['forex_to_sub'], format="%.7f", step=0.0000001, key=('sub_'+country_code))

				with col3: 
					st.number_input(label='Rate to convert Subsidiary to AUD', value=row['forex_to_aud'], format="%.7f", step=0.0000001, key='aud_'+country_code)
			
				st.markdown("""---""")


		submit_button = st.form_submit_button(label='Save Changes to Forex Rates Table')

		if submit_button:
			print(scope.forex_rates)
			print('we are saving here')
			save_forex_rates(scope)



	





