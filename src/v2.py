from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
import backtrader as bt
from stategy import TestStrategy, MainStrategy, diff_her
import pandas as pd


modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
dat1 = os.path.join(modpath, '../data/tickers1.csv')
tickers = pd.read_csv(dat1, header=None)[1].tolist()


# Create a cerebro entity
cerebro = bt.Cerebro()
cerebro.broker.set_coc(True)
df = pd.read_csv(f"{modpath}/../data/DSEX.csv", parse_dates=True, index_col=0)
df = df.reindex(index=df.index[::-1])
cerebro.adddata(bt.feeds.PandasData(dataname=df, plot=True))

for ticker in tickers:
    df = pd.read_csv(f"{modpath}/../data/{ticker}.csv", parse_dates=True, index_col=0)
    df = df.reindex(index=df.index[::-1])
    if len(df) > 100:  # data must be long enough to compute 100 day SMA
        cerebro.adddata(bt.feeds.PandasData(dataname=df, plot=False))

cerebro.addobserver(bt.observers.Value)
cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0.0)
cerebro.addanalyzer(bt.analyzers.Returns)
cerebro.addanalyzer(bt.analyzers.DrawDown)
cerebro.addstrategy(MainStrategy)
cerebro.broker.setcash(1000000.0)
cerebro.broker.setcommission(commission=0)

# Set our desired cash start

# Print out the starting conditions
print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

results = cerebro.run()

print(f"Sharpe: {results[0].analyzers.sharperatio.get_analysis()['sharperatio']:.3f}")
print(f"Norm. Annual Return: {results[0].analyzers.returns.get_analysis()['rnorm100']:.2f}%")
print(f"Max Drawdown: {results[0].analyzers.drawdown.get_analysis()['max']['drawdown']:.2f}%")
#
# # Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

# cerebro.plot()
