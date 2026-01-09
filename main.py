import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt
import base64
def set_bg(image_path):                       
    with open(image_path, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{data}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """, unsafe_allow_html=True)
    st.set_page_config(page_title='rajastan agriculture', page_icon='🏠')
    set_bg('a5.png')
  # put a soft sky/farm image
st.markdown("""
<style>
.crop-card {
    background: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 20px;
    max-width: 900px;
    margin: auto;
}
.crop-title {
    text-align: center;
    font-size: 36px;
    font-weight: 700;
    color: #1f2937;
}
</style>
""", unsafe_allow_html=True)
st.title('Major Crops of Rajasthan')
col1, col2 = st.columns(2)

with col1:
    st.image("ag1.jpg",use_column_width='auto')
    st.image("ag3.jpg",use_column_width='auto')

with col2:
    st.image("ag2.jpg",use_column_width='auto')
    st.image("ag4.jpg",use_column_width='auto')
    
