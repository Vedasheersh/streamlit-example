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
    ecs = enzyme.split('.')
    st.text("Status")
    success = True
    if len(ecs)!=4:
        success = False
    else:
        for each in ecs:
            if each=='-': continue
            else:
                try:
                    each_int = int(each)
                except:
                    success = False
    if success:
        st.success('Valid!', icon="✅")
    else:
        st.error('Invalid EC format!', icon="🚨")        

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
    
with tab2:
    st.header("Calculate Ki of an Enzyme-Inhibitor pair")
    enzyme = st.text_input("Enzyme EC number :", value="1.1.1.1")
    smiles = st.text_input("Inhibitor SMILES string:", value="CCO")
    organism_id = st.text_input("Organism NCBI Taxonomy id :", value="541")
    clicked = st.button("Calculate ")
