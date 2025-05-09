import streamlit as st
from dotenv import load_dotenv

load_dotenv()
admin_page = st.Page("admin.py", title="Admin", icon=":material/add_circle:")
user_page = st.Page("user.py", title="User", icon=":material/delete:")

pg = st.navigation([user_page, admin_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()