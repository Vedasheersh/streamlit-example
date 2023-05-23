from collections import namedtuple
import altair as alt
import math
import pandas as pd
input_dataframe = pd.read_csv('./input_data.csv')
ec_unique_list = ['None'] + sorted(list(input_dataframe.EC.unique()))
substrate_unique_list = ['None'] + sorted(list(input_dataframe.SUBSTRATE.unique()))
organism_unique_list = ['None'] + sorted(list(input_dataframe.ORGANISM.unique()))

import streamlit as st
from streamlit_option_menu import option_menu

# kcat_symbol = st.latex(r'k_{cat}')
# km_symbol = st.latex(r'K_{m}')
# ki_symbol = st.latex(r'K_{i}')

st.set_page_config(layout="wide")

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.01, 2.3, .1, 0.3, .01))
with row0_1:
    st.header("DeepMMPred - Deep learning models for Michaelis-Menten parameter prediction")
with row0_2:
    st.image('./cbi_logo.jpg', use_column_width=True)

# horizontal menu
selected2 = option_menu(None, ["Single-prediction", "Bulk-prediction", "Organism-prediction", 'Help'], 
    icons=['list-task', 'cloud-upload', "piggy-bank", 'info-square'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2=="Bulk-prediction":
    st.header('Upload CSV file in format described below')
    uploaded_file = st.file_uploader('Upload a file')
    
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
    st.header(f"Calculate {st.latex(r'k_{cat}')} and {st.latex(r'K_{m}')} of an Enzyme-Substrate pair")
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 0.3, .1))
    with row0_1:
        enzyme = st.selectbox("Enter EC number:", ec_unique_list, help="Keep typing and choose from suggestions. If you don't find your EC number type 'None'")
    with row0_2:
        st.text("")
        st.text("")
#         validate_enzyme(enzyme)
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 0.3, .1))
    with row0_1:
#         organism_id = st.text_input("Organism NCBI Taxonomy id:", value="541")
        organism_name = st.selectbox("Enter Organism name:", organism_unique_list)
    with row0_2:
        st.text("")
        st.text("")
#         validate_organism(organism_name)
    
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 0.3, .1))
    with row0_1:
#         smiles = st.text_input("Substrate SMILES string:", value="CCO")
        substrate_name = st.selectbox("Enter Substrate name:", substrate_unique_list)
    with row0_2:
        st.text("")
        st.text("")
#         validate_smiles(substrate_name)
    
    row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 0.3, .1))
    with row0_1:
        clicked = st.button("Predict")
    with row0_2:
        st.text("")
        st.text("")
        calculate_kcat_km(enzyme, organism_name, substrate_name)
    
with tab2:
    st.header(f"Calculate {ki_symbol} of an Enzyme-Inhibitor pair")
    st.header("Coming soon!")
#     row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 0.3, .1))
#     with row0_1:
#         enzyme2 = st.text_input("Enzyme EC number :", value="1.1.1.1")
#     with row0_2:
#         st.text("")
#         st.text("")
#         validate_enzyme(enzyme)
#     row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 0.3, .1))
#     with row0_1:
#         organism_id2 = st.text_input("Organism NCBI Taxonomy id :", value="541")
#     with row0_2:
#         st.text("")
#         st.text("")
#         validate_organism(organism_id)
    
#     row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 0.3, .1))
#     with row0_1:
#         smiles2 = st.text_input("Inhibitor SMILES string :", value="CCO")
#     with row0_2:
#         st.text("")
#         st.text("")
#         validate_smiles(smiles)
    
#     row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
#     with row0_1:
#         clicked = st.button("Predict ")
#     with row0_2:
#         st.text("")
#         st.text("")
#         calculate_ki(enzyme2, organism_id2, smiles2)
