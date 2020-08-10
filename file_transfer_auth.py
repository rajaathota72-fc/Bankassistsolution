import runpy
def copy_files():
    runpy.run_module("user_extracts")
import streamlit as st
st.title("Bank Assist System : Super Admin Panel")
template = """
    <div style = "background-color : black; padding : 0.1px;">
    <h1 style = "color:white;text-align:center;"> Data Push to Tech team</h1>
    </div>
        """
st.markdown(template, unsafe_allow_html=True)
st.write("This needs to be performed at the end of the day and it is to send authentications received to IT team that is responsible for training the voices and storing for authentication in central data base")
st.write("Press the button Data Push to Tech Team")
if st.button("Data Push to Tech Team"):
    copy_files()
    st.success("Successfully copied and sent for authentication training")
    st.balloons()

