import streamlit as st
import pandas as  pd
import datetime

st.title("これは演習課題です")
st.markdown("これから*Streamlit*の***cool***な一面をあなたに紹介しましょう！！！")
st.markdown('''
    :red[まずは] :orange[お互いに] :green[自己紹介] :blue[から] :violet[始めましょう]''') # 色付きの文字
st.header('''１．Let's introduction!!!''', divider='gray')

# Introduction
st.write("①まずは私から紹介させていただきます！  \n 下のボタンを押してください。")

# サンプルデータの生成
data = pd.read_csv("./data/introduction.csv")

# ボタンがクリックされたかの状態を保存するキーを定義
if 'show_table' not in st.session_state:
    st.session_state.show_table = False

# ボタンのアクションを定義
def toggle_table():
    st.session_state.show_table = not st.session_state.show_table

# ボタンを配置し、クリック時のアクションを設定
st.button("Show/Hide Table", on_click=toggle_table)

# ボタンの状態に応じて表を表示または非表示
if st.session_state.show_table:
    st.write(data)
    st.write("Jonny34才独身です！よろしくお願いします :sunglasses:")

st.write("①次はあなたのことを教えてください！  \n 下記のフォームに入力してください")

with st.form(key="profile_file"):

    name = st.text_input("名前")
    adress = st.text_input("住所")

    age_category =  st.radio(
        "年齢層",
        ("子供(18才未満)", "大人(18才以上)"))
    
    hobby = st.multiselect(
        "趣味（複数選択可）",
        ("スポーツ", "読書", "プログラミング", "アニメ・映画", "釣り", "料理"))
    
    mail_subscribe = st.checkbox("メールマガジンを購読する")

    height = st.slider("身長", min_value=110, max_value=210)

    start_date = st.date_input(
        "誕生日",
        datetime.date(2022, 7, 1))
    
    submit_button = st.form_submit_button("提出")

    if submit_button:
        st.text(f"よろしくお願いします!{name}さん!{adress}にお住まいなんですね！")
        st.text(f"年齢層：{age_category}")
        st.text(f", ".join(hobby))
        st.text("入力ありがとうございました！")

col1, col2 = st.columns(2)

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

st.title("コードは以下を参照ください！")
video_file = open('./data/myvideo.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)