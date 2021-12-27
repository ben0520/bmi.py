import streamlit as st
import random
import time

ping = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
pian = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']
yin = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'si/shi', 'su', 'se', 'so', 'ta', 'ti/chi', 'tu/tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'hu/fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo','n']

filename = './训练记录.log'
info = '''      日语五十音图练习
                by dreamingc
请选择练习内容：
    1：平假名练习
    2：片假名练习
    3：混合练习
'''
info2 ='''开始训练，按 ctrl+C 强行停止'''
输入错误 = "输入有误，请重新输入"

st.write(info)
tim1 = time.localtime(time.time())
start = time.time()


aa = st.text_input('Please input 1, 2, 3', '0')
comfirm_input = st.button('輸入確認')
if comfirm_input:
    while aa not in ['1','2','3']:
        st.write(输入错误)
        aa = st.number_input
    else :
        aa = int(aa)
        if aa == 1:
            train = {x:y for x,y in zip(ping, yin)}
        elif aa == 2:
            train = {x:y for x,y in zip(pian, yin)}
        else :
            train = {x:y for x,y in zip(ping, yin)}
            train.update({x:y for x,y in zip(pian, yin)})
    st.write(info2)
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
        comfirm_input = st.button('輸入確認')
        while inpt not in ['1','2','3','4']:
            st.write(输入错误)
            inpt = st.number_input
        inpt = int(inpt)
        if inpt == ans+1:
            st.write('正确')
            count += 1;
        else:
            st.write('错误，正确答案为：',ans+1,choice[ans])

    finish = time.time()
    st.write('\n恭喜，完成一次训练，正确率：',count,'/',92 if aa==3 else 46 )
    st.write('用时：%.2f 秒\n' % (finish-start))

    with open (filename,'a') as f:
        f.write(time.strftime('%Y-%m-%d-%H %I:%M',tim1))
        f.write('\n     正确率：')
        f.write(str(count))
        f.write('/')
        f.write(str(92 if aa==3 else 46))
        f.write('    用时：%.2f 秒\n' % (finish-start))
