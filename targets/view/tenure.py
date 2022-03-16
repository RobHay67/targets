from hashlib import new
import streamlit as st



def render_tenure_selector(scope):

	scope.target_selected_tenure = st.selectbox ( 
												label=('Tenure Category'), 
												options=scope.dropdown_tenure,
												
												help='Select the tenure level to view and edit the rates.',
												# key='target_selected_tenure',
												) 





def render_new_fundraisers(scope):

	st.subheader(str(scope.target_selected_tenure) + ' Fundraises for ' + scope.selected_country)


	last_campaign = int(scope.campaign) - 1			# 2021
	this_campaign = int(scope.campaign)				# 2022
	tenure = scope.target_selected_tenure 			# > New
	country = scope.selected_country				# > Canada # TODO - we need country code for this - should be target_selected_tenure

	# TODO - who sets the selected_tenure vs the target_selected_tenure

	region = 'total'

	# TODO - factor in regions, if appropriate

	# Instantiate metrics for totals

	# we require these 4 metrics for new
	# scope.target_df

	# regos = scope.target_df.loc[(scope.target_df['payment_country'] == 'au')]
	# regos = scope.target_df.loc[(scope.target_df['payment_country'] == 'au') & (scope.target_df['region'] == 'total') & (scope.target_df['tenure'] == 'new') & (scope.target_df['metric'] == 'regos') ]
	
	
	
	# regos = scope.target_df.loc[(scope.target_df['payment_country'] == 'au') & (scope.target_df['region'] == 'total') & (scope.target_df['tenure'] == 'new') & (scope.target_df['metric'] == 'regos') ]['result'].values[0]
	# regos = scope.target_df['result'].loc[(scope.target_df['payment_country']=='au') & (scope.target_df['region']=='total') & (scope.target_df['tenure']=='new') & (scope.target_df['metric']=='regos') ]
	
	print (type(regos))
	print(regos)
	# regos = scope.target_df.loc[(scope.target_df['payment_country']=='au', ['region']=='total', ['tenure'] == 'new', ['metric'] == 'regos']]
	print('regos = ', regos)




	# regos = 
	# active = 
	# funds = 
	# apam = 

	# we will need to format the values as appropriate - so regos is and integer and apam is displayed as 2 decimal places, but is a float

	# they can serve as defaults for the current campaign, but only if the current campaign is missing these rates??

	# we need to create widgets with appropriate names

	# this should all be in a form - right????


	

	with st.form(key='new_form'):




		st.markdown("""---""")
		
		submit_button = st.form_submit_button(label='Save Changes for NEW Fundraisers')





