import runpy
def train_files():
    runpy.run_module("speakers_training")
import streamlit as st
st.title("Bank Assist System : Tech Admin Panel")
template = """
    <div style = "background-color : black; padding : 0.1px;">
    <h1 style = "color:white;text-align:center;"> Train the Speaker data for voice authentication</h1>
    </div>
        """
st.markdown(template, unsafe_allow_html=True)
st.write("This needs to be performed at the end of the day after push is being received from super admin")
st.write("Press the button to Train speakers voices that needs to be kept as base for authentication")
if st.button("Train the user voices"):
    train_files()
    st.success("Successfully trained and saved in speaker_models database")
    st.balloons()