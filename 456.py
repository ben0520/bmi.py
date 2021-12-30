import streamlit as st
import random
from random import choice
def state():
  dict = {'あ':'a', 'い':'i', 'う':'u', 'え':'e', 'お':'o', 'か':'ka', 'き':'ki', 'く':'ku', 'け':'ke', 'こ':'ko', 'さ':'sa', 'し':'si/shi', 'す':'su', 'せ':'se', 'そ':'so', 'た':'ta', 'ち':'ti/chi', 'つ':'tu/tsu', 'て':'te', 'と':'to', 'な':'na', 'に':'ni', 'ぬ':'nu', 'ね':'ne', 'の':'no', 'は':'ha', 'ひ':'hi', 'ふ':'hu/fu', 'へ':'he', 'ほ':'ho', 'ま':'ma', 'み':'mi', 'む':'mu', 'め':'me', 'も':'mo', 'や':'ya', 'ゆ':'yu', 'よ':'yo', 'ら':'ra', 'り':'ri', 'る':'ru', 'れ':'re', 'ろ':'ro', 'わ':'wa', 'を':'wo', 'ん':'n'}
    return choice(dict)
st.write(state(),'的读音：')

for key, value in dict.items():
        
        k = [random.randint(0,44)]
        m = yin[:yin.index(v)]+(yin[yin.index(v)+1:])
        choice = []
        for i in range(4):
            choice.append(m[random.randint(0,44)])
        ans = random.randint(0,3)
        choice[ans] = v
        st.write('1:',choice[0],'   2:',choice[1],'   3:',choice[2],'   4:',choice[3])

a = st.text_input('請輸入答案(a)？', '0')
b = st.number_input('請輸入答案？(b)', '0')
comfirm_input = st.button('輸入確認')
if comfirm_input:
    inpt = input()
    while inpt not in ['1','2','3','4']:
        st.write(输入错误)
    inpt = int(inpt)
    if inpt == ans+1:
        st.write('正确')
        count += 1;     
    else:
        st.write('错误，正确答案为：',ans+1,choice[ans])      
        
        




        
