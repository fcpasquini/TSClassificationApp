import streamlit as st
import sys

sys.path.append('Streamlit')

def create_main_pg():
    # Create page
    st.set_page_config(page_title='Acknowledgements', page_icon=':car:', layout = 'wide')
    
    with open('./page_content/04_Acknowledgements.txt') as file:
        page_content = file.read()

    st.markdown(page_content, unsafe_allow_html=True)

create_main_pg()