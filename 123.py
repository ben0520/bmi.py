import streamlit as st
import random
import time

ping = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
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
        inpt = st.text_input('Please input 1, 2, 3, 4', '0')
        comfirm_input = st.button('確認')
        if comfirm_input:
            comfirm_input=0        
        while inpt not in ['1','2','3','4']:
                st.write(输入错误)
                inpt = st.text_input('Please input 1, 2, 3, 4', '0')
                comfirm_input3 = st.button('輸入確認')
                if comfirm_input3:
                    comfirm_input3=0
                inpt = int(inpt)
        if inpt == ans+1:
            st.write('正确')
            count += 1;
        else:
            st.write('错误，正确答案为：',ans+1,choice[ans])
                
        finish = time.time()
        st.write('\n恭喜，完成一次训练，正确率：',count,'/',46)
        st.write('用时：%.2f 秒\n' % (finish-start))

        with open (filename,'a') as f:
            f.write(time.strftime('%Y-%m-%d-%H %I:%M',tim1))
            f.write('\n     正确率：')
            f.write(str(count))
            f.write('/')
            f.write(str(46))
            f.write('    用时：%.2f 秒\n' % (finish-start))
