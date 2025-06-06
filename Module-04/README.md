## 🎯 Tutorial: Predicting Student Performance Using Multiple Linear Regression

### 📝 Objective

Your goal is to build and evaluate a **Multiple Linear Regression** model to predict a student's **Performance Index** based on multiple input features.

---

### 📂 Task 1: Load the Dataset

You are provided with a dataset containing the following columns:

* **Hours Studied**
* **Previous Scores**
* **Extracurricular Activities (Yes/No)**
* **Sleep Hours**
* **Sample Question Papers Practiced**
* **Performance Index (Target Variable)**

> ✅ **Task:** Load this dataset into your working environment (e.g., using a DataFrame or spreadsheet).

---

### 🧼 Task 2: Prepare the Data

Before training the model, the data must be cleaned and prepared.

> ✅ **Subtasks:**

* Convert categorical values like "Yes"/"No" in the **Extracurricular Activities** column into numerical format (e.g., Yes → 1, No → 0).
* Separate the dataset into **input features** (everything except *Performance Index*) and the **target variable** (*Performance Index*).

---

### 🔀 Task 3: Split the Data

Machine learning models should be evaluated on unseen data.

> ✅ **Task:** Split the dataset into two parts:

* **Training set** (to train the model)
* **Test set** (to evaluate the model's accuracy)

A common split is **80% for training** and **20% for testing**.

---

### 🧠 Task 4: Train the Model

Now it's time to train your Multiple Linear Regression model using the training set.

> ✅ **Task:** Fit a Multiple Linear Regression model using the training data (input features and target values).

---

### 📈 Task 5: Make Predictions

Once the model is trained, you can use it to predict the **Performance Index** for the test set.

> ✅ **Task:** Use the trained model to generate predictions for the test set.

---

### 📊 Task 6: Evaluate the Model

To understand how well your model performs, evaluate its predictions.

> ✅ **Subtasks:**

* Calculate the **Mean Squared Error (MSE)** to measure prediction accuracy.
* Calculate the **R² Score** to understand how much of the variation in Performance Index is explained by your model.

---
