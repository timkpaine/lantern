import io
import requests
import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, ResizeTool, SaveTool
from bokeh.models.widgets import TextInput, Button
from bokeh.plotting import figure, curdoc
from bokeh.layouts import row, widgetbox


TICKER = ""
base = "https://api.iextrading.com/1.0/"
data = ColumnDataSource(dict(time=[], display_time=[], price=[]))


def get_last_price(symbol):
    payload = {
        "format": "csv",
        "symbols": symbol
    }
    endpoint = "tops/last"

    raw = requests.get(base + endpoint, params=payload)
    raw = io.BytesIO(raw.content)
    prices_df = pd.read_csv(raw, sep=",")
    prices_df["time"] = pd.to_datetime(prices_df["time"], unit="ms")
    prices_df["display_time"] = prices_df["time"].dt.strftime("%m-%d-%Y %H:%M:%S.%f")

    return prices_df

def update_ticker():
    global TICKER
    TICKER = ticker_textbox.value
    price_plot.title.text = "IEX Real-Time Price: " + ticker_textbox.value
    data.data = dict(time=[], display_time=[], price=[])

    return

def update_price():
    new_price = get_last_price(symbol=TICKER)
    data.stream(dict(time=new_price["time"],
                     display_time=new_price["display_time"],
                     price=new_price["price"]), 10000)
    return


hover = HoverTool(tooltips=[
    ("Time", "@display_time"),
    ("IEX Real-Time Price", "@price")
    ])

price_plot = figure(plot_width=800,
                    plot_height=400,
                    x_axis_type='datetime',
                    tools=[hover, ResizeTool(), SaveTool()],
                    title="Real-Time Price Plot")

price_plot.line(source=data, x='time', y='price')
price_plot.xaxis.axis_label = "Time"
price_plot.yaxis.axis_label = "IEX Real-Time Price"
price_plot.title.text = "IEX Real Time Price: " + TICKER

ticker_textbox = TextInput(placeholder="Ticker")
update = Button(label="Update")
update.on_click(update_ticker)

inputs = widgetbox([ticker_textbox, update], width=200)

curdoc().add_root(row(inputs, price_plot, width=1600))
curdoc().title = "Real-Time Price Plot from IEX"
curdoc().add_periodic_callback(update_price, 1000)
