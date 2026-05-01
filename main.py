import streamlit as st
import nltk
import traceback

@st.cache_resource
def download_nltk():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

download_nltk()

from loader import load_data
from tokenisation import tokenize
from stemming import apply_stemming
from frequence import word_freq, ngrams, collocations_pmi
from visualisation import display_visuals
from concordance import get_concordance


if "text" not in st.session_state:
    st.session_state.text = None


st.title("Analyse de Corpus NLP")


if st.button("Charger le corpus par défaut"):
    try:
        st.session_state.text = open("corpus.txt", "r", encoding="utf-8").read()
    except Exception as e:
        st.error("Erreur lors du chargement de corpus.txt")
        st.text(str(e))


uploaded_file = st.file_uploader("Choisir un fichier texte", type=["txt"])

if uploaded_file is not None:
    try:
        st.session_state.text = uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error("Erreur lors de la lecture du fichier uploadé")
        st.text(str(e))


text = st.session_state.text


if text:
    try:
        st.subheader("Texte original")
        st.write(text[:1000])

       
        tokens = tokenize(text)
        st.subheader("Tokens nettoyés")
        st.write(tokens[:50])

        stemmed_tokens = apply_stemming(tokens)
        st.subheader("Tokens lemmatisés")
        st.write(stemmed_tokens[:50])

        
        st.subheader("Top mots fréquents")
        st.write(word_freq(stemmed_tokens))

        
        st.subheader("Top Bigrams")
        st.write(ngrams(stemmed_tokens, 2))

       
        st.subheader("Collocations (PMI)")
        st.write(collocations_pmi(stemmed_tokens))

        
        display_visuals(stemmed_tokens)

    
        st.subheader("Recherche par mot-clé")

        keyword = st.text_input("Entrer un mot")

        if keyword:
            keyword = keyword.lower()
            occurrences = [w for w in stemmed_tokens if w == keyword]

            st.write(f"Nombre d'occurrences de '{keyword}': {len(occurrences)}")

       
        st.subheader("Concordance (contexte du mot)")

        search_word = st.text_input("Mot pour concordance")

        if search_word:
            search_word = search_word.lower()
            results = get_concordance(stemmed_tokens, search_word)

            if results:
                for r in results:
                    left = " ".join(r.left)
                    right = " ".join(r.right)
                    st.write(f"... {left} **{search_word}** {right} ...")
            else:
                st.write("Aucun résultat trouvé.")

    except Exception:
        st.error("Une erreur s'est produite :")
        st.text(traceback.format_exc())

else:
    st.info("Veuillez charger un corpus ou uploader un fichier texte.")