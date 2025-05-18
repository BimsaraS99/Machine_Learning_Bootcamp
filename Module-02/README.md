## Module 2: Tools of the Trade

### Objective

Set up a dedicated Conda environment with all the essential Python libraries needed for your machine learning projects. This helps keep your work organized and dependencies isolated.

Watch Video Guide: https://youtu.be/pRhxVr_E3K4?si=60g32WOEXQ2rzEMm

### What You’ll Learn

* How to create and activate a Conda virtual environment named `ml`
* How to install key machine learning libraries within this environment
* How to launch Jupyter Notebook from the Conda environment

---

### Step 1: Create a Conda Environment

Open your terminal (Anaconda Prompt on Windows) and run:

```bash
conda create --name ml python=3.9
```

This command creates a new environment named `ml` with Python version 3.9.

---

### Step 2: Activate the Conda Environment

Activate your new environment by running:

```bash
conda activate ml
```

Your prompt should now indicate that you are inside the `ml` environment.

---

### Step 3: Install Essential Libraries

With the environment active, install the main libraries used in this course:

```bash
pip install numpy pandas scikit-learn matplotlib
```

This command installs NumPy, pandas, scikit-learn, matplotlib, and Jupyter Notebook.

---

### Step 4: Open VS Code and Create a Jupyter Notebook

1. Launch **Visual Studio Code** on your computer.
2. Open the folder where you want to save your project or create a new one.
3. In VS Code, click **File > New File** and then select **Jupyter Notebook** or simply create a new file with the extension `.ipynb`.
4. Start writing and running your Python code interactively inside the notebook.

---

### Step 5: Verify Your Setup

In a new Jupyter notebook, try running:

```python
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("Conda environment 'ml' is set up and ready!")
```

---

### Summary

You’ve now created a dedicated Conda environment named `ml` with all necessary libraries for your machine learning journey. This isolated setup ensures your projects run smoothly without conflicts.

