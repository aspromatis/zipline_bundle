#%%
import pickle
import pandas as pd
import pyfolio as pf


#%%
# If this was run from the Zipline Command Line, will need to process a pickle file
def process_performance(fname):
    perf = pd.read_pickle('{}.pickle'.format(fname))
    perf.to_csv('{}.csv'.format(fname))
    # Normalize the dates
    perf.index = perf.index.normalize()
    return perf

# for Pyfolio, create a benchmark to compare for the graphs
def create_benchmark(fname):
    # benchmark_rets (pd.Series, optional) -- Daily noncumulative returns of the benchmark. This is in the same style as returns.
    bench = pd.read_csv('{}.csv'.format(fname), index_col='date', parse_dates=True, date_parser=lambda col: pd.to_datetime(col, utc=True))
    # Create a series
    bench_series = pd.Series(bench['return'].values, index=bench.index)
    bench_series.rename(fname, inplace=True)
    return bench_series

# Use PyFolio to generate a performance report - benchmark_rets is optional
def analyze(perfdata, benchdata):
    returns, positions, transactions = pf.utils.extract_rets_pos_txn_from_zipline(perfdata)
    # pf.create_full_tear_sheet(returns, positions=positions, transactions=transactions, benchmark_rets=benchdata)
    pf.create_returns_tear_sheet(returns, benchmark_rets=benchdata)
