
# Project Title: 
# Stock Market Predictions using Time Series Analysis

- **Author Name:** Shalini Mopuri
- **Semester:** Fall 2024
- **Prepared for:** UMBC Data Science Master's Degree Capstone by Dr. Chaojie (Jay) Wang
- **GitHub:** [github.com/shaliniumbc] (https://github.com/shaliniumbc/UMBC-DATA606-Capstone)
- **LinkedIn profile:** [linkedin.com/in/shalini-mopuri-5355182b5](https://www.linkedin.com/in/shalini-mopuri-5355182b5 )
- **Youtube Link :** https://youtu.be/yrMQhS1Um4g?feature=shared
- **Streamlit Link :** https://stock-price-prediction-606.streamlit.app/
- **PPT Link :** https://github.com/shaliniumbc/UMBC-DATA606-Capstone/blob/main/docs/Stockmarket_Final%20PPT.pptx

---

## Background

### What is it about?
This project focuses on a set of time series analysis and machine learning models specifically, ARIMA(Auto Regressive Integrated Moving Averages), SARIMA(Seasonal Auto-Regressive Integrated Moving Average),  Random Forest, and Support Vector Regressor applied for predicting stock prices. Financial markets are quite complex and typically volatile therefore, accurate prediction about stock prices tends to be quite hard. The general objective is to create predictive models capable of forecasting future stock prices based on historical information. This project aims to determine whether or not applying advanced algorithms in machine learning can enhance the accuracy of forecasting performance to provide helpful information for investors, traders, and analysts.


### Why does it matter?

For investors and traders, stock price prediction is extremely important because it provides them with a sound basis for good decisions on when to buy or sell assets so that their financial strategy can be optimized while reducing risks. There is an enormous amount of data that is marketable, and because of such high dynamism and non-linearity, it remains highly challenging to predict stock prices. Traditional methods currently used can often fall through in capturing the minute complexities of market behaviour. To these ends, this project aims to use advanced predictive models such as ARIMA model,Random Forest and Support Vector Regressor, with promise established in other domains to serve as a more reliable source of prediction for stock price movements.

This project is significant in terms of its potential to:
-	Improve modern techniques in time series analysis and machine learning that are used to make accurate predictions about the stock price.
- Improve risk management and decision-making for the financial market participants.
-	Contribute to the still-growing field of financial analytics, and the applications of machine learning in the finance industry.


### Research Questions?

1. Can historical stock prices and financial data be used to accurately predict future stock market trends?
2. Which time series analysis model performs the best in terms of accuracy for stock market prediction?
3. Can feature selection improve the performance of predictive models in stock market analysis?



---

## Data

- **Data Sources:** 
The dataset used for this project was obtained from Yahoo Finance which contains daily stock price data for the Bank of America Corp stock. The dataset covers a wide time span, making it ideal for analyzing stock market trends and predicting future stock prices.
- **Data Size:** 2MB
- **Data Shape:**
- Number of Rows: There are approximately 5033 rows (number of observations for all the symbols).
- Number of Columns: For every stock, the dataset includes six columns- one column for the symbol and others for time-bound price metrics opening 
  price, closing price, adjacent closing price, high, low, and volume.
- **Each Row Represents:** Each row represents the daily trading activity for one of BAC stock detailing price movements and trading volumes for that particular day.

- ### Data dictionary:
  
| **Column Name**         | **Data Type**        |  **Definition**                                                                     |
|-------------------------|----------------------|-------------------------------------------------------------------------------------|
| `Date`                  | DateTime             |  The date on which the stock data was recorded.                                     |
| `Symbol`                | String(Categorical)  |  The ticker symbol of the Nifty 50 stock                                            |
| `Open`                  | Float                |  The price at which the stock opened for trading on the day                         |
| `High`                  | Float                |  The Highest price of the stock traded at during the day                            |
| `Low`                   | Float                |  The lowest price of the stock traded at during the day.                            |
| `Close`                 | Float                |  The stock price at the close of the trading day.                                   |
| `Adj Close`             | Float                |  Adjusted closing price that accounts for dividends and stock splits.               |
| `Volume`                | Integer              |  The total number of shares traded during the day.                                  |
---

### **Potential Values for Categorical Variables**:
- **Symbol**: Represents different stock symbols (e.g., ZEETELE). Each unique stock will have its symbol.
- **Series**: Typically "EQ" for equity.


### Target Variable for the Time Series Analysis:
The **Close** column will be used as the target variable for predicting stock prices.

### Potential Features/Predictors for Time Series Analysis:
The following columns from the dataset are selected as features/predictors to predict stock prices:

-**`Open`**: The stock price at the opening of the trading day.

-**`High`**: The highest price during the trading day.

-**`Low`**: The lowest price during the trading day.


### Key Features of the Project
1. Time Series Analysis:

-Applied decomposition to analyze stock price trends, seasonality, and residuals.

-Implemented ARIMA and SARIMA models for forecasting stock prices.

2. Machine Learning Models:

-Built and compared multiple machine learning models, including Random Forest, Decision Tree, XGBoost, and SVR.

-Evaluated models using metrics like Mean Squared Error (MSE) and R² scores.

3. Exploratory Data Analysis (EDA):

-Visualized the relationship between BAC's stock prices and trading volume.

-Analyzed moving averages and correlation with the S&P 500 index.

4. Visualization:

-Compared predicted values with actual stock prices to evaluate model performance.

-Presented intuitive charts for time series decomposition, daily returns, and moving averages.

### Data Preprocessing:

Data preprocessing ensures the dataset is clean, consistent, and ready for analysis. The following steps were implemented:

1. Data Cleaning:
   
-**Removing inconsistencies and errors:** Identified and corrected errors or inconsistencies in the dataset to maintain accuracy.
   
-**Standardizing data formats:** Ensured all date, price, and volume columns follow uniform formats for seamless analysis.

-**Handling missing values and outliers:** Imputed missing values and detected outliers using statistical methods to ensure data integrity.

2. Feature Engineering:
   
-**Calculating daily returns:** Computed daily returns to capture the percentage change in stock prices, which serves as an essential indicator of performance.

-**Using moving averages:** Created 20-day, 100-day, and 200-day moving averages to identify long-term trends and smooth out price fluctuations.
These steps ensure the dataset is ready for building predictive models and extracting meaningful insights.

### Exploratory Data Analysis:

Close Price Distribution for BAC:



-Stock prices are mostly clustered between $10 and $30.

1. Close Price vs Volume:



-The scatter plot highlights a negative correlation, where higher stock prices correspond to lower trading volumes.

2. Daily Returns Over Time:



-Daily returns exhibit high volatility during periods of market turbulence, such as the 2008 financial crisis and 2020 pandemic.

3. Moving Averages:



-Demonstrated long-term stock price trends using 20-day, 100-day, and 200-day moving averages.



4. Correlation Analysis:


The correlation heatmap reveals a strong relationship between BAC's daily returns and the S&P 500 index.



5. Time Series Decomposition:

-Time Series Decomposition are divided into three components Trend, Seasonality and Residual

-**Trend:** The long-term movement or direction in the data over time.

-**Seasonality:** Regular pattern or cycle in the data that repeats over a specific period.

-**Residual:** Random variations or fluctuations in the data that cannot be attributed to trend or seasonality.



-Analyzed trends, seasonality, and residuals for BAC stock prices.

## Model Training and Evaluation

### Selected Models for Predictive Analytics
1. **ARIMA**
2. **SARIMA**
3. **Support Vector Regressor**
4. **Random Forest Classifier**
5. **Decision Tree Regressor**
6. **XGradient Boosting Classifier**


### Training Methodology
1. **Data Splitting**: Dataset was split into **80% training** and **20% testing** to have a good check on the performance of the model.
.
2. **Python Packages:**
   
 - **scikit-learn:** For model training, evaluation, and tuning.
 - **pandas and NumPy:** For efficient data manipulation and preprocessing.
 - **Matplotlib and Seaborn:** For creating insightful visualizations.

3. **Development Environment:**
   
  - **Google Colab:** Used for computational support and running the models.
  - **GitHub:** Used for version control and collaboration.

### ARIMA











   
