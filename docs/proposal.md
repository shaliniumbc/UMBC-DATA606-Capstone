# Project Title: 
# Future Trends: Enhancing Stock Market Predictions Using Machine Learning

- **Author Name:** Shalini Mopuri
- **Semester:** Fall 2024
- **Prepared for:** UMBC Data Science Master's Degree Capstone by Dr. Chaojie (Jay) Wang
- **GitHub:** [github.com/shaliniumbc] (https://github.com/shaliniumbc/UMBC-DATA606-Capstone)
- **LinkedIn profile:** [linkedin.com/in/shalini-mopuri-5355182b5](https://www.linkedin.com/in/shalini-mopuri-5355182b5 )   

---

## Background

### What is it about?

The project aims to enhance stock market predictions using machine learning techniques. Stock market forecasts have always been very speculative, based on historical trends, financial news, and expert opinions. Machine learning is a powerful tool for making more accurate and efficient predictions about how stock prices will evolve. It can process large amounts of data and discover hidden trends.

### Why does it matter?

Accurate stock market predictions significantly benefit investors, financial experts, and hedge funds. Predictive accuracy can help with investment strategies, risk management, and general financial decision-making. Furthermore, given the dynamic and turbulent nature of stock markets, applying machine learning provides a modern method for addressing these challenges in a more data-driven approach.


### Research Questions?

1. Can machine learning models outperform traditional statistical methods in stock market prediction?
2. What are the key features that most significantly impact stock price movements?
3. How does the time horizon (short-term vs. long-term prediction) affect model accuracy?


---

## Data

- **Data Sources:** 
The dataset used for this project was obtained from a Kaggle repository, which contains daily stock price data for the Nifty 50 companies. The dataset covers a wide time span, making it ideal for analyzing stock market trends and predicting future stock prices.
- **Data Size:** 19MB  
- **Data Shape:** rows and 15 columns.  
- **Time Period:** The dataset covers the period from 2000 to 2021, capturing daily trading data.

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


### Target Variable for the ML Model:
The **Close** and **Adj Close** columns will be used as the target variable for predicting stock prices.

### Potential Features/Predictors for the ML Models
The following columns from the dataset are selected as features/predictors for building a machine learning model to predict stock prices:

**`**VWAP (Volume Weighted Average Price)`: The average price of the stock, weighted by volume during the day.
**`Volume`**:The number of shares traded during the day.
**`Turnover`**: The total monetary value of shares traded during the day.
**`Prev Close`**: The previous day's closing price.
**`Open`**: The stock price at the opening of the trading day.
**`High`**: The highest price during the trading day.
**`Low`**: The lowest price during the trading day.
**`Last`**: The last traded price before the market closes.

   



