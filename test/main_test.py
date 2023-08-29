import os
import subprocess
import sys

def main():
    streamlit_app_path = os.path.join(os.path.dirname(sys.executable), "streamlit.py")

    streamlit_script_path = os.path.join(
            os.path.dirname(sys.executable), "streamlit.exe"
        )
    
    subprocess.Popen([streamlit_script_path, "run", streamlit_app_path])
    

if __name__ == "__main__":
    main()
