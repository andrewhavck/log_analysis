import pandas as pd
from random import randint

from bokeh.plotting import output_file, figure, show


def __aggregate_status_data(source):
    dateparse = lambda x: pd.to_datetime(x, unit='s')
    df = pd.read_table(source,
                       index_col=[0],
                       usecols=[1, 3],
                       date_parser=dateparse)

    df.columns = ['status']
    df['status'] = df['status'].astype(str)
    df['hits'] = 1

    grouped = df.groupby(['status']).resample('2Min', fill_method='ffill', how='sum')
    grouped = grouped['hits'].to_frame()
    avgs = grouped.groupby(level=0).apply(pd.rolling_mean, 2, min_periods=1)
    avgs = avgs.reset_index()
    avgs.columns = ['status', 'time', 'hits']
    return avgs


def create_status_chart(source):
    avgs = __aggregate_status_data(source)
    output_file("status_codes.html")

    p = figure(width=800,
               height=400,
               tools="pan",
               title="http response codes",
               y_axis_label="# of responses",
               y_axis_type="log",
               y_range=(10 ** 0, 10 ** 4),
               x_axis_label="time",
               x_axis_type="datetime")

    for status in pd.unique(avgs['status']):
        data = avgs.loc[avgs['status'] == status]
        p.line(data['time'],
               data['hits'],
               color='#%06X' % randint(0, 0xFFFFFF),
               alpha=0.5,
               line_width=3,
               legend='Code ' + status)
    show(p)
