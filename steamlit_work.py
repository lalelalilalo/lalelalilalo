import streamlit as st
from streamlit_space import space
import plotly.express as px
import pandas as pd
import numpy as np
import datetime

with st.sidebar:
    st.markdown("Author: **:blue[Huỳnh Trần Yến Nhi]**")
    st.write("Date: ", datetime.date(2023, 7, 3))
    st.text("Description: This serves as an illustration \n for an Interactive Web Application \n for Python Project 2.")

st.title("Tips")
st.markdown("We analyze the :blue[tips] data set available in the :blue[plotly.express] package.")

st.divider()

df = px.data.tips()
