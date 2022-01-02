import random 
import streamlit as st 
 
 
st.title('1A2B game') 
st.markdown(""" 
大家應該都有玩過這個猜數字的遊戲吧， 
  
A 代表的是：數字猜對位子也對。 
  
B 代表的是：數字對了，但是位子不對。 
  
0～9會隨機抽出不重複的四位數字，準備好就開始吧  
 """) 
st.title('👇👇') 
 
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
random.shuffle(items) 
#st.write(answer)  
 
answer='' 

a_count=0 # initial A count 
b_count=0 # initial B count 

 
submit_button = st.button(label='開始遊戲')    
if submit_button: 
    for i in range(4): 
        answer+=str(items[i]) 
    st.session_state.answer=answer 

number=st.sidebar.text_input('請輸入數字') 
#while(True): 
    #number=st.text_input('Enter the number: ') 
#st.write(st.session_state.answer) 
if not number.isdigit():  #cheak all input is digit
     pass 
else: 
     if number==st.session_state.answer:
         st.write('好棒棒！你猜對了')
         #break 
     for i in range(4): 
         #st.session_state(st.session_state.answer) 
         for j in range(4): 
             if i==j and number[i]==st.session_state.answer[j]: 
                 a_count+=1 
             elif number[i]==st.session_state.answer[j]: 
                 b_count+=1 
             #    st.session_state(answer) 
     st.write(a_count, 'A', b_count, 'B') 
     a_count=0 
     b_count=0 
