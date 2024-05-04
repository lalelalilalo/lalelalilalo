import streamlit as st
from streamlit_space import space
import plotly.express as px
import pandas as pd
import numpy as np
import datetime

with st.sidebar:
    st.markdown("Author: **:blue[Huỳnh Trần Yến Nhi]**")
    st.write("Date: ", datetime.date(2024, x, x))
    st.text("Description: This serves as an illustration \n for an Interactive Web Application \n for Python Project 2.")

st.title("Score")
st.markdown("We analyze the :blue[score] data set available in the :blue[plotly.express] package.")

st.divider()

sp = px.data.tips()

st.header("Original dataset")

st.text("This is a dataset with 1,000 observations on 8 variables")

st.markdown(
"""
-**Description**: 
