# Ingesting Your Own Zipline Data Bundle

This code will format stock pricing history in the format of daily bars including OHLCV (Open, High, Low, Close, Volume) data.  The bars will be adjusted for stock splits.  Dividend data will also be appended for a complete view of returns.  

The files will be formatted as CSV files and will then utilize the Zipline csvdir.py process to read in the files as a new data bundle.

For this project, I source my data from Polygon.io.  You can sign up for an API key at [Polygon.io](https://polygon.io/).

Alternatively, you can use your [Alpaca](https://alpaca.markets/) Trading API key to get free access to Polygon data.

## Requirements

For instruction on how to set up your own virtual environment, go to my other project folder on [GitHub](https://github.com/aspromatis/Backtesting-RSI-Algo)

For information on how to pull stock data from Polygon.io, go to my other project folder on [GitHub](https://github.com/aspromatis/polygon_api)

Here is a link to the [Zipline documentation](https://www.zipline.io/bundles.html) as well as to the [Zipline GitHub page](https://github.com/quantopian/zipline)

## Process

You will need to update your csvdir.py file, located at:

`zip35/lib/python3.5/site-packages/zipline/data/bundles/csvdir.py`

To run the ingest program, you will need to register your data in the extension.py file located in your home directory (typically your user name, press shift-cmd-. to reveal hidden files in finder on Mac):

`.zipline/extension.py`

The file prepare_bundle.py is the code that will format your OHLCV, split, and dividend data into the format needed by the zipline csvdir.py process

The file get_trading_days.py is the code that will grab the trading days of the New York Stock Exchange for the date range you are looking for

The Command to run the zipline data bundle ingest process (run this in your terminal for the proper environment)

`$ zipline ingest -b custom-bundle`

To view the new bundle:

`$ zipline bundles`

The Zipline program will save the data in the .zipline/data directory.  You can use [DB Browser](https://sqlitebrowser.org/) to view some of the files.

The Asset Allocation example program was primarily writen by Andreas Clenow in the book Trading Evolved, with a few modification by me.  I recommend his book if you want to learn more about algo-trading.

Note, I'm using VS Code with the ipykernel (Jupyter Notebook) capability to run in a notebook like experience.  You can certainly also run this without this.

Additional instructions on my [YouTube channel](https://www.youtube.com/c/ErolAspromatis)