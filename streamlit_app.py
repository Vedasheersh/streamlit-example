from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

"""
# DeepMMPred - Deep learning models for Michaelis-Menten parameter prediction

Some brief description here....
Line1
Line2
"""

# horizontal menu
selected2 = option_menu(None, ["Single-prediction", "Bulk-prediction", "Organism-prediction", 'Help'], 
    icons=['list-task', 'cloud-upload', "piggy-bank", 'info-square'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

def print_success(success):
    if success:
        st.success('Valid!', icon="✅")
    else:
        st.error('Invalid EC format!', icon="🚨")   
        
def validate_organism(organism):
    success = True
    if not str(organism) in ['541']:
        success = False
    print_success(success)

def validate_smiles(smiles):
    success = True
    print_success(success)
    
def validate_enzyme(enzyme):
    ecs = enzyme.split('.')
#     st.text("Status")
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
    print_success(success)
    
def calculate_kcat_km(enzyme, organism_id, smiles):
    return 0.0

def calculate_ki(enzyme, organism_id, smiles):
    return 0.0

tab1, tab2 = st.tabs(["kcat & Km", "Ki"])
with tab1:
    st.header("Calculate kcat & Km of an Enzyme-Substrate pair")
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        enzyme = st.text_input("Enzyme EC number:", value="1.1.1.1")
    with row0_2:
        st.text("")
        st.text("")
        validate_enzyme(enzyme)
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        organism_id = st.text_input("Organism NCBI Taxonomy id:", value="541")
    with row0_2:
        st.text("")
        st.text("")
        validate_organism(organism_id)
    
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        smiles = st.text_input("Substrate SMILES string:", value="CCO")
    with row0_2:
        st.text("")
        st.text("")
        validate_smiles(smiles)
    
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        clicked = st.button("Predict")
    with row0_2:
        st.text("")
        st.text("")
        calculate_kcat_km(enzyme, organism_id, smiles)
    
with tab2:
    st.header("Calculate Ki of an Enzyme-Inhibitor pair")
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        enzyme2 = st.text_input("Enzyme EC number :", value="1.1.1.1")
    with row0_2:
        st.text("")
        st.text("")
        validate_enzyme(enzyme)
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        organism_id2 = st.text_input("Organism NCBI Taxonomy id :", value="541")
    with row0_2:
        st.text("")
        st.text("")
        validate_organism(organism_id)
    
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        smiles2 = st.text_input("Inhibitor SMILES string :", value="CCO")
    with row0_2:
        st.text("")
        st.text("")
        validate_smiles(smiles)
    
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
    with row0_1:
        clicked = st.button("Predict ")
    with row0_2:
        st.text("")
        st.text("")
        calculate_ki(enzyme2, organism_id2, smiles2)
