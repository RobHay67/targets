import streamlit as st




# TODO - scope.user_can_edit_targets - need to check this is True before allowing edits


from config.model.currency import currency_name, currency_symbol

from targets.view.header import render_target_header
from targets.view.tenure import render_tenure_selector
from targets.view.regions import render_region_rates

from targets.view.tenure import render_new_fundraisers




def view_targets(scope):
	# TODO : add the country slector back to the top of this screen


	render_target_header(scope)

	render_tenure_selector(scope)

	if scope.target_selected_tenure == 'New':
		render_new_fundraisers(scope)



	render_region_rates(scope)

	st.markdown("""---""")
	st.dataframe(scope.target_df)

