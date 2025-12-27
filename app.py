import streamlit as st
from auth import login_user
from client_page import client_page
from support_page import support_page

st.set_page_config(page_title="Client Query Management System")

st.title("Client Query Management System")

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit:
    result = login_user(username, password)

    if result:
        role = result[0]

        if role == "Client":
            st.success("Client Login Successful ✅")
            client_page()

        elif role == "Support":
            st.success("Support Login Successful ✅")
            support_page()
    else:
        st.error("Invalid Credentials ❌")
