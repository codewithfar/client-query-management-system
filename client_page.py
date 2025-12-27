import streamlit as st
from db import get_connection
from datetime import datetime

def client_page():
    st.subheader("Submit a Query")

    mail = st.text_input("Email ID")
    mobile = st.text_input("Mobile Number")
    heading = st.text_input("Query Heading")
    description = st.text_area("Query Description")

    if st.button("Submit Query"):
        if mail and mobile and heading and description:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO queries
                (mail_id, mobile_number, query_heading,
                 query_description, status, query_created_time)
                VALUES (%s,%s,%s,%s,%s,%s)
            """, (
                mail,
                mobile,
                heading,
                description,
                "Open",
                datetime.now()
            ))

            conn.commit()
            conn.close()
            st.success("Query submitted successfully ✅")
        else:
            st.warning("Please fill all fields ⚠️")
