import pandas as pd
from django.conf import settings
from django.shortcuts import render

from .dashboard import filter_by_price, frequency_table, full_table,  sales_by_transmission



def dashboard_view(request):
    df = pd.read_csv(settings.BASE_DIR / "dummy_data" / "vehicles_data_1000.csv")

    filtered_df = filter_by_price(df, 5000, column="selling_price")

    return render(request, "vehicles/index.html", {
        "frequency_table": frequency_table(df),
        "filtered_table": full_table(filtered_df),
        "filtered_count": len(filtered_df),
        "sales_table": sales_by_transmission(df),
    })