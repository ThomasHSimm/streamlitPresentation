import re
from pathlib import Path

import streamlit as st
from PIL import Image

from formatting import set_png_as_page_bg

class python_folders:
    def __init__(self, folder_name, file_names):
        self.folder_name = folder_name
        self.file_names = file_names


def _get_files(folder_name):
    return [
        filenams for filenams in folder_name.glob("*.py") if filenams.stem[0] != "_"
    ]


def get_functions(fname: str):
    with open(fname, "r") as file:
        data = "".join(file.read())

    classes = re.split(r"\n(class|def)\s", data)

    defALL = {}
    defq = False
    class_or_def = ""
    for string in classes:
        class_def = string.split("(")[0]

        if defq is True:
            defALL[class_def] = class_or_def + " " + string
        if string == "class" or string == "def":
            defq = True
            class_or_def = string
        else:
            defq = False
    return defALL


def create_list_files(folder: str):
    folder = Path(folder)
    py_folders = {}
    for subfolder in sorted(folder.rglob(".")):
        if subfolder.stem[0] != "_":

            files = _get_files(subfolder)
            if files:
                py_folders[subfolder] = python_folders(subfolder, files)
    return py_folders



set_png_as_page_bg('header1.png')

col1, _, col2 = st.columns((30, 10, 5))
with col1:
    text = "Modular Functions"
    st.markdown(f'<center><p style=font-family:"Calibri";background-color:#FFFFFF;color:#000000;font-size:42px;border-radius:10%><b>{text}</b></p></center>', unsafe_allow_html=True)

with col2:
    image = Image.open("./data/logo_color_small.png")
    st.image(image, width=80)

st.markdown("***")

fname = st.text_input("Enter folder path: ", "..\\Pesticide")

py_folders = create_list_files(fname)

folder_choi = st.selectbox("Select a folder", options=py_folders.keys())

files = [file.stem for file in py_folders[folder_choi].file_names]

defclassName = st.selectbox("Select a function", options=files)


funcs = get_functions(str(folder_choi.joinpath(defclassName)) + ".py")

functions = st.selectbox("Select a function", options=funcs.keys())

if functions:
    st.code(funcs[functions])

image = Image.open("./data/logo2.png")
st.sidebar.image(image, width=100)
