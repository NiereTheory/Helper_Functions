import sys

from table_generator import TableGenerator

# call with: python main.py Source.db test_tbl


def main():
    with TableGenerator(sys.argv[1], sys.argv[2]) as tg:
        print(f"{tg.get_row_count()}")
        print(f"{tg.get_tbl_schema()}")
        print(f"{tg.export_data()}")


if __name__ == "__main__":
    main()
