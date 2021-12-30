import streamlit as st
import random
dict = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'か':'ka', 'き':'ki', 'く':'ku', 'け':'ke', 'こ':'ko', 'さ':'sa', 'し':'si/shi', 'す':'su', 'せ':'se', 'そ':'so', 'た':'ta', 'ち':'ti/chi', 'つ':'tu/tsu', 'て':'te', 'と':'to', 'な':'na', 'に':'ni', 'ぬ':'nu', 'ね':'ne', 'の':'no', 'は':'ha', 'ひ':'hi', 'ふ':'hu/fu', 'へ':'he', 'ほ':'ho', 'ま':'ma', 'み':'mi', 'む':'mu', 'め':'me', 'も':'mo', 'や':'ya', 'ゆ':'yu', 'よ':'yo', 'ら':'ra', 'り':'ri', 'る':'ru', 'れ':'re', 'ろ':'ro', 'わ':'wa', 'を':'wo', 'ん':'n'}
def state():
  return random.choice(list(d.keys()))
st.write(state(),'的读音：')

for key, value in dict.items():
    answer = st.text_input('請輸入答案(a)？', '0')
    comfirm_input = st.button('輸入確認')
    if comfirm_input:
        if value == answer:
            print('正确')
        else:
            print('错误')

        
        



        
        




        
