import streamlit as st
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFium2Loader
from langchain.chains.question_answering import load_qa_chain


text_splitter = RecursiveCharacterTextSplitter(
        separators = ["\n\n", " ", "", "."],
        chunk_size = 1000,
        chunk_overlap = 500
    )
    
embeddings = HuggingFaceEmbeddings()


# Helper Functions
def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Hi how can I help you?"}]


def load_store_doc(file):
    loader = PyPDFium2Loader(file)
    data = text_splitter.split_documents(loader.load())
    vs = FAISS.from_documents(data, embeddings)
    return vs



def generate_response(prompt_input, llm, vs):
    doc = vs.similarity_search(prompt_input)
    chain = load_qa_chain(llm, chain_type="stuff")
    output = chain({"input_documents": doc, "question": prompt_input}, return_only_outputs=True)['output_text']
    return doc, output


def reformat(doc, ans):
    s = ans + '  \n  \n  The answer is generated based on the following context  \n'
    for i, d in enumerate(doc):
        s += '  \n  \n' + str(i+1)+'. Page ' + str(d.metadata['page'])
        s += '  \n' + d.page_content
    return s