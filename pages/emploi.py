import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.markdown("<h1 style='text-align: center; '>Emploi</h1>", unsafe_allow_html=True)
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

st.subheader("Nombres de Salaries")

@st.cache_data
def load_data(nom_fichier):
    # Chargez votre DataFrame ici
      df = pd.read_csv(nom_fichier)
      return df

menu = [ "Nombre Salaries", "Population active", "Chomage"]

choice = st.sidebar.selectbox("Navigation", menu)

# Contenu principal en fonction du choix dans le menu
if choice == "Nombre Salaries":
    df = load_data("info_salaries.csv")
    # Liste des secteurs d'activité uniques
  
# Liste des secteurs d'activité uniques
    secteurs = df['secteurs-d-activités'].unique()

# Sélectionner le secteur d'activité avec un widget de sélection
    selected_secteur = st.selectbox("Choisissez le secteur d'activité", secteurs)

# Filtrer les données pour le secteur d'activité sélectionné
    df_selected_secteur = df[df['secteurs-d-activités'] == selected_secteur]

# Afficher le diagramme à barres pour l'évolution de l'effectif dans le temps
    fig = px.bar(df_selected_secteur, x='Date', y='Value', title=f"Évolution du nobre de salaries dans le secteur {selected_secteur} dans le Temps")
    fig.update_layout(xaxis_title='Année', yaxis_title='Salaries')
    st.plotly_chart(fig, use_container_width=True)
    
    
    
    
    
    
    
    
    
elif choice == "Population active":
    df = load_data("population_active_inactive.csv")
 # Liste des indicateurs uniques
    indicateurs = df['indicator'].unique()

# Sélectionner l'indicateur avec un widget de sélection
    selected_indicator = st.selectbox("Choisissez l'indicateur", indicateurs)

# Filtrer les données pour l'indicateur sélectionné
    df_selected = df[df['indicator'] == selected_indicator]

# Afficher l'évolution de la valeur avec Plotly Express (graphique linéaire)
    fig_line = px.line(df_selected, x='Date', y='Value', title=f"Évolution de la valeur pour l'indicateur {selected_indicator}", labels={'Value': 'Valeur'})
    fig_line.update_layout(xaxis_title='Année', yaxis_title='Valeur')

# Afficher les valeurs individuelles avec Plotly Express (graphique en barres)
    fig_bar = px.bar(df_selected, x='Date', y='Value', title=f"Valeurs individuelles pour l'indicateur {selected_indicator}", labels={'Value': 'Valeur'})
    fig_bar.update_layout(xaxis_title='Année', yaxis_title='Valeur')

# Afficher les deux graphiques
    st.plotly_chart(fig_line, use_container_width=True)
    st.divider()
    st.plotly_chart(fig_bar, use_container_width=True)
    
    
    
    
    
elif choice == "Chomage":
# Charger les données depuis le fichier taux_chomage.csv
    df = load_data("taux_chomage.csv")

# Liste des indicateurs uniques
    indicateurs = df['indicator'].unique()

# Sélectionner l'indicateur avec un widget de sélection
    selected_indicator = st.selectbox("Choisissez l'indicateur", indicateurs)

# Filtrer les données pour l'indicateur sélectionné
    df_selected = df[df['indicator'] == selected_indicator]

# Grouper par année et obtenir la valeur maximale pour chaque année
    df_max_values = df_selected.groupby('Date')['Value'].max().reset_index()

# Afficher la valeur maximale pour chaque année avec Plotly Express (graphique en barres)
    fig_bar_max = px.bar(df_max_values, x='Date', y='Value', title=f"Valeur maximale de {selected_indicator} pour chaque année", labels={'Value': selected_indicator})
    fig_bar_max.update_layout(xaxis_title='Année', yaxis_title=f"Max {selected_indicator}")

# Afficher le graphique en barres des valeurs maximales
    st.plotly_chart(fig_bar_max, use_container_width=True)