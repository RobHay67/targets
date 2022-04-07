
import streamlit as st

from targets.model.format_values import format_regos, format_dolls, format_percent, format_string
from targets.model.rates_for_view import market_total, active_rate, retention_rate





def render_market_summary(scope):
	
	st.subheader('Market Summary')

	col1,col2,col3,col4,col5,col6,col7,col8,col9 = st.columns(9)

	with col1: 
		st.markdown(format_string('Key Measures' ,align='Left'), unsafe_allow_html=True)
		st.markdown(format_string('New' ,align='Left'), unsafe_allow_html=True)
		st.markdown(format_string('Returned' ,align='Left'), unsafe_allow_html=True)
		st.markdown(format_string('Retained' ,align='Left'), unsafe_allow_html=True)
		st.markdown(format_string('Total Peer to Peer' ,align='Left'), unsafe_allow_html=True)
		st.markdown(format_string('Foundation Donations' ,align='Left'), unsafe_allow_html=True)
		st.markdown(format_string('MARKET TOTALS' ,align='Right'), unsafe_allow_html=True)

	with col2: 
		st.markdown(format_string('Registrations' ,align='Right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'New', 'regos'), align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'Returned', 'regos'), align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'Retained', 'regos'), align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'p2p', 'regos'), align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'p2p', 'regos'), align='right'), unsafe_allow_html=True)

	with col3: 
		st.markdown(format_string('Donations' ,align='Right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'Foundation', 'donations'), align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'Foundation', 'donations'), align='right'), unsafe_allow_html=True)

	with col4: 
		st.markdown(format_string('Active Registrations' ,align='Right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'New', 'active'), align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'Returned', 'active'), align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'Retained', 'active'), align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'p2p', 'active'), align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_regos(market_total(scope, 'p2p', 'active'), align='right'), unsafe_allow_html=True)

	with col5: 
		st.markdown(format_string('APAM' ,align='Right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'New', 'apam'), align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'Returned', 'apam'), align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'Retained', 'apam'), align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'p2p', 'apam'), align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		# st.markdown(format_dolls(market_total(scope, 'p2p', 'apam'), align='right'), unsafe_allow_html=True)
	
	with col6: 
		st.markdown(format_string('ADA' ,align='Right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'Foundation', 'ada'), align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'Foundation', 'ada'), align='right'), unsafe_allow_html=True)
		# st.markdown(format_dolls(market_total(scope, 'p2p', 'apam'), align='right'), unsafe_allow_html=True)
	with col7: 
		st.markdown(format_string('Funds Raised' ,align='Right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'New', 'funds'), align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'Returned', 'funds'), align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'Retained', 'funds'), align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'p2p', 'funds'), align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'Foundation', 'funds'), align='right'), unsafe_allow_html=True)
		st.markdown(format_dolls(market_total(scope, 'Total', 'funds'), align='right'), unsafe_allow_html=True)

	with col8: 
		st.markdown(format_string('Active Rate' ,align='Right'), unsafe_allow_html=True)
		st.markdown(format_percent(active_rate(scope, 'New'), align='right'), unsafe_allow_html=True)
		st.markdown(format_percent(active_rate(scope, 'Returned'), align='right'), unsafe_allow_html=True)
		st.markdown(format_percent(active_rate(scope, 'Retained'), align='right'), unsafe_allow_html=True)
		st.markdown(format_percent(active_rate(scope, 'Total'), align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)

	with col9: 
		retention_rate(scope, 'Retained')
		st.markdown(format_string('Retention Ratio' ,align='Right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_percent(retention_rate(scope, 'Retained'), align='right'), unsafe_allow_html=True)
		st.markdown(format_percent(retention_rate(scope, 'Retained'), align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)
		st.markdown(format_string('-', align='right'), unsafe_allow_html=True)

	st.markdown("""---""")


