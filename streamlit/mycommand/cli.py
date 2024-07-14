import subprocess
import os

def main():
   subprocess.run(["streamlit","run",os.path.abspath("web.py")])