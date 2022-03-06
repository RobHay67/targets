

import streamlit as st


from targets.model.format_values import format_regos, format_dolls, format_percent

# TODO - scope.user_can_edit_targets - need to check this is True before allowing edits


from config.model.currency import currency_name, currency_symbol




def view_targets(scope):

	# st.subheader('Mo.com Target Setting Application')
	# st.write('Peer to Peer Fundraisers and Foundation Donations ( Mo.com )')
	# st.write('For the Financial Year period 1 May ' + str(scope.campaign) + ' to 30 April ' + str(scope.campaign + 1))




	currency = currency_name(scope.selected_country)
	dollar_symbol = currency_symbol(scope.selected_country)

	# st.title(scope.selected_country)
	# st.write('Currency = ' + currency +' ( ' + dollar_symbol + ' )')

	col1,col2 = st.columns([4,2])

	with col1: st.header(scope.selected_country)
	with col2: st.write('Currency = ' + currency +' ( ' + dollar_symbol + ' )')

	st.markdown("""---""")

	st.write('**Market Summary - Totals**')
	col1,col2,col3,col4,col5 = st.columns(5)




	regos_inactive_total = 123568
	regos_active_total = 456781
	regos_total = regos_inactive_total + regos_active_total

	apam_total = 472.27
	active_ratio_total = .242


	dolls_active_total = 7432666.27



	with col1: 
		st.write('**Fundraisers**')
		st.write('**Inactive**')
		st.write('**Active**')
		st.write('**Total**')
	
	with col2: 
		st.write('**Registrations**')
		st.write(format_regos(regos_inactive_total))
		st.write(format_regos(regos_active_total))
		st.write(format_regos(regos_total))

	with col3:
		st.write('**Average Per Mo**')
		st.write('$  0.00')
		st.write(format_dolls(apam_total))
		st.write('-')

	with col4:
		st.write('**Total Funds Raised**')
		st.write(format_dolls(0.0))
		st.write(format_dolls(dolls_active_total))
		st.write(format_dolls(dolls_active_total))

	with col5:
		st.write('**Active Ratio**')
		st.write(format_percent(0.0))
		st.write(format_percent(active_ratio_total))
		st.write('-')



	st.markdown("""---""")


	# for i in range(20):
	# 	print (i)
	# 	st.write(i, 'This will be even more data')

	

	scope.selected_tenure = st.selectbox ( 
												label=('Tenure Category'), 
												options=scope.dropdown_tenure,
												
												help='Select the tenure level to view and edit the rates.',
												key='target_selected_tenure',
												) 


	# st.markdown("""---""")
	

	
	# regions = ['Tas', 'NSW', 'VIC', 'QLD', 'NT', 'SA', 'WA', 'ACT', 'Other']
	regions = ['Tas', 'NSW', 'VIC', 'QLD', 'NT']

	col_list = regions

	# col_list.insert(0, 'Measure')
	no_of_columns = len(col_list)

	print('We have this many regions >', no_of_columns)

	
	cols = st.columns(no_of_columns)

	# for i, x in enumerate(regions):
	for i, col in enumerate(cols):
		print(i)
		print(regions[i])

		# col.selectbox(f"Input # {i}",[1,2,3], key=i)
		col.write('**'+regions[i]+'**')
		col.slider(label='Active Fundraisers', value=50, key=i)
		col.slider(label='In-Active Fundraisers', value=75, key=i)
		col.number_input(label='APAM', min_value=75.00, max_value=400.00, value=225.87, key=i)

		col.text_area(label='Explaination for changes', key=i)
		# if i == 0:
		# 	col.write('Number of Active Fundraisers')
		# 	col.write('Number of Inactive Fundraisers')
		# else:
		# 	# col.selectbox(f"Input # {i}",[1,2,3], key=i)
		# 	col.slider(label='Active Fundraisers', value=0, key=i)




		# for column in no_of_columns:
		# 	col.write('This is a mesure')

		# TODO - we need to skip the first column and we might need a total column at the end??
