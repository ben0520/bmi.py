import streamlit as st
import random
dict = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'か':'ka', 'き':'ki', 'く':'ku', 'け':'ke', 'こ':'ko', 'さ':'sa', 'し':'si/shi', 'す':'su', 'せ':'se', 'そ':'so', 'た':'ta', 'ち':'ti/chi', 'つ':'tu/tsu', 'て':'te', 'と':'to', 'な':'na', 'に':'ni', 'ぬ':'nu', 'ね':'ne', 'の':'no', 'は':'ha', 'ひ':'hi', 'ふ':'hu/fu', 'へ':'he', 'ほ':'ho', 'ま':'ma', 'み':'mi', 'む':'mu', 'め':'me', 'も':'mo', 'や':'ya', 'ゆ':'yu', 'よ':'yo', 'ら':'ra', 'り':'ri', 'る':'ru', 'れ':'re', 'ろ':'ro', 'わ':'wa', 'を':'wo', 'ん':'n'}
def state():
    return random.choice(list(dict))
value=state()
st.write(value,'的读音：')
submit_button = st.button(label='開始遊戲')   
if submit_button:
    for i in range(4):
        answer+=str(items[i])
    st.session_state.answer=answer
    ans=dict[value]
    answer = st.text_input('Please input 音標', 'a')
    comfirm_input = st.button('確認')
    if comfirm_input:
        if answer == ans :
            st.write('正确')
        else:
            st.write('错误')
                
                

        
        



        
        




        
