import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

@st.cache_data
def load_data(nom_fichier):
    # Chargez votre DataFrame ici
      df = pd.read_csv(nom_fichier)
      return df

st.markdown("<h1 style='text-align: center; '>Ressources Vitales</h1>", unsafe_allow_html=True)
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

menu = [  "Electrification", "Acces eau potable","Insecurite Alimentaire"]

choice = st.sidebar.selectbox("Navigation", menu)



# Contenu principal en fonction du choix dans le menu
if choice == "Insecurite Alimentaire":
    df = load_data("resilience_insecurite_alimentaire_2021.csv")
    
# Filtrer les données pour obtenir uniquement le premier département de chaque région
    first_department_data = df.groupby(['région', 'département'], as_index=False).first()

# Choisir le type de diagramme (barres ou circulaire)
    chart_type = st.selectbox("Choisissez le type de diagramme", ["Barres", "Barres renverses"])

# Choisir l'indice (RIMA ou AMR)
    selected_indice = st.selectbox("Choisissez l'indice", df['indice'].unique())

# Filtrer les données en fonction de l'indice sélectionné
    filtered_data = first_department_data[first_department_data['indice'] == selected_indice]

# Afficher le diagramme en fonction du choix de l'utilisateur
    if chart_type == "Barres":
        fig = px.bar(filtered_data, x="région", y="Value", title=f"Taux de resilience a l'insecurite alimentaire {selected_indice} pour  chaque région")
    elif chart_type == "Barres renverses":
        fig = px.bar(filtered_data, x="Value", y="région", title=f"Taux de resilience a l'insecurite alimentaire {selected_indice} pour  chaque région")
# Afficher le graphique
    st.plotly_chart(fig, use_container_width=True)

    
    
    
    
    
    
    
elif choice == "Electrification":
    df = load_data("electrification.csv")
  
    # Filtrer les données pour obtenir uniquement les taux urbains pour l'année 2022
    # Filtrer les données pour obtenir uniquement les taux urbains pour l'année 2022
    filtered_data = df[(df["niveaux"] == "Taux urbain") & (df["Date"] == 2022)]

# Choisir le type de diagramme (barres ou circulaire)
    chart_type = st.selectbox("Choisissez le type de diagramme", ["Barres", "Barres renverses"])

# Afficher le diagramme en fonction du choix de l'utilisateur
    if chart_type == "Barres":
        fig = px.bar(filtered_data, x="regions", y="Value", title="Taux d'électrification par Région en 2022")
    elif chart_type == "Barres renverses":
        fig = px.bar(filtered_data, x="Value", y="regions", title="Taux d'électrification par Région en 2022")

# Afficher le graphique
    st.plotly_chart(fig, use_container_width=True)
    
    
    
    
    
    
    
elif choice == "Acces eau potable":
    df = load_data("eau_source_amelioree.csv")
    # Sélectionner l'indicateur avec un widget de sélection
    selected_indicator = "Pourcentage utilisant pour boire l'eau d'une source amelioree"

# Afficher le graphique en barres avec Plotly Express
    fig_bar = px.bar(df, x='region', y='Value',
                 title=f"{selected_indicator} par région",
                 labels={'Value': selected_indicator, 'region': 'Région'})
    fig_bar.update_layout(xaxis_title='Région', yaxis_title=selected_indicator)

# Afficher le graphique en barres
    st.plotly_chart(fig_bar, use_container_width=True)
