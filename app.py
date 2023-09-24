import vectorbt as vbt

data_exchange = 'binanceusdm'
data_timeframe = '15m'
data_start = '2023-05-01'
data_end = '2023-08-31'
btc_price = vbt.CCXTData.download_symbol('BTC/USDT', exchange=data_exchange, timeframe=data_timeframe, start=data_start, end=data_end)
eth_price = vbt.CCXTData.download_symbol('ETH/USDT', exchange=data_exchange, timeframe=data_timeframe, start=data_start, end=data_end)
