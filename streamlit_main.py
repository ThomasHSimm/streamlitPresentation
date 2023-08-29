import streamlit as st
from PIL import Image
from formatting import set_png_as_page_bg

set_png_as_page_bg('header1.png')

col1, col2 = st.columns((30,  5))
with col1:
    url = "Communicating Code With Streamlit"
    st.markdown(f'<center><p style=font-family:"Calibri";background-color:#FFFFFF;color:#000000;font-size:42px;border-radius:10%><b>{url}</b></p></center>', unsafe_allow_html=True)
with col2:
    image = Image.open("./data/logo_color_small.png")
    st.image(image)

image = Image.open("./data/logo2.png")
st.sidebar.image(image, width=100)


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
    ### 
    """)
with colR:
    image = Image.open("./data/profile.jpg")
    st.image(image)
