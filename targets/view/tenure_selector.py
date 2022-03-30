
from email import header
import streamlit as st


def render_tenure_selector(scope):

	col1,col2 = st.columns([1,3])

	with col1:

		scope.target_selected_tenure = st.selectbox ( 
													label=('Tenure Category'), 
													options=scope.dropdown_tenure,
													help='Select the tenure level to view and edit the rates.',
													) 




def tenure_group_header(scope):

	if scope.target_selected_tenure == 'Foundation':
		header_string = (str(scope.target_selected_tenure) + ' Donors')
	else:
		header_string = (str(scope.target_selected_tenure) + ' Fundraisers')


	return header_string
