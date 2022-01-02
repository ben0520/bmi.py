import random 
2 import streamlit as st 
3 
 
4 st.title('1A2B game') 
5 st.markdown(""" 
6 大家應該都有玩過這個猜數字的遊戲吧， 
7  
8 A 代表的是：數字猜對位子也對。 
9  
10 B 代表的是：數字對了，但是位子不對。 
11  
12 0～9會隨機抽出不重複的四位數字，準備好就開始吧  
13 """) 
14 st.title('👇👇') 
15 
 
16 items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
17 random.shuffle(items) 
18 #st.write(answer) 
19 
 
20 answer='' 
21 
 
22 a_count=0 # initial A count 
23 b_count=0 # initial B count 
24 
 
25 submit_button = st.button(label='開始遊戲')    
26 if submit_button: 
27     for i in range(4): 
28         answer+=str(items[i]) 
29     st.session_state.answer=answer 
30 
 
31 number=st.sidebar.text_input('請輸入數字') 
32 #while(True): 
33     #number=st.text_input('Enter the number: ') 
34 #st.write(st.session_state.answer) 
35 if not number.isdigit():  #cheak all input is digit 
36     pass 
37 else: 
38     if number==st.session_state.answer: 
39         st.write('好棒棒！你猜對了') 
40         #break 
41     for i in range(4): 
42         #st.session_state(st.session_state.answer) 
43         for j in range(4): 
44             if i==j and number[i]==st.session_state.answer[j]: 
45                 a_count+=1 
46             elif number[i]==st.session_state.answer[j]: 
47                 b_count+=1 
48             #    st.session_state(answer) 
49     st.write(a_count, 'A', b_count, 'B') 
50     a_count=0 
51     b_count=0 
