
import pandas as pd
import os
import streamlit as st
from forex.model.rates_for_view import forex_rates_for_view


def load_forex_rates(scope):

	if os.path.exists( scope.path_forex_file ):

		forex_table = pd.read_csv( scope.path_forex_file, 
									dtype={'campaign':'int', 'country':'str', 'forex_to_sub':'float64', 'forex_to_aud':'float64'},
									# parse_dates=csv_dates(schema),
									)

		scope.forex_df = forex_table

		scope.loaded_forex_table = True

	else: 

		forex_table = pd.DataFrame(columns=['campaign', 'country', 'forex_to_sub', 'forex_to_aud'])

		scope.forex_df = forex_table
		

	# establish a default set of forex rates to display in the browser
	forex_rates_for_view(scope)			







