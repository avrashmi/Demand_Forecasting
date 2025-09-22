**Supply Chain Demand Forecasting Using Facebook Prophet and XGBoost**

This project focuses on forecasting demand in supply chain management using AI and machine learning
techniques, specifically Facebook Prophet and XGBoost. It aims to improve accuracy over traditional
forecasting methods and provide actionable insights for inventory and supply chain optimization.

**Project Description**

This project focuses on **demand forecasting in supply chain management** using **machine learning and time series techniques**. The goal is to improve accuracy over traditional forecasting methods and provide actionable insights for inventory management and supply chain optimization.

The workflow involves:

1. **Data Cleaning and Preprocessing** – Raw data is ingested, cleaned, transformed, and stored as a **SupplyChainDataset** CSV.
2. **Exploratory Data Analysis (EDA)** – Understanding trends, seasonality, and key factors affecting demand.
3. **Forecasting Models** – Two primary models are implemented:

   * **Facebook Prophet** – Handles time series with seasonal patterns and holidays.
   * **XGBoost** – High-performance gradient boosting model for scalable forecasting.
4. **Evaluation and Results** – Models are evaluated and compared to provide insights for future supply chain planning.

The project is built entirely in **Python**, leveraging libraries such as **Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook, Facebook Prophet, and XGBoost**.


python Data_Ingestion.py
python Data_Preprocessing.py
python Data_Transformation.py
python Data_Storing.py

This will clean the dataset and automatically save the csv file in a separate folder. 

I’ll then name it as SupplyChainDataset and upload it in drive to do analysis and create prediction models.

**Tools & Technologies Used**

Python 3.x – Main programming language for data analysis, modeling, and visualization.

Facebook Prophet – A time series forecasting library designed for handling seasonal trends and holiday effects.

XGBoost – A scalable, high-performance gradient boosting machine learning algorithm for regression and classification tasks.

Pandas – Library for data manipulation and analysis, including handling structured datasets.

NumPy – Library for numerical computations and array operations.

Matplotlib – Visualization library for creating static, interactive, and animated plots.

Seaborn – Statistical data visualization library built on Matplotlib for more advanced plots.

Scikit-learn – Machine learning library for preprocessing, model evaluation, and utilities.

Jupyter Notebook – Interactive coding environment to combine code, visualizations, and documentation.


**Project Structure**

SupplyChainForecasting/

Data_Ingestion.py          # Loads raw dataset

Data_Preprocessing.py      # Cleans the dataset

Data_Transformation.py     # Transforms data for analysis

Data_Storing.py            # Saves cleaned dataset as CSV (SupplyChainDataset)

fbprophet.py               # Runs Facebook Prophet forecasting

xgboost_supplychain.py     # Runs XGBoost forecasting

README.txt                 # Project documentation
