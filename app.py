import streamlit as st

pages = [
    st.Page(page="pages/pages01.py", title="Home", icon="🏡"),
    st.Page(page="pages/pages02.py", title="Visualisasi Data", icon= "📊"),
    st.Page(page="pages/pages03.py", title="Settings", icon= "⚙"),
]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()
