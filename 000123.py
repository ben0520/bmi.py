import streamlit as st 

a = st.text_input('請輸入答案(a)？', '0')
b = st.number_input('請輸入答案？(b)', '0')
comfirm_input = st.button('輸入確認')
if comfirm_input:


