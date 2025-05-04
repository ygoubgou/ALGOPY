import streamlit as st
from objets import UserInput



MODELES_PAR_MARQUE = {"__" : ["__"],
    "Renault": ["Megane E Tech", "Megane R.S.", "Megane", "Clio", "Captur", "Arkana"],
    "Citroën": ["C3", "C4 X"],
    "Dacia": ["Sandero", "Sandero Stepway", "Spring"],
    "Mercedes-Benz": ["Classe A", "Classe C", "GLA"],
    "Nissan": ["Qashqai"],
    "Peugeot": ["2008", "e-2008", "308 SW"],
    "Toyota": ["C-HR", "Yaris"]
}


"""
Cette fonction permet d'afficher un formulaire Streamlit et de retourner les données
saisies par l'utilisateur en tant qu'instance de UserInput
"""
def get_forms() -> UserInput:
    with st.sidebar:
        marque = st.radio("Marque du véhicule", list(MODELES_PAR_MARQUE.keys()))

        # Filtrage dynamique des modèles selon la marque sélectionnée
        modeles_possibles = MODELES_PAR_MARQUE.get(marque, [])
        modele = st.selectbox("Modèle du véhicule", modeles_possibles)

        annee = st.number_input("Année du véhicule", min_value=2014, max_value=2025)
        kilometrage = st.number_input("Nombre de Km au compteur", min_value=0)
        energie = st.selectbox("Energie utilisée par le véhicule", ["__","essence", "Diesel", "hybride"])
        nombre_chevaux = st.number_input("Puissance du moteur en nombre de chevaux", min_value=50, max_value=400)
        region = st.selectbox("Lieu d'achat", ["__","Auvergne-Rhône-Alpes", "Bourgogne-Franche-Comté", "Bretagne", "Centre-Val de Loire", "Grand_Est", "Hauts-de-France","Normandie","Occitanie","Pays de la Loire","Provence-Alpes-Côte d'Azur","Île-de-France"])

        user_input = UserInput(
            marque,
            modele,
            annee,
            kilometrage,
            energie,
            nombre_chevaux,
            region,
        )
    return user_input