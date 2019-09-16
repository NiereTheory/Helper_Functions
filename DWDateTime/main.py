import os
import getpass
import pandas as pd

from dim_date.dim_date import DimDate
from dim_time.dim_time import DimTime


def main():
    dd = DimDate()
    df_dd = dd.gen_dim_date()

    dt = DimTime()
    df_dt = dt.gen_dim_time()

    for df in [df_dd, df_dt]:
        try:
            destination_csv_path: str = f"/app/Data/{df.columns[0].split('_')[0]}.csv"
            df.to_csv(destination_csv_path, index=False)
            print("Process completed!")
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
