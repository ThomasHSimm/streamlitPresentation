import os
import subprocess
import sys

def main():
    streamlit_app_path = os.path.join(os.getcwd(), "streamlit.py")

    streamlit_script_path = os.path.join(
            os.getcwd(), "streamlit.exe"
        )
    
    python_path =  os.path.join(
            os.getcwd(), "python.exe"
        )
    sys.executable = python_path
    
    subprocess.Popen([streamlit_script_path, "run", streamlit_app_path])
    

if __name__ == "__main__":
    main()
