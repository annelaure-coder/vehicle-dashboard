import pandas as pd


def filter_by_price(df, min_price=5000, column="selling_price"):
    """Select all cars bought for more than min_price."""
    return df[df[column] > min_price]


def frequency_table(df):
    """Manufacturer and Count (all cars)."""
    counts = df["manufacturer"].value_counts().reset_index()
    counts.columns = ["Manufacturer", "Count"]
    return counts.to_html(
        classes="table table-bordered table-striped table-sm",
        justify="center",
        index=False,
    )


def full_table(df):
    """Every column and row of the data given."""
    return df.to_html(
        classes="table table-bordered table-striped table-sm",
        justify="center",
        index=False,
    )


def sales_by_transmission(df):
    """Total selling price for each manufacturer and transmission type."""
    totals = df.groupby(["manufacturer", "transmission"])["selling_price"].sum()
    totals = totals.to_frame("total_selling_price")
    return totals.to_html(
        classes="table table-bordered table-striped table-sm",
        justify="center",
    )