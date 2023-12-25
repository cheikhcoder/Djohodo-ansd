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

st.markdown("<h1 style='text-align: center; '>Sante</h1>", unsafe_allow_html=True)
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)
# Ajouter des éléments au menu
menu = [ "Couverture Sanitaire", "Structures de sante", "Condition d/'accouchements",]

choice = st.sidebar.selectbox("Navigation", menu)

# Couverture Sanitaire 
if choice == "Couverture Sanitaire":
    df = load_data("Evolution_taux_couverture.csv")
    selected_structure = st.selectbox("Choisissez une structure", df["structures"].unique())

# Filtrer les données en fonction du choix de l'utilisateur
    filtered_data = df[df["structures"] == selected_structure]

# Afficher la courbe au cours du temps avec Plotly Express
    fig = px.line(filtered_data, x='Date', y='Value', title=f' Évolution du taux de couverture sanitaire pour {selected_structure} au cours du temps')
    st.plotly_chart(fig, use_container_width=True)
    
    fig = px.bar(filtered_data, x='Date', y='Value', color='structures',
             title=f'Évolution du taux de couverture sanitaire pour {selected_structure} au cours du temps')
    st.plotly_chart(fig, use_container_width=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
elif choice == "Structures de sante":
    df = load_data("structure_sante.csv")
   # Widget de sélection pour les structures
    selected_structure = st.selectbox("Choisissez une structure", df["indicateurs"].unique())

# Filtrer les données en fonction de la structure sélectionnée
    filtered_data = df[df["indicateurs"] == selected_structure]

# Afficher le diagramme en barres pour le nombre de structures par région
    fig_bar = px.bar(filtered_data, x='regions', y='Value', title=f'Nombre de {selected_structure} par regions ')
    st.plotly_chart(fig_bar, use_container_width=True)
    
    # Widget de sélection pour les régions
    selected_region = st.selectbox("Choisissez une région", df["regions"].unique())
    # Filtrer les données en fonction de la région sélectionnée
    filtered_count_data = df[df['regions'] == selected_region]

# Afficher le diagramme en courbe pour l'évolution du nombre de structures pour la région sélectionnée
    fig_count = px.bar(filtered_count_data, x='Date', y='Value', title=f'Évolution des {selected_structure} pour la region de {selected_region}')
    st.plotly_chart(fig_count, use_container_width=True)




    
    
    
    
    
    
    
    
   
    
      
    
    
    
elif choice == "Condition d/'accouchements":
    df = load_data("accouchement.csv")
    # Sélectionner l'indicateur avec un widget de sélection
    selected_indicator = st.selectbox("Choisissez l'indicateur", df['indicateur'].unique())

# Filtrer les données pour l'indicateur sélectionné
    df_selected = df[df['indicateur'] == selected_indicator]

# Pour chaque région, trouver le maximum d'accouchements
    df_max = df_selected.groupby('regions')['Value'].max().reset_index()

# Afficher le graphique en barres empilées avec Plotly Express
    fig_bar = px.bar(df_max, x='regions', y='Value', color='regions',
                 title=f"Nombre de ({selected_indicator} par region )",
                 labels={'Value': 'Nombre d\'accouchements', 'regions': 'Région'})
    fig_bar.update_layout(xaxis_title='Région', yaxis_title='Nombre d\'accouchements')

# Afficher le graphique en barres empilées
    st.plotly_chart(fig_bar, use_container_width=True) 