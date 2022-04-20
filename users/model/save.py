


def save_users_table(scope):

	# Save the User Table
	saving_df = scope.user_df.copy()

	saving_df = saving_df.reset_index()

	saving_df.to_csv( scope.path_user_file, index=False )