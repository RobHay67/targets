
import streamlit as st

from targets.model.format_values import format_regos, format_dolls, format_percent

def render_totals(scope):
	st.write('**Market Summary - Totals**')
	col1,col2,col3,col4,col5 = st.columns(5)




	regos_inactive_total = 123568
	regos_active_total = 456781
	regos_total = regos_inactive_total + regos_active_total

	apam_total = 472.27
	active_ratio_total = .242


	dolls_active_total = 7432666.27



	with col1: 
		st.write('**Fundraisers**')
		st.write('**Inactive**')
		st.write('**Active**')
		st.write('**Total**')
	
	with col2: 
		st.write('**Registrations**')
		st.write(format_regos(regos_inactive_total))
		st.write(format_regos(regos_active_total))
		st.write(format_regos(regos_total))

	with col3:
		st.write('**Average Per Mo**')
		st.write('$  0.00')
		st.write(format_dolls(apam_total))
		st.write('-')

	with col4:
		st.write('**Total Funds Raised**')
		st.write(format_dolls(0.0))
		st.write(format_dolls(dolls_active_total))
		st.write(format_dolls(dolls_active_total))

	with col5:
		st.write('**Active Ratio**')
		st.write(format_percent(0.0))
		st.write(format_percent(active_ratio_total))
		st.write('-')



	st.markdown("""---""")