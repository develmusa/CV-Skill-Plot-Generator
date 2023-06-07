import os
import subprocess
import sys

# Install dependencies
subprocess.check_call([sys.executable, "-m", "pip", "install", "jupyter"])

# Launch Jupyter notebook
notebook_path = os.path.join(os.getcwd(), "cv_skill_plot.ipynb")
subprocess.check_call(["jupyter", "notebook", notebook_path])
