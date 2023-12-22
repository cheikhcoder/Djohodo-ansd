import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


st.markdown("<h1 style='text-align: center; '>Condition de vie </h1>", unsafe_allow_html=True)
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

@st.cache_data
def load_data(nom_fichier):
    # Chargez votre DataFrame ici
      df = pd.read_csv(nom_fichier)
      return df

menu = [ "Bien etre economique", "Migration","Hygiene"]

choice = st.sidebar.selectbox("Navigation", menu)

# Contenu principal en fonction du choix dans le menu
if choice == "Bien etre economique":
     data =load_data("bien_etre_economique_ok.csv")
     filtered_data1= data[data["indicateur"] == "le plus eleve"]
     st.subheader("Bien etre economique en fonction des regions ")
     chart_type = st.selectbox("Choisissez le type de graphique", ["Diagramme Circulaire", "Diagramme en Barres"])
     if chart_type == "Diagramme Circulaire":
             fig = px.pie(filtered_data1, values='Value', names='region', title='Diagramme Circulaire des Valeurs par Région')
             st.plotly_chart(fig, use_container_width=True)
     elif chart_type == "Diagramme en Barres":
    # Afficher le diagramme en barres avec Plotly Express
             fig = px.bar(filtered_data1, x='region', y='Value', title='Diagramme en Barres du taux de bien etre economique  par Région')
             st.plotly_chart(fig, use_container_width=True)
             
             # plus bas 
     st.divider()        
     filtered_data2= data[data["indicateur"] == "Le plus bas"]
     if chart_type == "Diagramme Circulaire":
             fig = px.pie(filtered_data2, values='Value', names='region', title='Diagramme Circulaire des Valeurs par Région')
             st.plotly_chart(fig, use_container_width=True)
     elif chart_type == "Diagramme en Barres":
    # Afficher le diagramme en barres avec Plotly Express
             fig = px.bar(filtered_data2, x='region', y='Value', title='Diagramme en Barres des Valeurs par Région')
             st.plotly_chart(fig, use_container_width=True)
     
     
             
# FIN PAGE BIEN ETRE ECONOMIQUE

  
    
elif choice == "Migration":
    st.subheader("taux de migration du a l'emploi")
    data = load_data("migration_emplois.csv")
    chart_type = st.selectbox("Choisissez le type de graphique", ["Diagramme Circulaire", "Diagramme en Barres"])
    if chart_type == "Diagramme Circulaire":
             fig = px.pie(data, values='Value', names='regions', title='Diagramme Circulaire du Taux de migration par Région')
             st.plotly_chart(fig, use_container_width=True)
    elif chart_type == "Diagramme en Barres":
    # Afficher le diagramme en barres avec Plotly Express
             fig = px.bar(data, x='regions', y='Value', title='Diagramme en Barres du Taux de migration  par Région')
             st.plotly_chart(fig, use_container_width=True)
             
    st.subheader("taux de migration du a l'innondation")
    data2 = load_data("migration_innondations.csv")
    if chart_type == "Diagramme Circulaire":
             fig = px.pie(data2, values='Value', names='regions', title='Diagramme Circulaire du Taux de migration par Région')
             st.plotly_chart(fig, use_container_width=True)
    elif chart_type == "Diagramme en Barres":
    # Afficher le diagramme en barres avec Plotly Express
             fig = px.bar(data2, x='regions', y='Value', title='Diagramme en Barres  du Taux de migration s par Région')
             st.plotly_chart(fig, use_container_width=True)              
             
elif choice == "Hygiene":
    st.subheader("taux d'utulisation de toilettes non amelioree")
    data = load_data("toilettes_non_amelioree.csv")
    chart_type = st.selectbox("Choisissez le type de graphique", ["Diagramme Circulaire", "Diagramme en Barres"])
    if chart_type == "Diagramme Circulaire":
             fig = px.pie(data, values='Value', names='region', title='Diagramme Circulaire du Taux de toilettes non amelioree par Région')
             st.plotly_chart(fig, use_container_width=True)
    elif chart_type == "Diagramme en Barres":
    # Afficher le diagramme en barres avec Plotly Express
             fig = px.bar(data, x='region', y='Value', title='Diagramme en Barres du Taux de toilettes non amelioree  par Région')
             st.plotly_chart(fig, use_container_width=True)
    