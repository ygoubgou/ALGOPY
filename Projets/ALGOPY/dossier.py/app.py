import streamlit as st
from formulaire import get_forms
import model_helper as models
import numpy as np
import base64
import pandas as pd
import os
import polars as pl
import plotly.express as px
from pathlib import Path


# Interface utilisateur
st.set_page_config(
        page_title="Meillleures estimations" ,page_icon="✨", layout="wide"
)
st.sidebar.header("Estimation du prix des véhicules 🚗")



st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:wght@800&display=swap');

    .animated-gradient-text {
        font-family: 'Raleway', sans-serif;
        font-size: 60px;  /* Taille visible et raisonnable */
        text-align: center;
        background: linear-gradient(270deg, #ff416c, #ff4b2b, #1e90ff, #00bfff);
        background-size: 600% 600%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: rainbow 5s ease infinite, slide-in 1s ease-out forwards;
        opacity: 0;
        transform: translateY(-20px);
        margin-top: 40px;
        margin-bottom: 40px;
    }

    @keyframes rainbow {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    @keyframes slide-in {
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>

    <div class="animated-gradient-text">Estimez le prix de votre véhicule!</div>
""", unsafe_allow_html=True)



from dataclasses import asdict

LINEAR_REGRESSION = "Régression linéaire"
GRADIENT_BOOSTING = "Gradient Boosting"
KNN = "KNN"
RANDOM_FOREST = "Random Forest"

selected_model = st.selectbox("Choisir modèle prédiction",
                              ["--", LINEAR_REGRESSION, GRADIENT_BOOSTING, KNN, RANDOM_FOREST])

if selected_model == LINEAR_REGRESSION:
    model = models.get_linear_model()
elif selected_model == GRADIENT_BOOSTING:
    model = models.get_boosting_model()
elif selected_model == RANDOM_FOREST:
    model = models.get_rf_model()
else :
    model = models.get_knn_model()


user_input = get_forms()

mlinput = np.array([*asdict(user_input.convert_to_mlinput()).values()]).reshape(1, -1)

prediction = ""

def predict_model():
    if selected_model != "--":
        value_prediction = model.predict(mlinput)
        global prediction
        prediction = f"Le modèle {selected_model} prédit : {value_prediction}"
        print(prediction)

if selected_model != "--":
    value_prediction = model.predict(mlinput)
    prediction = f"Le modèle {selected_model} prédit : {value_prediction}"
    st.markdown(f"### {prediction}")

if st.checkbox("Comparaison"):
    st.markdown("### Voici une comparaison de ce que prédit chaque modèle")

    for model, prediction in zip([LINEAR_REGRESSION, GRADIENT_BOOSTING, KNN, RANDOM_FOREST],
                                 [models.get_linear_model().predict(mlinput),
                                 models.get_boosting_model().predict(mlinput),
                                 models.get_knn_model().predict(mlinput),
                                 models.get_rf_model().predict(mlinput)]) :
        
        st.markdown(f"#### {model} : {prediction}")
        



# Obtenir le chemin absolu du répertoire du script
CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
DATA_PATH = CURRENT_DIR / "data" / "vehicules1.csv"

# Initialiser la session
if "show_stats" not in st.session_state:
    st.session_state["show_stats"] = False

# Bouton déclencheur
if st.button("📊 Statistiques moyennes"):
    st.session_state["show_stats"] = True

# Si le bouton a été cliqué
if st.session_state["show_stats"]:
    st.subheader("📈 Observation des prix par année et par marque")
    if not DATA_PATH.exists():
        st.error("❌ La donnée n'est pas chargée.")
    else:
        df = pl.read_csv(str(DATA_PATH), separator=",", ignore_errors=True)
        st.success("✅ Données chargées avec succès, voilà un apperçu !")
        st.write(df.head())

        # Vérification des colonnes
        if all(col in df.columns for col in ["annee", "prix", "marque"]):
            df = df.to_pandas()

            # Sélecteur d'année
            annees_disponibles = sorted(df["annee"].dropna().unique())
            annee_selectionnee = st.select_slider(
                "📅 Sélectionner une année",
                options=annees_disponibles,
                value=max(annees_disponibles)
            )

            # Filtrage et agrégation
            df_filtre_annee = df[df["annee"] == annee_selectionnee]
            prix_par_marque = df_filtre_annee.groupby("marque")["prix"].mean().reset_index()

            # Graphique
            fig = px.bar(prix_par_marque,
                         x="marque",
                         y="prix",
                         color="marque",
                         text="prix",
                         title=f"💶 Prix moyen par marque en {annee_selectionnee}",
                         labels={"marque": "Marque", "prix": "Prix moyen (€)"})
            st.plotly_chart(fig)
        else:
            st.warning("⚠️ Les colonnes 'annee', 'prix' et 'marque' sont nécessaires dans le dataset.")





# Obtenir le chemin absolu du répertoire du script
CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
DATA_PATH = CURRENT_DIR / "data" / "voitures.csv"

# Initialiser la session
if "show_stats" not in st.session_state:
    st.session_state["show_stats"] = False

# Bouton déclencheur
if st.button("📊 Statistiques moyennes sur les donnees initiales, plus complètes en marque"):
    st.session_state["show_stats"] = True

# Si le bouton a été cliqué
if st.session_state["show_stats"]:
    st.subheader("📈 Observation des prix par année et par marque")
    if not DATA_PATH.exists():
        st.error("❌ La donnée n'est pas chargée.")
    else:
        df = pl.read_csv(str(DATA_PATH), separator=";", ignore_errors=True)
        st.success("✅ Données chargées avec succès, voilà un apperçu !")
        st.write(df.head())

        # Vérification des colonnes
        if all(col in df.columns for col in ["annee", "prix", "marque"]):
            df = df.to_pandas()

            # Sélecteur d'année
            annees_disponibles = sorted(df["annee"].dropna().unique())
            annee_selectionnee = st.select_slider(
                "📅 Sélectionner une année",
                options=annees_disponibles,
                value=max(annees_disponibles)
            )

            # Filtrage et agrégation
            df_filtre_annee = df[df["annee"] == annee_selectionnee]
            prix_par_marque = df_filtre_annee.groupby("marque")["prix"].mean().reset_index()

            # Graphique
            fig = px.bar(prix_par_marque,
                         x="marque",
                         y="prix",
                         color="marque",
                         text="prix",
                         title=f"💶 Prix moyen par marque en {annee_selectionnee}",
                         labels={"marque": "Marque", "prix": "Prix moyen (€)"})
            st.plotly_chart(fig)
        else:
            st.warning("⚠️ Les colonnes 'annee', 'prix' et 'marque' sont nécessaires dans le dataset.")            