import streamlit as st


st.markdown("***")

colL, colR = st.columns((15,  30))

with colL:
    st.markdown("""
    ## Example use of streamlit for presentations

    ### 1. pages
    - Adding seperate streamlit .py files in a folder called `pages`
    - All pages can be accessed in sidebar

    ### 2. `st.echo`
    - used in **Example code**
    - provides ability to run and show the same code

    ### 3. background image
    - Can add various additional personalisations using html
    - This involves using `st.markdown` with `unsafe_allow_html=True`
        - Use of html not recommended by streamlit
                - Hi
    ### 
    """)
with colR:
    st.markdown("""Hello""")
