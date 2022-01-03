import streamlit as st
import random
dict = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'か':'ka', 'き':'ki', 'く':'ku', 'け':'ke', 'こ':'ko', 'さ':'sa', 'し':'si/shi', 'す':'su', 'せ':'se', 'そ':'so', 'た':'ta', 'ち':'ti/chi', 'つ':'tu/tsu', 'て':'te', 'と':'to', 'な':'na', 'に':'ni', 'ぬ':'nu', 'ね':'ne', 'の':'no', 'は':'ha', 'ひ':'hi', 'ふ':'hu/fu', 'へ':'he', 'ほ':'ho', 'ま':'ma', 'み':'mi', 'む':'mu', 'め':'me', 'も':'mo', 'や':'ya', 'ゆ':'yu', 'よ':'yo', 'ら':'ra', 'り':'ri', 'る':'ru', 'れ':'re', 'ろ':'ro', 'わ':'wa', 'を':'wo', 'ん':'n'}
def state():
    return random.choice(list(dict))

st.write(st.session_state.answer,'的读音：')
ans=dict[st.session_state.answer]
ans=st.sidebar.text_input('Please input 音標', 'a')

submit_button = st.button(label='開始遊戲')    
if submit_button: 
    value=state()
    st.session_state.answer=value    
     
    if ans==st.session_state.answer:
        st.write('正确')
    else:
        st.write('错误')
            
            
 
                
                

        
        



        
        




        
