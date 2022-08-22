
import streamlit as st

# import pandas as pd



# def export_rates_df(scope):

# 	print('export rates right here')

# 	csv = scope.rates_df.to_csv().encode()

# 	b64 = base64.b64encode(csv).decode()

# 	href = f’Download CSV File’

# 	st.markdown(href, unsafe_allow_html=True)


@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun

	df = df.to_csv(index=False).encode('utf-8')

	return df

