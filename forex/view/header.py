
import streamlit as st


from forex.model.maintenance import forex_rates_maintenance


def render_forex_header(scope, copy_rates):

	st.header('Forex Maintenance Screen')


	col1,col2,col3 = st.columns([1,9,2])

	with col1: 
		scope.campaign_forex = st.selectbox ( 
											label=('Available Campaigns'), 
											options=scope.dropdown_campaigns,
											# index=pos_of_campiagn - dont bother setting - user can work it out
											# key='campaign_forex_1', - dont add as it create another object in scope
											help='Select the campaign to view and edit the forex rates.',
											) 

	# check if the forex df contains any rates for the selected campaign, and 
	# add a copy from previous year button, if it does not

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



