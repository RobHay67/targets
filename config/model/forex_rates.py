
# we need to store these as a file in the project directory
import pandas as pd
import os
# import pathlib




def load_forex_rates(scope):

	if os.path.exists( scope.path_forex_file ):

		forex_table = pd.read_csv( scope.path_forex_file, 
									dtype={'campaign':'int', 'country':'str', 'forex_to_sub':'float64', 'forex_to_aud':'float64'},
									# parse_dates=csv_dates(schema),
									)

		# ticker_index.set_index('share_code', inplace=True)

		print(forex_table)
		
		scope.forex_rates = forex_table
	else: 

		forex_table = pd.DataFrame(columns=['campaign', 'country', 'forex_to_sub', 'forex_to_aud'])

		scope.forex_rates = forex_table
		
		# save_forex_table(scope) # TODO



def save_forex_rates(scope):

	saving_df = scope.forex_rates.copy()

	saving_df.to_csv( scope.path_forex_file, index=False )









