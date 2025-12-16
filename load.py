import pandas as pd


def load_to_excel(data: dict, filename: str = "sales_report.xlsx") -> None:
    try:
        with pd.ExcelWriter(filename, engine="openpyxl") as writer:
            for sheet_name, df in data.items():
                valid_sheet_name = sheet_name[:31]
                df.to_excel(writer, sheet_name=valid_sheet_name, index=False)
        print(f"Successfully created {filename}")
    except Exception as e:
        print(f"Error creating Excel file: {e}")


if __name__ == "__main__":
    try:
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        load_to_excel({"test_sheet": df})
    except ImportError:
        print("Pandas or openpyxl not installed.")
