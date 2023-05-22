from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")

"""
# DeepMMPred - Deep learning models for Michaelis-Menten parameter prediction

Some brief description here....
Line1
Line2

If you have any questions, checkout our [GitHub](https://docs.streamlit.io) for more details.

"""
def validate_enzyme(enzyme):
    return type(enzyme) is str

tab1, tab2 = st.tabs(["kcat & Km", "Ki"])
with tab1:
    st.header("Calculate kcat & Km of an Enzyme-Substrate pair")
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        enzyme = st.text_input("Enzyme EC number:", value="1.1.1.1")
    with row0_2:
        validate_enzyme(enzyme)
    organism_id = st.text_input("Organism NCBI Taxonomy id:", value="541")
    clicked = st.button("Calculate")
    
    
with row0_1:
    st.title('BuLiAn - Bundesliga Analyzer')
with row0_2:
    st.text("")
    st.subheader('Streamlit App by [Tim Denzler](https://www.linkedin.com/in/tim-denzler/)')
row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
with row3_1:
    st.markdown("Hello there! Have you ever spent your weekend watching the German Bundesliga and had your friends complain about how 'players definitely used to run more' ? However, you did not want to start an argument because you did not have any stats at hand? Well, this interactive application containing Bundesliga data from season 2013/2014 to season 2019/2020 allows you to discover just that! If you're on a mobile device, I would recommend switching over to landscape for viewing ease.")
    st.markdown("You can find the source code in the [BuLiAn GitHub Repository](https://github.com/tdenzl/BuLiAn)")
    st.markdown("If you are interested in how this app was developed check out my [Medium article](https://tim-denzler.medium.com/is-bayern-m%C3%BCnchen-the-laziest-team-in-the-german-bundesliga-770cfbd989c7)")
    
with tab2:
    st.header("Calculate Ki of an Enzyme-Inhibitor pair")
    enzyme = st.text_input("Enzyme EC number :", value="1.1.1.1")
    smiles = st.text_input("Inhibitor SMILES string:", value="CCO")
    organism_id = st.text_input("Organism NCBI Taxonomy id :", value="541")
    clicked = st.button("Calculate ")
