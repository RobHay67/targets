
import streamlit as st



from forex.model.maintenance import forex_rates_maintenance
from forex.model.save import save_forex_rates

def copy_prior_year_rates(scope):

	new_forex_rates = pd.DataFrame
	current_campaign = int(scope.campaign_forex)
	prior_campaign = current_campaign - 1

	st.warning ('Attempting to add forex rates for ' + str(current_campaign) + ' to the forex dataset')
	
	new_forex_rates = scope.forex_df.loc[scope.forex_df['campaign'] == prior_campaign].copy()

	if new_forex_rates.empty:
		st.error('The ' + str(prior_campaign) + ' campaign does not contain any forex rates.')
		st.info('You can only copy from the immediately preceeding campaign year, which must contain some rates to copy.')
	else:
		st.success('Finished copying ' + str(prior_campaign) + ' forex rates. You now have a base set of rates for ' + str(current_campaign))
		new_forex_rates['campaign'] = current_campaign
		scope.forex_df = pd.concat([scope.forex_df, new_forex_rates])
		forex_rates_maintenance(scope)
		save_forex_rates(scope)