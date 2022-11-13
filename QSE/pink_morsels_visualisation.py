import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

colors = {
    'background': '#111111',
    "secondary": "red",
    'text': '#FEDBFF',
    'line': '#522A61'
}

DATA_FILE_PATH = "./data/output.csv"

df = pd.read_csv(DATA_FILE_PATH)
df = df.sort_values(by="date")

app = Dash(__name__)


def generate_fig(data):
    fig = px.line(data, x="date", y="sales", title="Pink Morsel Sales Plot")
    fig.update_layout(
        plot_bgcolor=colors["background"],
        paper_bgcolor=colors["background"],
        font_color=colors["text"]
    )
    return fig


header = html.H1(
    "Soul Foods",
    id="header",
    style={
        'textAlign': 'center',
        'color': colors['text']
    })

subheader = html.H2(
    "Pink Morsel Sales",
    id="subheader",
    style={
        "background-color": colors["background"],
        "color": colors["text"],
        "border-radius": "20px"
    })

plot = dcc.Graph(id="plot", figure=generate_fig(df))

region_picker = dcc.RadioItems(
    ["north", "east", "south", "west", "all"],
    "north",
    id="region_picker",
    inline=True
)
region_picker_wrapper = html.Div(
    [region_picker],
    style={
        "font-size": "120%",
        'color': '#FEDBFF'
    }
)


@app.callback(
    Output(plot, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    if region == "all":
        trimmed_data = df
    else:
        trimmed_data = df[df["region"] == region]
    figure = generate_fig(trimmed_data)
    return figure


app.layout = html.Div(
    style={'backgroundColor': colors['background'], "textAlign": "center"},
    children=[
        header,
        subheader,
        plot,
        region_picker_wrapper
    ])

if __name__ == '__main__':
    app.run_server()
