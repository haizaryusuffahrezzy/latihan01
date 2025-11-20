import streamlit as st

pages = [
    st.Page(page="pages/pages01.py", tittle="Home", icon="🏡"),
    st.Page(page="pages/pages02.py", tittle="Visualisasi Data", icon= "📊"),
    st.Page(page="pages/pages03.py", tittle="Settings", icon= "⚙"),
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanden= True
)

pg.run()
