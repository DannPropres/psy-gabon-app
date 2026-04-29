
import streamlit as st
import os
from datetime import date

# Configuration de la page
st.set_page_config(page_title="I.N.O.S.M. - PsyGabon", layout="wide", page_icon="🌿")

# --- CHARGEMENT DU LOGO ---
logo_path = "logo.png" 

# --- BARRE LATÉRALE ---
with st.sidebar:
    if os.path.exists(logo_path):
        st.image(logo_path, width=150)
    st.title("🏢 Espace de Gestion")
    st.divider()
    role = st.sidebar.radio("Navigation :", [
        "🏠 Accueil", 
        "📝 Nouvelle Consultation (Test)", 
        "📊 Tableau de Bord Directeur"
    ])

# --- INTERFACE 1 : ACCUEIL ---
if role == "🏠 Accueil":
    col_logo, col_titre = st.columns([1, 4])
    with col_logo:
        if os.path.exists(logo_path):
            st.image(logo_path, width=120)
    with col_titre:
        st.title("Bienvenue à l'I.N.O.S.M.")
        st.subheader("Institut National d'Orientation et de la Santé Mentale")
    
    st.info("L'INOSM est l'institution de référence au Gabon pour une approche holistique de la psychologie.")
    
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("### 🎓 Pôle Développement")
        st.write("Orientation scolaire et bilans.")
    with p2:
        st.markdown("### 🏥 Pôle Clinique")
        st.write("Santé mentale et psychothérapies.")
    with p3:
        st.markdown("### 💼 Pôle Travail")
        st.write("Bien-être et climat social.")

# --- INTERFACE 2 : TEST D'ENREGISTREMENT ---
elif role == "📝 Nouvelle Consultation (Test)":
    st.title("📝 Enregistrement d'une Consultation")
    st.write("Ceci est une simulation pour démontrer le fonctionnement de la base de données.")
    
    with st.form("form_consultation"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom du Patient")
            prenom = st.text_input("Prénom")
        with col2:
            motif = st.selectbox("Motif", ["Orientation", "Suivi Clinique", "RPS Travail", "Autre"])
            date_j = st.date_input("Date", date.today())
        
        notes = st.text_area("Observations cliniques")
        
        submit = st.form_submit_button("Enregistrer dans le registre de l'INOSM")
        
        if submit:
            if nom and prenom:
                st.success(f"✅ Succès : Le dossier de {prenom} {nom} a été généré avec succès dans la base sécurisée.")
                st.balloons() # Petit effet visuel pour le "Wahou" devant les mentors
            else:
                st.error("Veuillez remplir le nom et le prénom pour le test.")

# --- INTERFACE 3 : DIRECTEUR ---
else:
    st.title("📊 Pilotage Stratégique - Direction")
    st.write("Vue d'ensemble des activités de l'Institut.")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Consultations ce mois", "42", "+5")
    m2.metric("Patients suivis", "128", "+12")
    m3.metric("Taux de satisfaction", "94%", "+2%")
    
    st.bar_chart({"Consultations": [10, 15, 8, 22, 18, 25]})