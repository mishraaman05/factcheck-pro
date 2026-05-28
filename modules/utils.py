import streamlit as st

def load_css(file_path: str):
    """Loads external global css rules into the layout."""
    with open(file_path, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def initialize_session_state():
    """Bootstraps session variables across re-runs."""
    if "claims_data" not in st.session_state:
        st.session_state.claims_data = []
    if "processing_done" not in st.session_state:
        st.session_state.processing_done = False