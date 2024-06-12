import streamlit as st
import pandas as pd
import io

st.title('SSG Data Reformatting Tool')

uploaded_file = st.file_uploader("Choose a file")

