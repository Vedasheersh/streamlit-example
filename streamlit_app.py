from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# DeepMMPred - Deep learning models for Michaelis-Menten parameter prediction

Some brief description here....
Line1
Line2

If you have any questions, checkout our [GitHub](https://docs.streamlit.io) for more details.

"""

tab1, tab2 = st.tabs(["kcat & Km", "Ki"])
with tab1:
    st.header("Calculate kcat & Km of an Enzyme-Substrate pair")
    enzyme = st.text_input("Enzyme EC number:", value="1.1.1.1")
    smiles = st.text_input("Substrate SMILES string:", value="CCO")
    organism_id = st.text_input("Organism NCBI Taxonomy id:", value="541")
    clicked = st.button("Calculate")

with tab2:
    st.header("Calculate Ki of an Enzyme-Inhibitor pair")
    enzyme = st.text_input("Enzyme EC number :", value="1.1.1.1")
    smiles = st.text_input("Inhibitor SMILES string:", value="CCO")
    organism_id = st.text_input("Organism NCBI Taxonomy id :", value="541")
    clicked = st.button("Calculate ")
