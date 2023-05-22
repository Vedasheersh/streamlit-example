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


with st.echo(code_location='below'):
    choices = st.radio("Parameter", ["kcat", "Km", "Ki"])
    smiles = st.text_input("Substrate SMILES string:", value="CCO")
    organism_id = st.text_input("Organism NCBI Taxonomy id:", value="541")
    ec1 = st.text_input("EC1", value="1")
    ec2 = st.text_input("EC2", value="1")
    ec3 = st.text_input("EC3", value="1")
    ec4 = st.text_input("EC4", value="1")
    
    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
