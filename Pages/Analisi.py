import streamlit as st
from utils.utils import *
import pandas as pd

def create_tab_prodotti(tab_prodotti):
    col1, col2, col3=tab_prodotti.columns(3)
    ayment_info=execute_query(st.session_state["connection"],"SELECT SUM(ammount) AS total_ammount FROM payment;")



# Set the page title and layout
if __name__ == "__main__":
    st.title("Analisi")




