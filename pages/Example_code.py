import re

import pandas as pd
import streamlit as st
from PIL import Image

from formatting import set_png_as_page_bg

def resub_eg():

    colL, colR = st.columns((10, 25))
    with colL:
        text = st.text_input("String Input", value="No. of people per household")
        regex_search = st.text_input("regex_search", value="(^[A-Za-z])")
        regex_sub = st.text_input("regex_sub", value=". \\1")

        if st.checkbox("Do examples"):
            example_list = [
                "Full-stop before",
                "Full-stop after",
                "Change order of edge words",
                "Subsititute a word",
            ]
            example_opt = st.selectbox("Examples", example_list)
            if example_opt == "Full-stop before":
                regex_search = "(^[A-Za-z])"
                regex_sub = ". \\1"
            elif example_opt == "Full-stop after":
                regex_search = "([A-Za-z]$)"
                regex_sub = "\\1\\. "
            elif example_opt == "Change order of edge words":
                regex_search = "(^[A-Za-z]+[\\s\\.])(.*[\\.\\s])([A-Za-z\\.]+$)"
                regex_sub = "\\3 \\2 \\1"
            elif example_opt == "Subsititute a word":
                regex_search = "(No.)(.*)"
                regex_sub = "Number \\2"

    with colR:
        with st.echo():
            # Everything inside this block will be both printed to the screen
            # and executed.
            def do_re_sub(text, regex_search, regex_sub):
                changed_text = re.sub(regex_search, regex_sub, text)
                st.write(
                    f"regex_search = '{regex_search}' and regex_sub = '{regex_sub}'"
                )
                st.write(f"Input string = '{text}'")
                st.write(f"Output string = '{changed_text}'")

            do_re_sub(text, regex_search, regex_sub)


def pd_replace_eg():
    colL, colR = st.columns((10, 25))
    with colL:
        text = st.text_input("String Input", value="No. of people per household")
        text_search = st.text_input("Characters to remove", value="No.")
        text_sub = st.text_input("Characters to replace", value="Number")

    with colR:
        with st.echo():
            # Everything inside this block will be both printed to the screen
            # and executed.

            def do_pd_replace(text, text_search, text_sub):
                col_name = "Start string"
                df = pd.DataFrame(data=[text], columns=[col_name])

                df["Final String"] = df[col_name].replace(
                    text_search, text_sub, regex=True
                )

                st.dataframe(df)
                st.write(f"text_search = '{text_search}' and text_sub = '{text_sub}'")
                st.write(f"Input string = '{text}'")
                st.write(f"Output string = '{df['Final String'].values[0]}'")

            do_pd_replace(text, text_search, text_sub)


def main():
    set_png_as_page_bg('header1.png')
    col1, _, col2 = st.columns((30, 10, 5))
    with col1:
        text = "Code Examples"
        st.markdown(f'<center><p style=font-family:"Calibri";background-color:#FFFFFF;color:#000000;font-size:42px;border-radius:10%><b>{text}</b></p></center>', unsafe_allow_html=True)

    with col2:
        image = Image.open("./data/logo_color_small.png")
        st.image(image, width=80)

    st.markdown("***")

    code_list = ["Overview", "re.sub", "pd.replace"]
    code_choi = st.selectbox("Code examples", code_list, label_visibility="hidden")

    if code_choi == "Overview":
        st.markdown(
            """
        ### `re.sub`

        For more on `re.sub()` see https://regex101.com/ and select
        - FLAVOR = Python and FUNCTION = Substitution

        ### `pd.replace`

        For more on `pd.replace` see [pandas replace](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html)

        """
        )

    elif code_choi == "re.sub":
        resub_eg()

    elif code_choi == "pd.replace":
        pd_replace_eg()

    image = Image.open("./data/logo2.png")
    st.sidebar.image(image, width=100)

if __name__ == "__main__":
    main()
