# cholera-survival-predictor
A MODEL FOR PREDICTING CHOLERA  SURVIVALS 
#  Cholera Survival Predictor

##  Project Overview
Cholera remains a persistent public health concern in Nigeria, often leading to significant morbidity and mortality. Accurate prediction of cholera outcomes, especially survivor estimates, is essential for effective public health planning and resource allocation.

This study presents the design and implementation of a **mathematical model** to predict the number of cholera survivors over a **30-year period** using **exponential growth functions**.

The model utilizes an exponential growth formula:

S = SoeαT  

Where:  
- **S₀** = initial number of survivors  
- **e** = 2.718 (Euler’s constant)  
- **α** = death rate  
- **T** = time duration (in years)

---

##  System Implementation
A **Python-based graphical interface** was developed using **PyQt5**, allowing users to input values and generate survivor predictions.  
The system computes and displays predicted survivor counts, with results truncated to **two decimal places** for consistency.

A complementary **Jupyter Notebook** was also created to visualize survivor trends across the 30-year timeframe, providing both **line** and **bar chart** representations of projected outcomes.

Manual calculations were performed to validate the system outputs, confirming the model’s accuracy.

---

##  Key Features
- Exponential growth-based prediction of cholera survivorship  
- PyQt5 GUI for user-friendly input and output visualization  
- Graphical trend analysis using Jupyter Notebook  
- Results rounded to two decimal places  
- Simple, interpretable, and reliable forecasting tool  

---

##  Conclusion
This study demonstrates the usefulness of **mathematical modeling** in predicting post-outbreak survival outcomes.  
The tool developed can assist **public health decision-makers** by providing a simple, reliable, and interpretable means to forecast cholera survivorship trends without the complexity of advanced machine learning or large-scale epidemiological datasets.
