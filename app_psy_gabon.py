import streamlit as st
import os

# Configuration de la page
st.set_page_config(page_title="I.N.O.S.M. - PsyGabon", layout="wide", page_icon="🧠")

# --- CHARGEMENT DU LOGO AVEC SÉCURITÉ ---
logo_path = "logo.png"

# Barre latérale (Sidebar) pour la navigation et le logo
st.sidebar.markdown("---")
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, use_column_width=True)
else:
    st.sidebar.error("Fichier 'logo.png' non trouvé dans le dossier.")

st.sidebar.title("🏢 Espace de Gestion")
st.sidebar.markdown("---")

role = st.sidebar.radio("Sélectionnez votre interface :", ["Accueil (Public/Patient)", "Tableau de Bord Directeur"])

# --- INTERFACE 1 : ACCUEIL (Public / Patient) ---
if role == "Accueil (Public/Patient)":
    
    # En-tête de la page d'accueil avec Logo et Titres alignés
    col_logo, col_titre = st.columns([1, 4])
    
    with col_logo:
        if os.path.exists(logo_path):
            st.image(logo_path, width=160)
            
    with col_titre:
        st.title("I.N.O.S.M. - PsyGabon")
        st.subheader("Institut National d'Orientation et de la Santé Mentale")
        st.markdown("___") # Ligne de séparation

    st.markdown("""
    ## Bienvenue à l'Institut
    
    L'I.N.O.S.M. est l'institution de référence au Gabon, vous accompagnant à travers une approche holistique et indivisible de la psychologie, structurée autour de trois piliers fondamentaux :
    """)
    
    # Présentation des piliers en colonnes
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown("### 🎓 Pôle Développement & Éducation")
        st.write("Accompagnement du parcours scolaire, bilans d'orientation et remédiation pour enfants et adolescents.")
    with p2:
        st.markdown("### 🧠 Pôle Clinique & Psychopathologie")
        st.write("Soin de la souffrance psychique, psychothérapies et diagnostics cliniques pour l'équilibre mental.")
    with p3:
        st.markdown("### 💼 Pôle Travail & Social")
        st.write("Bien-être en entreprise, gestion des risques psychosociaux (RPS) et audit du climat social.")

    st.markdown("___")
    # Section Prise de rendez-vous simple
    with st.expander("📅 Prendre un premier contact / Demande d'information"):
        st.text_input("Nom complet")
        st.text_input("Numéro de téléphone ou Email")
        st.selectbox("Pôle concerné", ["Développement & Éducation", "Clinique & Psychopathologie", "Travail & Organisations", "Autre demande"])
        st.text_area("Votre message (bref descriptif de votre besoin)")
        st.button("Envoyer la demande d'orientation")

# --- INTERFACE 2 : TABLEAU DE BORD (Directeur) ---
else:
    st.title("📊 Tableau de Bord Direction - I.N.O.S.M.")
    st.info("Bienvenue, Directeur Dann Blanky MOUITY MOUITY. Voici le pilotage stratégique de l'Institut.")
    st.markdown("___")

    # Indicateurs clés en colonnes
    st.subheader("Statistiques Globales (Simulées)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Consultations", "23", "+4 ce mois")
    with col2:
        st.metric("Bilans Orientation", "12", "50%")
    with col3:
        st.metric("Suivis Cliniques", "8", "-1")
    with col4:
        st.metric("Contrats B2B (Entreprises)", "3", "Nouveau pôle")

    # Navigation par branches
    st.divider()
    st.subheader("Détails par Pôle d'Expertise")
    onglet = st.tabs(["🎓 Éducation", "🧠 Clinique", "💼 Travail", "⚙️ Admin"])
    
    with onglet[0]:
        st.subheader("Suivi Pôle Développement & Éducation")
        st.write("Tableau de bord des bilans et orientations scolaires.")
        # Espace pour futurs graphiques
        
    with onglet[1]:
        st.subheader("Suivi Pôle Clinique & Psychopathologie")
        st.write("Gestion des files d'attente, motifs de consultation et suivi thérapeutique.")

    with onglet[2]:
        st.subheader("Suivi Pôle Travail & Social")
        st.write("Pilotage des missions en entreprise (audits, RPS, cohésion d'équipe).")
        
    with onglet[3]:
        st.subheader("Administration & Stratégie")
        st.markdown("""
        - **Statut ANPI :** Phase finale de clôture (Immatriculation).
        - **Roadmap 2026 :** Objectif d'ouverture du centre physique T3 2026.
        - **Plateforme mobile :** En cours de déploiement pour démonstration mentors.
        """)

    # Section administrative sidebar
    st.sidebar.divider()
    st.sidebar.subheader("⚙️ Pilotage")
    st.sidebar.text("Version: 1.1 (Logo Intégré)")
    st.sidebar.caption("© 2026 I.N.O.S.M. PsyGabon")