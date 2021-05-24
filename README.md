# Using Python to Backtest and Evaluate Trading Strategies in the Dhaka Stock Exchange

![Group 4 (3)](https://user-images.githubusercontent.com/2813022/119393625-01e82d00-bcf3-11eb-8d7a-dae8224a4559.png)


# What is this?

This was my final year project for IBA, University of Dhaka.

I look at how a momentum trading strategy would perform in the Dhaka Stock Exchange, the main bourse of Bangladesh, over a three year period. 

# Long story short

Which benchmark index will be followed? For what time period? Why? Which publicly listed companies will we trade? What are the rules of our trading strategy? How will we evaluate performance? To put it succinctly, we used the DSEX broad index and used 26 stocks out of those listed in the DSE30 list. The rules of our strategy include trading once a week, ranking stocks in the DSEX based on momentum and then buying or selling the top/bottom 3 stocks. 

We only opened new positions if the DSEX was above its 200-day moving average. Since the market was bearish during the 2014-16 time period, we saw many trades cancelled. 

The results show that momentum strategy performs suboptimally for this dataset. It yields an annual return of 2.11% (DSEX CAGR is 8.4%) with a max drawdown of around 34% (High). The Sharpe ratio was less than 0.2, which indicates taking on high risk for insignificant returns. 
A future iteration of this research may be performed with a bullish dataset. Other parameters and filters may be altered to yield better results. 

To summarize the findings:
- As we can see the momentum strategy performs suboptimally for this dataset.  
- It makes an average of 2.11% a year with a max drawdown of around 34%. 
- The DSEX outperforms the algorithm over this time period (CAGR of 8.4%) 
- The algorithm does so with more volatility (Max Drawdown of 34.98%, Sharpe of ~0.2).
- Overall, this algorithm provides a good base for a momentum strategy and can likely be improved by altering time periods, parameters, applying filters, and adding leverage. 

![Screenshot 2021-05-25 at 01 08 02](https://user-images.githubusercontent.com/2813022/119395732-c6029700-bcf5-11eb-8275-fc68e7b1562e.png)


# Packages Used

[Backtrader](https://www.backtrader.com/)
backtrader allows you to focus on writing reusable trading strategies, indicators and analyzers instead of having to spend time building infrastructure.

# Notes 

The report (which is *not* attached here) starts by introducing the role of capital markets in the economy, then expanding upon concepts like trading strategies and backtesting. In simple terms, backtesting a trading strategy is the process of testing a trading hypothesis/strategy on prior time periods – something we will be doing for our report. 

Then we briefly reviewed the history of the Dhaka Stock Exchange as well as notable rallies and crashes in the stock market over the past few decades. We explained why and how stock markets crash and differentiated between bull and bear market conditions. All of this was necessary to set context for our task of applying a momentum strategy. 
