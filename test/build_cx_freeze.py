import sys
from cx_Freeze import setup, Executable
import os
import tomllib


# def get_platform_settings() -> dict:
#     """
#     Returns platform-specific settings based on the system's platform.

#     Returns:
#         dict: A dictionary containing the base, build directory, and icon path.

#     Raises:
#         ValueError: If the system's platform is not supported.
#     """
#     if sys.platform == "win32":
#         return {"base": None, "build_dir": "build_windows", "icon_path": "data/favicon.ico"}
#     elif sys.platform == "linux":
#         return {"base": None, "build_dir": "build_linux", "icon_path": None}
#     else:
#         LOGGER.error("Unsupported platform")
#         raise ValueError("Unsupported platform")

def read_requirements(file_path: str) -> list[str]:
    """
    Reads the 'requirements.txt' file and extracts package names.

    Args:
        file_path (str): Path to the 'requirements.txt' file.

    Returns:
        list[str]: A list of package names extracted from the 'requirements.txt' file.

    Raises:
        FileNotFoundError: If the 'requirements.txt' file is not found in the current directory.
    """
    try:
        with open(file_path, "r") as file:
            requirements = file.readlines()

        requirements = [
            req.strip()
            .split("=", 1)[0]
            .split(">", 1)[0]
            .split("<", 1)[0]
            .split("[", 1)[0]
            for req in requirements
        ]

        # Exclude certain packages from the requirements
        # requirements = [req for req in requirements if req not in excluded_packages]

        return requirements

    except FileNotFoundError as e:
        raise e
    

def main():
    """
    Main function to build the cx_Freeze executable.
    """

    with open("test/setup_cxfreeze.toml", mode="rb") as config:
        config = tomllib.load(config)

    requirements_file = config["project"]["requirements_file"]

    # platform_settings = get_platform_settings()

    base = None # config["project"]["base"]
    build_dir = config["project"]["build_dir"]
    icon_path = config["project"]["icon_path"]
    entry_point = config["project"]['entry_point']
    app_name = config["project"]['name']
    app_description = config["project"]['description']

    # Get the directory of the current Python executable
    python_env_dir = os.path.dirname(sys.executable)

    # Build the path to the Scripts directory and streamlit.exe
    scripts_dir = os.path.join(python_env_dir, "Scripts")
    streamlit_exe_path = os.path.join(scripts_dir, "streamlit.exe")
    python_exe_path = os.path.join(python_env_dir, "python.exe")

    include_files = [
        (streamlit_exe_path, "streamlit.exe"),
        (python_exe_path, "python.exe"),
        ("test/main_test.py", "main_test.py"),
        ("test/streamlit.py", "streamlit.py"),
    ]

    build_exe_options = {
        "packages": read_requirements(requirements_file),# + additional_packages,
        "excludes": [".env"],
        "include_files": include_files,
        "path": sys.path
    }

    executables = [
        Executable(entry_point, base=base, target_name=app_name, icon=icon_path)
    ]

    sys.argv.append("build")

    setup(
        name=app_name,
        version="1.0",
        description=app_description,
        options={
            "build_exe": build_exe_options,
            "build": {"build_base": build_dir},
        },
        executables=executables,
    )


if __name__ == "__main__":
    main()
