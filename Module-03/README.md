# 🧠 Simple Linear Regression from Scratch Using NumPy

Linear regression is one of the most fundamental techniques in machine learning and statistics. It helps us understand the relationship between two continuous variables by fitting a straight line to the data. This article walks you through the core concepts behind simple linear regression and how it can be implemented from scratch using only NumPy.

---

## 🔍 What is Simple Linear Regression?

Simple linear regression models the relationship between one independent variable and one dependent variable using the equation:

$$
Y = a + bX
$$

Where:

* $X$: Independent variable (e.g., years of experience)
* $Y$: Dependent variable (e.g., salary)
* $a$: Intercept (value of $Y$ when $X = 0$)
* $b$: Slope (change in $Y$ for a one-unit change in $X$)

---

## 📘 Problem Statement

In our example, we aim to predict an individual's salary based on their years of professional experience. We use a dataset consisting of pairs of values: years of experience and corresponding salaries.

---

## 🧠 How the Model Works

To build the linear regression model, we calculate two key values:

1. **Slope (b)**: Measures how much $Y$ increases for each additional unit of $X$.
2. **Intercept (a)**: The value of $Y$ when $X = 0$. This is where the regression line crosses the Y-axis.

These values are calculated using statistical formulas that rely on the mean of the data points and their spread.

---

## 📈 Making Predictions

Once the slope and intercept are known, we can use the regression equation to predict the value of $Y$ for any given $X$. For example, to predict the salary of someone with 10 years of experience, we simply plug that value into the equation.

---

## 📊 Visualizing the Relationship

After building the model, it’s helpful to visualize:

* The original data as scattered points
* The fitted regression line, which shows the trend or relationship between the variables

This allows us to see how well our model captures the underlying pattern in the data.

---

## ✅ Real-World Output

For instance, using our salary dataset, we might find:

* An intercept of around 25,792
* A slope of approximately 9,450

This means:

* Someone with 0 years of experience earns roughly 25,792
* Every additional year of experience adds about 9,450 to the salary

So, a person with 10 years of experience might have a predicted salary of about 120,292.

---

## 📌 Summary

* Simple linear regression helps us model a linear relationship between two continuous variables.
* The model is defined by the slope and intercept.
* Using NumPy, we can calculate these values from scratch without relying on machine learning libraries.
* This hands-on approach deepens your understanding of the mathematical foundation behind regression.

---

## 🚀 What's Next?

After understanding and implementing simple linear regression:

* Try evaluating the model's accuracy using R² (coefficient of determination)
* Extend the idea to multiple linear regression (more than one input variable)
* Explore optimization techniques like gradient descent
