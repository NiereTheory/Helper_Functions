import os
import getpass

from dim_date import DimDate


def main():
    dd = DimDate()
    df = dd.gen_dim_date()

    try:
        destination_csv_path: str = os.path.join(
            *["/Users", getpass.getuser(), "Projects/Helper_Functions/dim_date/dim_date.csv"]
        )
        df.to_csv(destination_csv_path, index=False)
        print("Process completed!")
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
