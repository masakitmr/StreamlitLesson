import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('Display Image')

condition=st.sidebar.slider('調子は？',0,100,50)
'コンデション',condition

txt=st.sidebar.text_input('趣味は？')
'趣味は',txt,'です'

option=st.selectbox(
'好きな数字を選ぶ',
list(range(1,11))
)
'好きな数字は',option,'です'

if st.checkbox('チェック'):
  img = Image.open('samplePythonImg.webp')
  st.image(img,caption='Tamura Masaki',use_column_width=True)