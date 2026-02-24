from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import streamlit as st

load_dotenv()

def getSystemMessage(selected_item):
    if selected_item == "睡眠に関する相談":
        content = """
            あなたは、睡眠に関する専門家です。睡眠に関する質問に対して、わかりやすく丁寧に回答してください。
            回答は日本語でお願いします。
            """
    else:
        content = """
            あなたは、アロマテラピストです。アロマテラピーに関する相談に対して、
            効果のある精油や使用方法をわかりやすく丁寧に回答してください。
            回答は日本語でお願いします。"""
    
    return SystemMessage(content=content)

def responseChat(selected_item, input_message):
    system_message = getSystemMessage(selected_item)
    human_message = HumanMessage(content=input_message)
    
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    messages = [
        system_message,
        human_message
    ]
    result = llm.invoke(messages)
    return result.content 

st.title("サンプルアプリ: LLMを活用した相談アプリ")
st.write("##### 動作モード1: 睡眠に関する相談")
st.write("相談内容を「睡眠に関する相談」を選択し、相談を入力して実行してください。")
st.write("##### 動作モード2: アロマテラピーに関する相談")
st.write("相談内容を「アロマテラピーに関する相談」を選択し、相談を入力して実行してください。")


selected_item = st.radio(
    "相談内容を選択してください。",
    ["睡眠に関する相談", "アロマテラピーに関する相談"]
)

input_message = st.text_input(label="相談内容を入力してください。")
st.divider()

if st.button("実行"):
    st.divider()
    if selected_item == "":
        st.error("相談内容を選択してください。")
    else:
        if input_message:
            result_content = responseChat(selected_item, input_message)
            st.write(result_content)
        else:
            st.error("相談内容を入力してください。")


