import streamlit as st
import openai

# StreamlitのSecretsに設定したAPIキーを利用
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

st.title("AIチャットボット")

# ユーザーの入力を受け取る
user_input = st.text_input("あなたのメッセージを入力してください:")

if user_input:
    with st.spinner("AIが考えています..."):
        response = generate_response(user_input)
    st.markdown("### AIの返答:")
    st.write(response)
