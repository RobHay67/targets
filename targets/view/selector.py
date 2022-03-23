from hashlib import new
import streamlit as st


# from config.model.tenure import tenure_levels

from targets.view.new import render_new_fundraisers



def render_tenure_selector(scope):

	scope.target_selected_tenure = st.selectbox ( 
												label=('Tenure Category'), 
												options=scope.dropdown_tenure,
												help='Select the tenure level to view and edit the rates.',
												) 





