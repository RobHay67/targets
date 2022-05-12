



from targets.view.header import render_targets_header
from targets.view.market_summary import render_market_summary
from targets.view.widgets import render_tenure_selector
from targets.view.newbies import render_new_fundraisers
from targets.view.returned import render_returned_fundraisers
from targets.view.retained import render_retained_fundraisers
from targets.view.foundation import render_foundation_donations

# TODO - scope.user_can_edit_targets - need to check this is True before allowing edits


def view_targets(scope):

	render_targets_header(scope)

	render_market_summary(scope)

	render_tenure_selector(scope)

	if scope.target_selected_tenure == 'New':
		render_new_fundraisers(scope)

	if scope.target_selected_tenure == 'Retained':
		render_retained_fundraisers(scope)
	
	if scope.target_selected_tenure == 'Returned':
		render_returned_fundraisers(scope)
	
	if scope.target_selected_tenure == 'Foundation':
		render_foundation_donations(scope)


