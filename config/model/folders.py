import os
# import pathlib

import streamlit as st



def scope_folders(scope):
	# scope.folder_project = pathlib.Path(__file__).parent.parent.parent.resolve()
	# project_parent = os.path.dirname(os.path.dirname(__file__))	
	scope.folder_project = os.path.abspath(os.curdir)

	# scope.folder_files = pathlib.Path.home().joinpath( scope.folder_project, 'files' )
	scope.folder_files = os.path.join(scope.folder_project, 'files')
	
	if not os.path.isdir( scope.folder_project ) : os.makedirs( scope.folder_project )
	if not os.path.isdir( scope.folder_files ) 	 : os.makedirs( scope.folder_files )
	
	# File Paths
	# scope.path_forex_file = pathlib.Path.home().joinpath( scope.folder_files, 'forex_rates.csv' )
	scope.path_forex_file = os.path.join(scope.folder_files, 'forex_rates.csv')

	scope.path_user_file = os.path.join(scope.folder_files, 'users.csv')


def set_path_to_target_file(scope):
	print('-'*70)
	campaign_year = str(scope.campaign)

	target_file_name = 'target_rates_' + campaign_year + '.csv'
	
	# scope.path_target_file = pathlib.Path.home().joinpath( scope.folder_files, target_file_name )
	scope.path_target_file = os.path.join(scope.folder_files, target_file_name)

