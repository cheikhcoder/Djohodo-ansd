import streamlit as st
from openai import OpenAI
from PIL import Image
import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.document_loaders import PyPDFLoader
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
import asyncio
load_dotenv()

st.set_page_config(page_title="Djohodo", page_icon=":bar_chart:",layout="wide")

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)



# st.title("Bienvenue a Djohodo")
st.markdown("<h1 style='text-align: center; '>Bienvenue a Djohodo</h1>", unsafe_allow_html=True)
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

col1,col2 = st.columns(2)
st.write("""Djohodo" révolutionne la compréhension socio-économique du Sénégal en centralisant et visualisant des données variées. Intégrant science des données, IA, et design, la plateforme stimule la culture statistique et facilite la lutte contre la pauvreté. Avec un chatbot multilingue et des modèles de prédiction, "Djohodo" inspire l'innovation et favorise une utilisation responsable des données pour un impact socio-économique positif.""")

 
def load_db(file, chain_type, k):
    async def load_and_process():
        # load documents 
        loader = PyPDFLoader(file)
        documents = loader.load()
        # split documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        docs = text_splitter.split_documents(documents)
        # define embedding
        embeddings = OpenAIEmbeddings(openai_api_key = os.environ.get("OPENAI_API_KEY"))
        # create vector database from data
        db = DocArrayInMemorySearch.from_documents(docs, embeddings)
        # define retriever
        retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": k})
        # create a chatbot chain. Memory is managed externally.
        qa = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, openai_api_key=os.environ.get("OPENAI_API_KEY")),
            chain_type=chain_type,
            retriever=retriever,
            return_source_documents=True,
            return_generated_question=True,
        )
        return qa

    return asyncio.run(load_and_process()) 

async def chat_with_bot(cb, query):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, cb, {"question": query, "chat_history": []})

def main():
    st.title("Cheikh'sBot")

    # Load the database and chatbot
    cb = load_db("Prompt chatbot.pdf", "stuff", 4)

    query = st.text_input("Enter your question:")
    if st.button("Ask"):
        result = asyncio.run(chat_with_bot(cb, query))
        response = result["answer"]
        st.write("ChatBot:", response)

if __name__ == '__main__':
    main()
