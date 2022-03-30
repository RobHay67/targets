
import streamlit as st
import pandas as pd


from forex.view.header import render_forex_header
from forex.model.copy_rates import copy_prior_year_rates
from forex.view.forex_rates import render_forex_rates



def view_forex(scope):

	copy_rates = False

	copy_rates = render_forex_header(scope, copy_rates)

	if copy_rates:
		# The COPY Button only appears if we do not 
		# have any rates for the selected forex campaign year
		copy_prior_year_rates(scope)


	# If the selected forex campaign year has rates, 
	# we can now display them

	if scope.campaign_forex in scope.forex_df.campaign.values:
		render_forex_rates(scope)
	
	
	












