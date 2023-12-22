import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.markdown("<h1 style='text-align: center; '>Education</h1>", unsafe_allow_html=True)
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

@st.cache_data
def load_data(nom_fichier):
    # Chargez votre DataFrame ici
      df = pd.read_csv(nom_fichier)
      return df

menu = [  "Repartition etablissements ", "Population scolaire "]

choice = st.sidebar.selectbox("Navigation", menu)
   
if choice == "Repartition etablissements ":
    df = load_data("repartition_superieur.csv")

# Liste des types uniques
    types = df['type'].unique()

# Sélectionner le type avec un widget de sélection
    selected_type = st.selectbox("Choisissez le type", types)

# Filtrer les données pour le type sélectionné
    df_selected_type = df[df['type'] == selected_type]

# Afficher le graphique en barres avec Plotly Express
    fig_bar = px.bar(df_selected_type, x='region', y='Value',
                 title=f"Valeur de {selected_type} pour toutes les régions",
                 labels={'Value': f"{selected_type} Value"})
    fig_bar.update_layout(xaxis_title='Région', yaxis_title=f"{selected_type} Value")

# Afficher le graphique en barres
    st.plotly_chart(fig_bar, use_container_width=True)
   
elif choice == "Population scolaire ":
    st.subheader("Population scolaire")
    df = load_data("population_scolaire.csv")
# Liste des cycles uniques
    cycles = df['cycle'].unique()

# Liste des sexes uniques
    sexes = df['sexe'].unique()

# Sélectionner le cycle avec un widget de sélection
    selected_cycle = st.selectbox("Choisissez le cycle", cycles)

# Sélectionner le sexe avec un widget de sélection
    selected_sexe = st.selectbox("Choisissez le sexe", sexes)

# Filtrer les données pour le cycle et le sexe sélectionnés
    df_selected = df[(df['cycle'] == selected_cycle) & (df['sexe'] == selected_sexe)]

# Afficher le graphique en barres avec Plotly Express
    fig_bar = px.bar(df_selected, x='région', y='Value',
                 title=f"Valeur de {selected_cycle} pour {selected_sexe} par région",
                 labels={'Value': f"{selected_cycle} Value", 'région': 'Région'})
    fig_bar.update_layout(xaxis_title='Région', yaxis_title=f"{selected_cycle} Value")

# Afficher le graphique en barres
    st.plotly_chart(fig_bar, use_container_width=True)
    
    
    
    
    
    
    
