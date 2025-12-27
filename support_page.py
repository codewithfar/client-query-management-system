import streamlit as st
import pandas as pd
from db import get_connection
from datetime import datetime

def support_page():
    st.subheader("Support Team Dashboard")

    conn = get_connection()
    df = pd.read_sql("SELECT * FROM queries", conn)

    if df.empty:
        st.info("No queries available")
    else:
        st.dataframe(df)

        query_id = st.number_input(
            "Enter Query ID to close",
            min_value=1,
            step=1
        )

        if st.button("Close Query"):
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE queries
                SET status='Closed',
                    query_closed_time=%s
                WHERE query_id=%s
            """, (datetime.now(), query_id))

            conn.commit()
            st.success("Query closed successfully ✅")

    conn.close()
