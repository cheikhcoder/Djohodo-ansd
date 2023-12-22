import streamlit as st
from openai import OpenAI
from PIL import Image
import os
from dotenv import load_dotenv
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

with col1: 
    st.write("""Djohodo" révolutionne la compréhension socio-économique du Sénégal en centralisant et visualisant des données variées. Intégrant science des données, IA, et design, la plateforme stimule la culture statistique et facilite la lutte contre la pauvreté. Avec un chatbot multilingue et des modèles de prédiction, "Djohodo" inspire l'innovation et favorise une utilisation responsable des données pour un impact socio-économique positif.""")

with col2 : 
  image = Image.open("images/chatbot.png")
  image2 = image.resize((300,250))
  st.image(image2)  
  user_input = st.text_input("Tout ce que vous voulais savoir sur djohodo")

  # Bouton pour envoyer la requête à l'API
  if st.button("Envoyer"):
      # Appel à l'API OpenAI GPT-3
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "you are a friendly friend"},
    {"role": "user", "content":user_input}
    ]
  )

    st.write(completion.choices[0].message.content)