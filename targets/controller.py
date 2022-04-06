import streamlit as st
# TODO - remove this import later


# TODO - scope.user_can_edit_targets - need to check this is True before allowing edits


from targets.view.header import render_country_selector
from targets.view.totals import render_target_totals
from targets.view.tenure_selector import render_tenure_selector
from targets.view.newbies import render_new_fundraisers
from targets.view.retained import render_retained_fundraisers
from targets.view.returning import render_returning_fundraisers
from targets.view.foundation import render_foundation_donations




from targets.view.regions import render_region_rates



def view_targets(scope):

	render_country_selector(scope)

	render_target_totals(scope)

	render_tenure_selector(scope)

	if scope.target_selected_tenure == 'New':
		render_new_fundraisers(scope)

	if scope.target_selected_tenure == 'Retained':
		render_retained_fundraisers(scope)
	
	if scope.target_selected_tenure == 'Returning':
		render_returning_fundraisers(scope)
	
	if scope.target_selected_tenure == 'Foundation':
		render_foundation_donations(scope)


	# render_region_rates(scope)  # for demo purposes

	st.markdown("""---""")
	st.write('This is the scope.target_df')
	st.dataframe(scope.target_df)

