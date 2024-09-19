# Project Title: 
# Stock Market Predictions Using Time Series Analysis

- **Author Name:** Shalini Mopuri
- **Semester:** Fall 2024
- **Prepared for:** UMBC Data Science Master's Degree Capstone by Dr. Chaojie (Jay) Wang
- **GitHub:** [github.com/shaliniumbc] (https://github.com/shaliniumbc/UMBC-DATA606-Capstone)
- **LinkedIn profile:** [linkedin.com/in/shalini-mopuri-5355182b5](https://www.linkedin.com/in/shalini-mopuri-5355182b5 )   

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
The dataset used for this project was obtained from a Kaggle repository, Nifty50 Stock Market Data which contains daily stock price data for the Nifty 50 companies. The dataset covers a wide time span, making it ideal for analyzing stock market trends and predicting future stock prices.
- **Link:** https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset/data
- **Data Size:** 19MB  
- **Data Shape:** 68435 rows and 15 columns. 
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
| `Prev Close`            | Float                |  The closing price of the stock on the previous trading day.                        |
| `%change`               | Float                |  The percentage change in the stock's price compared to the previous trading day.   |
| `52w High`              | Float                |  The highest price the stock traded at in the last 52 weeks.                        |
| `52w Low`               | Float                |  The lowest price the stock traded at in the last 52 weeks.                         |
| `Deliverable Volume`    | Integer              |  The number of shares that were actually delivered on that day.                     |
| `%Deliverable`          | Float                |  The percentage of the total volume that was deliverable.                           |

---

### **Potential Values for Categorical Variables**:
- **Symbol**: Represents different stock symbols (e.g., ZEETELE). Each unique stock will have its symbol.
- **Series**: Typically "EQ" for equity, but other series types could be present depending on the dataset.


### Target Variable for the Time Series Analysis:
The **Close** column will be used as the target variable for predicting stock prices.

### Potential Features/Predictors for Time Series Analysis:
The following columns from the dataset are selected as features/predictors to predict stock prices:

-**`**VWAP (Volume Weighted Average Price)`: The average price of the stock, weighted by volume during the day.

-**`Volume`**:The number of shares traded during the day.

-**`Turnover`**: The total monetary value of shares traded during the day.

-**`Prev Close`**: The previous day's closing price.

-**`Open`**: The stock price at the opening of the trading day.

-**`High`**: The highest price during the trading day.

-**`Low`**: The lowest price during the trading day.

-**`Last`**: The last traded price before the market closes.

   



