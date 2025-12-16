import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce").fillna(0)
    df["size"] = pd.to_numeric(df["size"], errors="coerce").fillna(0)
    df.dropna(subset=["name", "region"], inplace=True)
    return df


def aggregate_data(df: pd.DataFrame) -> dict:
    aggregations = {}
    aggregations["sales_by_region"] = (
        df.groupby("region")["sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    aggregations["sales_by_firmness"] = (
        df.groupby("firmness")["sales"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )

    bins = [0, 20, 50, 100, 200, 1000]
    labels = ["Tiny", "Small", "Medium", "Large", "Giant"]
    df["size_category"] = pd.cut(df["size"], bins=bins, labels=labels)
    aggregations["sales_by_size"] = (
        df.groupby("size_category", observed=False)["sales"].sum().reset_index()
    )

    flavor_data = []
    for _, row in df.iterrows():
        sales = row["sales"]
        flavors_list = row["flavors"]
        if isinstance(flavors_list, str):
            try:
                import ast

                flavors_list = ast.literal_eval(flavors_list)
            except:
                flavors_list = []

        if isinstance(flavors_list, list):
            for f_str in flavors_list:
                if ":" in f_str:
                    flavor_name, potency = f_str.split(":")
                    potency = int(potency.strip())
                    if potency > 0:
                        flavor_data.append(
                            {"flavor": flavor_name.strip(), "sales": sales}
                        )

    if flavor_data:
        df_flavor = pd.DataFrame(flavor_data)
        aggregations["sales_by_flavor"] = (
            df_flavor.groupby("flavor")["sales"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )
    else:
        aggregations["sales_by_flavor"] = pd.DataFrame(
            columns=["flavor", "sales"]
        )

    return aggregations


def get_insights(df: pd.DataFrame, aggregations: dict = None) -> pd.DataFrame:
    insights = []

    top_region = df.groupby("region")["sales"].sum().idxmax()
    top_region_sales = df.groupby("region")["sales"].sum().max()
    insights.append(
        {
            "Metric": "Top Region",
            "Value": top_region,
            "Details": f"Sales: {top_region_sales}",
        }
    )

    top_berry = df.groupby("name")["sales"].sum().idxmax()
    top_berry_sales = df.groupby("name")["sales"].sum().max()
    insights.append(
        {
            "Metric": "Top Berry",
            "Value": top_berry,
            "Details": f"Sales: {top_berry_sales}",
        }
    )

    if (
        aggregations
        and "sales_by_flavor" in aggregations
        and not aggregations["sales_by_flavor"].empty
    ):
        top_flavor_row = aggregations["sales_by_flavor"].iloc[0]
        insights.append(
            {
                "Metric": "Top Flavor",
                "Value": top_flavor_row["flavor"],
                "Details": f"Sales: {top_flavor_row['sales']}",
            }
        )

    avg_sales = df["sales"].mean()
    insights.append(
        {
            "Metric": "Average Sales per Entry",
            "Value": f"{avg_sales:.2f}",
            "Details": "",
        }
    )

    return pd.DataFrame(insights)


def process(df: pd.DataFrame) -> dict:
    df = clean_data(df)
    aggs = aggregate_data(df)
    insights = get_insights(df, aggs)

    result = aggs.copy()
    result["insights"] = insights
    return result


def main():
    import extract

    df = extract.extract()
    results = process(df)
    for k, v in results.items():
        print(f"--- {k} ---")
        print(v)
        print("\n")


if __name__ == "__main__":
    main()
