#%%
import pandas as pd
import zipline
import pytz
import numpy as np
from analysis import create_benchmark, analyze
from zipline.api import order, record, order_target_percent, symbol, schedule_function, date_rules, time_rules
from datetime import datetime
from matplotlib import pyplot as plt, ticker, rc


#%%
def initialize(context):
    # ETFs and target weights for a balanced and hedged portfolio
    context.securities = {
        'SPY': 0.25, 
        'TLT': 0.3, 
        'IEF': 0.3, 
        'GLD': 0.075, 
        'DBC': 0.075
    }
    
    # Schedule rebalance for once a month
    schedule_function(rebalance, date_rules.month_start(), time_rules.market_open())
    
    # Set up a benchmark to measure against
    context.set_benchmark(symbol('SPY'))


def rebalance(context, data):
    # Loop through the securities
    for sec, weight in context.securities.items():
        sym = symbol(sec)
        
        # Check if we can trade
        if data.can_trade(sym):
            # Reset the weight
            order_target_percent(sym, weight) 


#%%
start = pd.Timestamp('2005-1-3', tz='utc')
end = pd.Timestamp('2020-10-26', tz='utc')


# Fire off backtest
result = zipline.run_algorithm(
    start=start, # Set start
    end=end,  # Set end
    initialize=initialize, # Define startup function
    capital_base=100000, # Set initial capital
    data_frequency = 'daily',  # Set data frequency
    bundle='custom-bundle' ) # Select bundle

print("Ready to analyze result.")


#%% Create a benchmark file for Pyfolio
bench_df = pd.read_csv('data/bars_adj/SPY.csv')
bench_df['return'] = bench_df.close_adj.pct_change()
bench_df.to_csv('SPY.csv', columns=['date','return'], index=False)

#%%
# Create a benchmark dataframe
bench_series = create_benchmark('SPY')
#%%
# Filter for the dates in returns to line up the graphs - normalize cleans up the dates
result.index = result.index.normalize() # to set the time to 00:00:00
bench_series = bench_series[bench_series.index.isin(result.index)]
bench_series

#%%
# Run the tear sheet analysis
analyze(result, bench_series)


#%%
# Dump out the results to a csv
result.to_csv('result.csv')