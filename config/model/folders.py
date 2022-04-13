import os
# import pathlib

import streamlit as st



def scope_folders(scope):
	# scope.folder_project = pathlib.Path(__file__).parent.parent.parent.resolve()
	scope.folder_project = os.path.dirname(os.path.dirname(__file__))
	scope.folder_project = os.path.join(scope.folder_project, 'targets')

	# scope.folder_data = pathlib.Path.home().joinpath( scope.folder_project, 'files' )
	scope.folder_data = os.path.join(scope.folder_project, 'files')
	
	if not os.path.isdir( scope.folder_project ) : os.makedirs( scope.folder_project )
	if not os.path.isdir( scope.folder_data ) 	 : os.makedirs( scope.folder_data )
	
	# File Paths
	# scope.path_forex_file = pathlib.Path.home().joinpath( scope.folder_data, 'forex_rates.csv' )
	scope.path_forex_file = os.path.join(scope.folder_data, 'forex_rates.csv')



def set_path_to_target_file(scope):
	campaign_year = str(scope.campaign)

	target_file_name = 'target_rates_' + campaign_year + '.csv'

	# scope.path_target_file = pathlib.Path.home().joinpath( scope.folder_data, target_file_name )
	scope.path_target_file = os.path.join(scope.folder_data, target_file_name)





# folder_data                              /Users/rob.hay/git_repo/targets/files
# folder_project                           /Users/rob.hay/git_repo/targets

# path_forex_file                          /Users/rob.hay/git_repo/targets/files/forex_rates.csv
# path_target_file                         /Users/rob.hay/git_repo/targets/files/target_rates_2022.csv
