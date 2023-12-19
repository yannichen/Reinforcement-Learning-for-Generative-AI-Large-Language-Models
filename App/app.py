import os
import torch
import streamlit as st
from utils import *
from models import *
from tempfile import NamedTemporaryFile

gpu_ava = torch.cuda.is_available()

# App title
st.set_page_config(page_title="Financial Report Chatbot")

# Left-Hand Side Bar
with st.sidebar:
    st.title('Financial Report Chatbot')
    st.write('This chatbot can work as a Financial Report Analyzer or a Prompt Optimizer')
    
    # Upload File
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if pdf_file:
        bytes_data = pdf_file.read()
        with NamedTemporaryFile(delete=False) as tmp:  # open a named temporary file
            tmp.write(bytes_data)
        vs = load_store_doc(tmp.name)
        os.remove(tmp.name)  
        
        st.write('Processing complete')
    
    

    # Select Model
    selected_model = st.sidebar.selectbox('Choose a model', list(models.keys()), key='selected_model')
    llm = models[selected_model]
    
# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Hi how can I help you?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)


# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking... {s}".format(s=" (Warning: it takes longer than expected since GPU is not available)" if gpu_ava == False else "")):
            context, response = generate_response(prompt, llm, vs)
            response = reformat(context, response)

            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)

    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
