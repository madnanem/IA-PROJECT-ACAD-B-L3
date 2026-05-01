import streamlit as st
import plotly.express as px
from nltk import bigrams, FreqDist

def display_visuals(list_token):
    st.subheader("Top 15 Bigrams les plus fréquents")
    bi = FreqDist(bigrams(list_token))
    top_bigrams = bi.most_common(15)
    labels = [f"{a} {b}" for (a, b), _ in top_bigrams]
    counts_bi = [count for _, count in top_bigrams]
    fig2 = px.bar(
        x=labels, 
        y=counts_bi, 
        labels={"x": "Bigram", "y": "Fréquence"},
        template="plotly_dark"
    )
    st.plotly_chart(fig2)