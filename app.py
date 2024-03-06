import streamlit as st
from dotenv import load_dotenv

from services import (get_pdf_text, 
                      get_text_chunks, 
                      get_vectorstore, 
                      get_conversation_chain)

from templates import css, user_template, bot_template


def handle_user_input(user_question):
    response = st.session_state.conversation({'question' : user_question})
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    load_dotenv()
    st.set_page_config(page_title="Hello PDF", page_icon="📚")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    
    st.header("Chat with your PDFs 💬")
    user_question = st.text_input("Ask a question about your documents: ")
    if user_question:
        handle_user_input(user_question)

    # st.write(user_template.replace("{{MSG}}", ), unsafe_allow_html=True)
    # st.write(bot_template.replace("{{MSG}}", "hello human"), unsafe_allow_html=True)

    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your document here",
            accept_multiple_files=True,
            type=["pdf"])
        if st.button("Process"):
            with st.spinner("Processing.."):
                pass
                # get odf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(vectorstore)

    # st.session_state.conversation



if __name__ == "__main__":
    main()