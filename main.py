from langchain.chat_models import init_chat_model   # or ChatOpenAI, see note above
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

##streamlit
import streamlit as st

#from dotenv import load_dotenv
#load_dotenv()  # loads OPENAI_API_KEY

llm = init_chat_model("gpt-4o-mini", model_provider="openai")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}]")
])

output_parser = StrOutputParser()

#llm chian struncture
chain = prompt | llm | output_parser


#Title
st.title("AI poetry generator")

#Write a poem subject
content = st.text_input("시를 작성할 주제를 입력하세요")
st.write("시의 주제는:", content)    

#Request the AI to write a poem
if st.button("시 작성하기"):
    with st.spinner("AI가 시를 작성하는 중입니다..."):
        result = chain.invoke({"input": content+ "에 대한 시를 작성해줘."})
        st.write("AI가 작성한 시:\n", result)
