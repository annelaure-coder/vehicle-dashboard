import pandas as pd
import plotly.express as px


def frequency_table(df):
    counts = df["manufacturer"].value_counts().reset_index()
    counts.columns = ["Manufacturer", "Count"]
    return counts.to_html(
        classes="table table-bordered table-striped table-sm",
        float_format="%.2f",
        justify="center",
        index=False,
    )


def manufacturer_chart(df):
    counts = df["manufacturer"].value_counts().reset_index()
    counts.columns = ["Manufacturer", "Count"]
    fig = px.bar(counts, x="Manufacturer", y="Count", color="Manufacturer",
                 title="Vehicles by Manufacturer")
    fig.update_layout(showlegend=False, margin=dict(l=20, r=20, t=50, b=20))
    return fig.to_html(full_html=False, include_plotlyjs="cdn")
