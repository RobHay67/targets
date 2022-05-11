import pandas as pd
import os
import streamlit as st

from config.model.folders import set_path_to_target_file
from targets.model.rates_for_view import target_rates_for_view
from config.model.regions import set_regions_for_country


def load_target_rates(scope):

	loaded_status = False

	set_path_to_target_file(scope)

	if os.path.exists( scope.path_target_file ):
		taget_table = pd.read_csv( scope.path_target_file, 
									dtype={'campaign':'int', 'payment_country':'str', 'region':'str', 'tenure':'str', 'metric':'str', 'value':'float64'},
									# parse_dates=csv_dates(schema),
									index_col=None,

									)

		loaded_status = True

	else: 
		# establish a default set of target rates to display in the browser
		taget_table = pd.DataFrame(columns=['campaign', 'payment_country', 'region', 'tenure', 'metric', 'value'])

	scope.target_df = taget_table
	scope.loaded_target_table = loaded_status
	
	