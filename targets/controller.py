import streamlit as st




# TODO - scope.user_can_edit_targets - need to check this is True before allowing edits


from config.model.currency import currency_name, currency_symbol

from targets.view.header import render_country_selector
from targets.view.totals import render_totals
from targets.view.tenure import render_tenure_selector
from targets.view.tenure import render_new_fundraisers

from targets.view.regions import render_region_rates


def view_targets(scope):
	# TODO : add the country slector back to the top of this screen


	render_country_selector(scope)
	render_totals(scope)
	render_tenure_selector(scope)

	if scope.target_selected_tenure == 'New':
		render_new_fundraisers(scope)



	# render_region_rates(scope)  # for demo purposes

	st.markdown("""---""")
	st.dataframe(scope.target_df)

