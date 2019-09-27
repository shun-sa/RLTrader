import ta
import pandas as pd

diff = lambda x, y: x - y
abs_diff = lambda x, y: abs(x - y)


indicators = [
    ('RSI', ta.rsi, ['Close']),
    ('MFI', ta.money_flow_index, ['High', 'Low', 'Close', 'Volume']),
    ('TSI', ta.tsi, ['Close']),
    ('UO', ta.uo, ['High', 'Low', 'Close']),
    ('AO', ta.ao, ['High', 'Close']),
    ('MACDDI', ta.macd_diff, ['Close']),
    ('VIP', ta.vortex_indicator_pos, ['High', 'Low', 'Close']),
    ('VIN', ta.vortex_indicator_neg, ['High', 'Low', 'Close']),
    ('VIDIF', abs_diff, ['VIP', 'VIN']),
    ('TRIX', ta.trix, ['Close']),
    ('MI', ta.mass_index, ['High', 'Low']),
    ('CCI', ta.cci, ['High', 'Low', 'Close']),
    ('DPO', ta.dpo, ['Close']),
    ('KST', ta.kst, ['Close']),
    ('KSTS', ta.kst_sig, ['Close']),
    ('KSTDI', diff, ['KST', 'KSTS']),
    ('ARU', ta.aroon_up, ['Close']),
    ('ARD', ta.aroon_down, ['Close']),
    ('ARI', diff, ['ARU', 'ARD']),
    ('BBH', ta.bollinger_hband, ['Close']),
    ('BBL', ta.bollinger_lband, ['Close']),
    ('BBM', ta.bollinger_mavg, ['Close']),
    ('BBHI', ta.bollinger_hband_indicator, ['Close']),
    ('BBLI', ta.bollinger_lband_indicator, ['Close']),
    ('KCHI', ta.keltner_channel_hband_indicator, ['High', 'Low', 'Close']),
    ('KCLI', ta.keltner_channel_lband_indicator, ['High', 'Low', 'Close']),
    ('DCHI', ta.donchian_channel_hband_indicator, ['Close']),
    ('DCLI', ta.donchian_channel_lband_indicator, ['Close']),
    ('ADI', ta.acc_dist_index, ['High', 'Low', 'Close', 'Volume']),
    ('OBV', ta.on_balance_volume, ['Close', 'Volume']),
    ('CMF', ta.chaikin_money_flow, ['High', 'Low', 'Close', 'Volume']),
    ('FI', ta.force_index, ['Close', 'Volume']),
    ('EM', ta.ease_of_movement, ['High', 'Low', 'Close', 'Volume']),
    ('VPT', ta.volume_price_trend, ['Close', 'Volume']),
    ('NVI', ta.negative_volume_index, ['Close', 'Volume']),
    ('DR', ta.daily_return, ['Close']),
    ('DLR', ta.daily_log_return, ['Close'])
]


def get_indicators_len():
    return 0
    features = []
    for name, f in indicators_talib:
        features += f.output_flags

    return len(indicators)


def add_indicators_from_talib(df):
    df2 = df.iloc[:,:6]
    df2.columns = [col.lower() for col in df2.columns]

    for name, f in indicators_talib:
        print(df2)
        dfadd = f(df2)

        if len(dfadd.shape)==1:
            df[name]=float(dfadd)
        else:
            for i in dfadd.columns:
                df[name+i]=float(dfadd[i])

    return df


def add_indicators(df) -> pd.DataFrame:
    # if len(df) >15: return ta.add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume", fillna=True)
    # print (len(df))
    wrapper = lambda func, args: func(*args)
    for name, f, arg_names in indicators:
        args = [df[arg_name] for arg_name in arg_names]
        df[name] = wrapper(f, args)
    df.fillna(method='bfill', inplace=True)
    return df
