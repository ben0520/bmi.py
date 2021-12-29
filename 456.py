import streamlit as st
import random
import time
ping = ['a あ', 'b い', 'c う', 'd え', 'e お', 'f か', 'g き', 'h く', 'i け', 'j こ', 'k さ', 'l し', 'm す', 'n せ', 'o そ', 'p た', 'q ち', 'r つ', 's て', 't と', 'u な', 'v に', 'w ぬ', 'x ね', 'y の', 'z は', 'A ひ', 'B ふ', 'C へ', 'D ほ', 'E ま', 'F み', 'G む', 'H め', 'I も', 'J や', 'K ゆ', 'L よ', 'M ら', 'N り', 'O る', 'P れ', 'Q ろ', 'R わ', 'S を', 'T ん']
yin = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'si/shi', 'su', 'se', 'so', 'ta', 'ti/chi', 'tu/tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'hu/fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo','n']

filename = './训练记录.log'
tim1 = time.localtime(time.time())
start = time.time()
train = {x:y for x,y in zip(ping, yin)}
count = 0

for k,v in train.items():
        st.write('\n',k,'的读音：')
        m = yin[:yin.index(v)]+(yin[yin.index(v)+1:])
        choice = []
        for i in range(4):
            choice.append(m[random.randint(0,44)])
        ans = random.randint(0,3)
        choice[ans] = v
        st.write('1:',choice[0],'   2:',choice[1],'   3:',choice[2],'   4:',choice[3])

a = st.text_input('請輸入答案？', '0')
b = st.text_input('請輸入答案？', '0')
c = st.text_input('請輸入答案？', '0')
d = st.text_input('請輸入答案？', '0')
e = st.text_input('請輸入答案？', '0')
f = st.text_input('請輸入答案？', '0')
g = st.text_input('請輸入答案？', '0')        
comfirm_input = st.button('輸入確認')
if comfirm_input:
    comfirm_input=0

    inpt = input()
    while inpt not in ['1','2','3','4']:
        st.write(输入错误)
    
    inpt = int(inpt)
    if inpt == ans+1:
        st.write('正确')
        count += 1;
        
    else:
        st.write('错误，正确答案为：',ans+1,choice[ans])      
        
        




        
