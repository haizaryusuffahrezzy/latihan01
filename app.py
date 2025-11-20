import streamlit as st

pages = [
    st.Page(page="pages/page01.py", tittle="Home", icon="🏡"),
    st.Page(page="pages/page02.py", tittle="Visualisasi Data", icon= "📊"),
    st.Page(page="pages/page03.py", tittle="Settings", icon= "⚙"),
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanden= True
)

pg.run()
