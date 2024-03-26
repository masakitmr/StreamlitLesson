import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')
st.write('Display Image')

left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
button2=right_column.button('左カラムに文字を表示')

if button:
  right_column.write('右カラム')
if button2:
  left_column.write('左カラム')

"""
## よくある質問
"""
expander1=st.expander('Aですか？')
expander1.write('Aです')
expander2=st.expander('Bですか？')
expander2.write('Bです')
expander3=st.expander('Cですか？')
expander3.write('Cです')
