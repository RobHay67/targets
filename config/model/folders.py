import os
import pathlib

import streamlit as st



def scope_folders(scope):
	scope.folder_project = pathlib.Path(__file__).parent.parent.parent.resolve()

	print ( scope.folder_project )
	scope.folder_data = pathlib.Path.home().joinpath( scope.folder_project, 'files' )
	
	if not os.path.isdir( scope.folder_project ) : os.makedirs( scope.folder_project )
	if not os.path.isdir( scope.folder_data ) 	 : os.makedirs( scope.folder_data )
	
	# File Paths
	scope.path_data_file = pathlib.Path.home().joinpath( scope.folder_data, 'data.csv' )
	scope.path_users_file  = pathlib.Path.home().joinpath( scope.folder_data, 'users.json' )
	# scope.path_dvds_file   = pathlib.Path.home().joinpath( scope.folder_data, 'dvds.json' )






