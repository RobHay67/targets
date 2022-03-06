import os
import pathlib

import streamlit as st



def scope_folders(scope):
	scope.folder_project = pathlib.Path(__file__).parent.parent.parent.resolve()

	scope.folder_data = pathlib.Path.home().joinpath( scope.folder_project, 'files' )
	
	if not os.path.isdir( scope.folder_project ) : os.makedirs( scope.folder_project )
	if not os.path.isdir( scope.folder_data ) 	 : os.makedirs( scope.folder_data )
	
	# File Paths
	scope.path_forex_file = pathlib.Path.home().joinpath( scope.folder_data, 'forex_rates.csv' )







