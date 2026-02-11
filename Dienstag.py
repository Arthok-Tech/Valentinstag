import streamlit as st
from streamlit_confetti import confetti
import time

# ---------------------------------------------------------
# Seite konfigurieren
# ---------------------------------------------------------
st.set_page_config(page_title="Für meine Lieblingsperson", page_icon="❤️")

# ---------------------------------------------------------
# Globales Styling
# ---------------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(180deg, #ffe6ec 0%, #ffd1dc 40%, #ffb3c6 100%);
    background-attachment: fixed;
    overflow: hidden;
}

/* Schwebende Valentins-Herzen */
.floating-heart {
    position: fixed;
    font-size: 55px;
    opacity: 0.22;
    animation: floatUpDown 4s ease-in-out infinite;
    pointer-events: none;
}

.heart1 { top: 12%; left: 8%; animation-delay: 0s; }
.heart2 { bottom: 15%; right: 10%; animation-delay: 1.2s; }
.heart3 { top: 40%; right: 20%; animation-delay: 0.6s; }
.heart4 { bottom: 30%; left: 18%; animation-delay: 1.8s; }

@keyframes floatUpDown {
    0%   { transform: translateY(0px); }
    50%  { transform: translateY(-25px); }
    100% { transform: translateY(0px); }
}

.big-font { 
    font-size:40px !important; 
    font-weight: bold; 
    color: #ff4b4b; 
    text-align: center; 
    font-family: 'Comic Sans MS', cursive, sans-serif;
    padding: 20px;
}

.stButton>button { 
    background-color: #ff4b4b; 
    color: white; 
    border-radius: 25px; 
    width: 100%;
    height: 3.0em;
    font-size: 1.1em;
    font-weight: bold;
    border: none;
}

p, h1, h2, h3, span { color: #31333F !important; }

/* ❤️ Neue Valentins-Boxen */
.valentine-box {
    background: linear-gradient(135deg, #ffd6e5, #ffb3c6);
    padding: 18px;
    border-radius: 18px;
    border: 2px solid #ff8fb3;
    box-shadow: 0px 0px 12px rgba(255, 255, 255, 0.6);
    font-size: 1.1em;
}

.heartbeat { animation: beat 1s infinite; }
@keyframes beat {
  0% { transform: scale(1); }
  50% { transform: scale(1.25); }
  100% { transform: scale(1); }
}

.fade-in { animation: fadein 1.5s; }
@keyframes fadein {
    from { opacity: 0; }
    to   { opacity: 1; }
}

</style>

<!-- Schwebende Herzen -->
<div class="floating-heart heart1">💖</div>
<div class="floating-heart heart2">💘</div>
<div class="floating-heart heart3">💕</div>
<div class="floating-heart heart4">💗</div>

""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------
if "clicked" not in st.session_state:
    st.session_state.clicked = False

if "transition" not in st.session_state:
    st.session_state.transition = False

# ---------------------------------------------------------
# Titel
# ---------------------------------------------------------
st.markdown("<p class='big-font'>Einladung zum Valentinstag? 💌</p>", unsafe_allow_html=True)

# ---------------------------------------------------------
# GIF + Buttons in der gleichen mittleren Spalte
# ---------------------------------------------------------
left, center, right = st.columns([1, 2, 1])

with center:
    st.image("rocket.gif")
    st.write("")

    if not st.session_state.clicked:
        btn_left, btn_right = st.columns(2)

        with btn_left:
            if st.button("JAAA! 😍", key="yes"):
                st.session_state.transition = True
                st.session_state.clicked = True
                st.rerun()

        with btn_right:
            if st.button("Nein... 😢", key="no"):
                st.warning("NIEMALS! Versuch's nochmal. 😉")

# ---------------------------------------------------------
# Übergangsseite
# ---------------------------------------------------------
if st.session_state.transition:
    st.markdown("""
        <div class='fade-in' style='text-align:center; margin-top:50px;'>
            <h1 class='heartbeat' style='color:#ff4b4b; font-size:80px;'>❤️</h1>
            <h2 style='color:#ff4b4b;'>YAY! Du bist die Liebe meines Lebens!</h2>
        </div>
    """, unsafe_allow_html=True)

    confetti(emojis=["❤️", "🎉", "💌"])
    time.sleep(2)
    st.session_state.transition = False
    st.rerun()

# ---------------------------------------------------------
# Hauptseite nach Klick
# ---------------------------------------------------------
if st.session_state.clicked and not st.session_state.transition:

    st.markdown("""
        <h2 class='heartbeat' style='text-align: center; color: #ff4b4b;'>
            YAY! Ich freue mich so! ❤️
        </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>Dein Gutschein:</h3>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("<div class='valentine-box'>🎬 <b>Kinopolis</b><br>Film Code 101</div>", unsafe_allow_html=True)

    with c2:
        st.markdown("<div class='valentine-box'>🍣 <b>Dinner</b><br>Suuuuuuuushi</div>", unsafe_allow_html=True)
