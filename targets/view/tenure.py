from hashlib import new
import streamlit as st


# from config.model.tenure import tenure_levels






def render_tenure_selector(scope):

	scope.target_selected_tenure = st.selectbox ( 
												label=('Tenure Category'), 
												options=scope.dropdown_tenure,
												
												help='Select the tenure level to view and edit the rates.',
												# key='target_selected_tenure',
												) 


	if scope.target_selected_tenure == 'New':
		render_new_fundraisers

	if scope.target_selected_tenure == 'Returned':
		print('Render the Returned variables right here')
	

	if scope.target_selected_tenure == 'Returning':
		print('Render the Returning variables right here')

	if scope.target_selected_tenure == 'Foundation':
		print('Render the Foundation variables right here')


def render_new_fundraisers(scope):



	if scope.target_selected_tenure == 'Foundation':
		header_string = (str(scope.target_selected_tenure) + ' Donations')
	else:
		header_string = (str(scope.target_selected_tenure) + ' Fundraisers')

	

	last_campaign = int(scope.campaign) - 1			# 2021
	this_campaign = int(scope.campaign)				# 2022

	# campaigns 2			ok	scope.campaign	
	# country	1			ok	target_selected_country
	# tenure	1			ok 	target_selected_tenure
	# regions	multiple	ok	target_regions
	# metrics	multiple		hard coded
	# values	multiple		hard coded


	# payment_country = country_key_from_name(scope.target_selected_country)

	no_of_columns = len(scope.target_regions)
	




	# Update Values Section

	with st.form(key='new_form'):
		st.subheader(header_string)

		cols = st.columns(no_of_columns)
		
		for i, col in enumerate(cols):
			print(i)
			print(scope.target_regions[i])

			col.write('**'+scope.target_regions[i]+'**')


		# st.markdown("""---""")
		
		submit_button = st.form_submit_button(label='Save Changes for NEW Fundraisers')

	# st.slider(label='Active Fundraisers', value=50, key='this')

	# Instantiate metrics for totals

	# we require these 4 metrics for NEW Fundraisers
	# regos = 
	# active = 
	# funds = 
	# apam = 

	# Prior Year Values
	
	st.subheader('Last Years Values')

	cols = st.columns(no_of_columns)

	for i, col in enumerate(cols):
		col.write('**'+scope.target_regions[i]+'**')






	# 	st.write('This is something')

	# TODO this method will only work if all the values are there!!

	regos = int(scope.target_df.loc[  
								  (scope.target_df['payment_country'] 	== 'au') 
								& (scope.target_df['region'] 			== 'total') 
								& (scope.target_df['tenure'] 			== 'new') 
								& (scope.target_df['metric'] 			== 'regos') 
								]['result'].values[0])




	# we will need to format the values as appropriate - so regos is and integer and apam is displayed as 2 decimal places, but is a float

	# they can serve as defaults for the current campaign, but only if the current campaign is missing these rates??

	# we need to create widgets with appropriate names

	# this should all be in a form - right????


	

	





