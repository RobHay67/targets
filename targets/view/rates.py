import streamlit as st
import pandas as pd

from targets.model.export import convert_df
from targets.model.save import save_target_df


def render_rates_page(scope):

	st.header('Rates Page')


	campaign_list = list(scope.target_df['campaign'].unique())
	
	col1,col2,col3,col4,col5 = st.columns([2,6,2,2,2])

	with col1:	
		campaign_selected = st.selectbox ( 
											label=('Select Campaign Year'), 
											options=campaign_list,
											index=0,
											key='widget_campaign_rates_year',
											# on_change=render_target_df_for_selected_campaign,
											# args=(scope, ),
											) 

	with col3:
		if scope.user_can_download_rates_table:
			widget_key = scope.user_name + '_download_rates'
			st.download_button( 
										"Download Entire Rates Table", 
										data=convert_df(scope.target_df),
										file_name='target_rates_2022.csv', 
										mime='text/csv', 
										key=widget_key,
										)

	with col5:
		if scope.user_can_edit_config:
			widget_key = scope.user_name + '_copy_previous_rates'
			campaign_target = int(scope.campaign)
			campaign_previous = campaign_target - 1
			st.button(	
								'Replace ' + str(campaign_target) +' Target Rates with Last Years ( ' + str(campaign_previous) + ' ) Campaign Rates', 
								on_click=copy_rates, 
								args=(scope, ), 
								key=widget_key
								)


	rates_to_display = scope.target_df[scope.target_df['campaign']==campaign_selected]

	st.dataframe(rates_to_display, 1000,600)



def copy_rates(scope):

	# Establish Campaign Years
	campaign_to_replace = int(scope.campaign)
	campaign_previous = campaign_to_replace - 1

	# Take a copy of last years rates and change the campaign year
	last_years_rates = scope.target_df[scope.target_df['campaign']==campaign_previous].copy()
	last_years_rates['campaign'] = campaign_to_replace

	# Remove the campaign to be replaced from the primary dataframe
	scope.target_df = scope.target_df[scope.target_df['campaign'] != campaign_to_replace]

	# Concatenate last years rates into the primary dataframe
	scope.target_df = pd.concat([scope.target_df, last_years_rates], sort=False)

	save_target_df(scope)
