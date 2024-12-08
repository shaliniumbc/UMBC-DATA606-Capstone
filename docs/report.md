
# Project Title: 
# Stock Market Predictions using Time Series Analysis

- **Author Name:** Shalini Mopuri
- **Semester:** Fall 2024
- **Prepared for:** UMBC Data Science Master's Degree Capstone by Dr. Chaojie (Jay) Wang
- **GitHub:** [github.com/shaliniumbc] (https://github.com/shaliniumbc/UMBC-DATA606-Capstone)
- **LinkedIn profile:** [linkedin.com/in/shalini-mopuri-5355182b5](https://www.linkedin.com/in/shalini-mopuri-5355182b5 )
- **Youtube Link :** https://youtu.be/yrMQhS1Um4g?feature=shared
- **Streamlit Link :** https://stock-price-prediction-606.streamlit.app/
- **PPT Link :** 

---

## Background

### What is it about?
Stock market prediction using time series analysis involves using historical stock prices and other financial indicators to forecast future stock prices. Time series analysis is crucial in understanding the temporal patterns in stock prices, trends, seasonality, and volatility. Techniques like ARIMA (Auto-Regressive Integrated Moving Average), SARIMA (Seasonal ARIMA)

### Why does it matter?

Accurately predicting stock market trends is a significant challenge in finance, offering critical insights to investors, financial analysts, and businesses. Such predictions enable informed decisions regarding buying, selling, or holding stocks, ultimately impacting portfolio returns and market strategies. Moreover, stock price volatility has broader economic implications, influencing factors like retirement savings and corporate investments. Addressing this challenge through time series analysis can enhance decision-making and contribute to financial stability


### Research Questions?

1. Can historical stock prices and financial data be used to accurately predict future stock market trends?
2. Which time series analysis model performs the best in terms of accuracy for stock market prediction?
3. Can feature selection improve the performance of predictive models in stock market analysis?



---

## Data

- **Data Sources:** 
The dataset used for this project was obtained from Yahoo Finance which contains daily stock price data for the Nifty 50 companies. The dataset covers a wide time span, making it ideal for analyzing stock market trends and predicting future stock prices.
- **Data Size:** 3MB  
- **Data Shape:** 50153 rows and 8 columns. 
- **Each Row Represents** Each row represents the daily trading activity for one of the Nifty 50 stocks, detailing price movements and trading volumes for that particular day.

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

   
