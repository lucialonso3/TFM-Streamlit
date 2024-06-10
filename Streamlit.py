import streamlit as st

st.markdown(
    """
    <link rel="stylesheet" href="style.css">
    """,
    unsafe_allow_html=True
)

audios = {
    'Inglés': "/Users/luciaalonsoarias/Downloads/audios/audio_en.mp3",
    'Francés': "/Users/luciaalonsoarias/Downloads/audios/audio_fr.mp3",
    'Alemán': "/Users/luciaalonsoarias/Downloads/audios/audio_de.mp3",
    'Español': "/Users/luciaalonsoarias/Downloads/audios/audio_es.mp3"
}

# Textos para la etiqueta del botón de radio según el idioma
textos_idioma = {
    'Inglés': 'Paseos in Mexico City',
    'Francés': 'Paseos à Mexico',
    'Alemán': 'Paseos durch Mexiko-Stadt',
    'Español': 'Paseos en Ciudad de Mexico'
}

# Lista de idiomas disponibles
idiomas = list(audios.keys())

# Obtener el nombre del idioma seleccionado
idioma_elegido = st.radio("", idiomas)



header = st.container()
dataset = st.container()

with header:
    st.title("Paseo App")


titulo_ciudad = textos_idioma[idioma_elegido]
with dataset:
    st.header(titulo_ciudad)


textos_idioma = {
    'Inglés': 'Choose a Paseo',
    'Francés': 'Choisissez un Paseo',
    'Alemán': 'Wählen Sie eine Paseo',
    'Español': 'Elija un Paseo'
}
titulo_opcion = textos_idioma[idioma_elegido]
option = st.selectbox(
titulo_opcion,
('Palacio Nacional', 'Museo Frida Kahlo', 'Virgen Guadalupe'))


seleccionado = {
    'Inglés': 'You have selected ',
    'Francés': 'Vous avez sélectionné ',
    'Alemán': 'Du hast ausgewählt ',
    'Español': 'Ha seleccionado '
}
st.write(seleccionado[idioma_elegido], option)


# Obtener el archivo de audio correspondiente al idioma seleccionado
audio_seleccionado = audios[idioma_elegido]

# Reproducir el audio
st.audio(audio_seleccionado, format="audio/mpeg", loop=True)


















