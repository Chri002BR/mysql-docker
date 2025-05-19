import streamlit as st
from sqlalchemy import create_engine,text

st.set_page_config(
    page_title="Streamlit App",
    layout="wide",
    initial_sidebar_state="expanded",
    )
    
## rivedi
def connection_db(dialect,username,password,host,port,database):
    """
    Create a connection to the database using SQLAlchemy.
    """
    try:
        engine = create_engine(f"{dialect}://{username}:{password}@{host}:{port}/{database}")
        connection = engine.connect()
        return connection
    except Exception as e:
        st.error(f"Error connecting to the database: {e}")
        return None


