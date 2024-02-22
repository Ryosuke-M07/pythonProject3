import streamlit as st
from PIL import Image

st.sidebar.write("こんにちワン！\n こちらはサイドバーです。\n メモ帳としてお使いください。")
st.sidebar.text_input("メモ帳：")

st.header('''１．Let's Upload!!!''', divider='gray')

# 画像アップロードのためのウィジェットを作成
uploaded_file = st.file_uploader("画像を選択してください。", type=["jpg", "jpeg", "png"])

# ファイルがアップロードされた場合、それを表示
if uploaded_file is not None:
    # PILを使用して画像を読み込む
    image = Image.open(uploaded_file)
    
    # 画像を表示
    st.image(image, caption='Uploaded Image.', use_column_width=True)