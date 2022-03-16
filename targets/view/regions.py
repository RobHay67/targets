
import streamlit as st





def render_region_rates(scope):

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



	

			
	# regions = ['Tas', 'NSW', 'VIC', 'QLD', 'NT', 'SA', 'WA', 'ACT', 'Other']


		# for column in no_of_columns:
		# 	col.write('This is a mesure')

		# TODO - we need to skip the first column and we might need a total column at the end??