import streamlit as st

# Seite konfigurieren
st.set_page_config(page_title="Für meine Lieblingsperson", page_icon="❤️")

# Styling für den "Reel"-Look
st.markdown("""
    <style>
    .main {
        background-color: #fff5f5;
    }
    .big-font { 
        font-size:40px !important; 
        font-weight: bold; 
        color: #ff4b4b; 
        text-align: center; 
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .stButton>button { 
        background-color: #ff4b4b; 
        color: white; 
        border-radius: 25px; 
        width: 100%;
        height: 3.5em;
        font-size: 1.2em;
        font-weight: bold;
        border: none;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        background-color: #ff3333;
        color: white;
        transform: scale(1.05);
        transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# Session State für den Klick-Status
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

# Titel / Frage
st.markdown("<p class='big-font'>Willst du mein Valentin sein? 💌</p>", unsafe_allow_html=True)

# Das Bild (Die Katze aus dem Reel-Stil)
# Dieser Link führt zu einer sehr bekannten "Mochi Peach Cat" mit Herz
cat_url = "https://media.tenor.com/unS7Nf9m93MAAAAi/cat-love.gif"
st.image(cat_url, use_container_width=True)

st.write("") # Platzhalter

# Die Buttons (wie im Reel)
if not st.session_state.clicked:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("JAAA! 😍"):
            st.session_state.clicked = True
            st.balloons() # Der Effekt aus dem Video
            st.rerun()
    with col2:
        # Ein kleiner Scherz: Der "Nein"-Button, der eigentlich nichts macht 
        # (oder man könnte ihn wegwandern lassen, aber das ist komplexer)
        if st.button("Nein... 😢"):
            st.warning("Falsche Antwort! Versuch's nochmal. 😉")

# Was passiert nach dem Klick?
if st.session_state.clicked:
    st.success("YAY! Ich freue mich so! ❤️")
    
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Dein Gutschein:</h2>", unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("🎬 **Kino-Abend**\n\nDein Wunschfilm + Popcorn")
    with c2:
        st.info("🍽️ **Dinner**\n\nDein Lieblingsrestaurant")
        
    st.confetti() # Falls du ein Plugin hättest, sonst reichen die Balloons oben
