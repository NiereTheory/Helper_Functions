from datetime import date, timedelta, datetime
from calendar import monthrange

from typing import Dict, List
import pandas as pd


class DimDate(object):

    def __init__(self, start_date: date = date(2019, 1, 1), end_date: date = date(2019, 12, 31), date_int_format: str = r'%Y%m%d', date_str_format=r'%Y-%m-%d'):
        self.start_date = start_date
        self.end_date = end_date

        self.date_int_format = date_int_format
        self.date_str_format = date_str_format

        self.current_date_dict: Dict = {}

    def fns_date(self, date_id: int) -> str:
        """Convert an integer formatted date to a standard US date format"""
        return datetime.strptime(str(date_id), self.date_int_format).strftime(self.date_str_format)

    def fns_date_id(self, dt: date):
        """Convert a python date to an integer date_id"""
        return int(dt.strftime(self.date_int_format))

    def gen_dim_date(self) -> pd.DataFrame:
        """Generate a potentail dim_date table in a data warehouse"""
        delta: timedelta = self.end_date - self.start_date
        dim_date: List = []

        for i in range(delta.days + 1):
            python_date: date = self.start_date + timedelta(days=i)

            self.current_date_dict["DATE_ID"] = self.fns_date_id(python_date)

            self.current_date_dict["FULL_DATE"] = self.fns_date(
                self.current_date_dict["DATE_ID"])

            self.current_date_dict["DAY_VALUE"] = python_date.day

            self.current_date_dict["WEEKDAY_NAME"] = python_date.strftime("%A")

            self.current_date_dict["IS_WEEKDAY"] = 1 if python_date.weekday(
            ) <= 4 else 0

            self.current_date_dict["MONTH_VALUE"] = python_date.month

            self.current_date_dict["MONTH_NAME"] = python_date.strftime("%B")

            self.current_date_dict["FIRST_DAY_OF_MONTH"] = python_date.replace(
                day=1)

            monthrange(python_date.year, python_date.month)
            self.current_date_dict["LAST_DAY_OF_MONTH"] = python_date.replace(
                day=monthrange(python_date.year, python_date.month)[1]
            )

            self.current_date_dict["QUARTER_VALUE"] = (
                python_date.month - 1) // 3 + 1

            qtr_val = self.current_date_dict["QUARTER_VALUE"]
            self.current_date_dict["FIRST_DAY_OF_QUARTER"] = python_date.replace(
                month=qtr_val * 3 - 2, day=1
            )

            last_quarter_month_start = date(python_date.year, qtr_val * 3, 1)
            self.current_date_dict["LAST_DAY_OF_QUARTER"] = last_quarter_month_start.replace(
                day=monthrange(
                    last_quarter_month_start.year, last_quarter_month_start.month
                )[1]
            )

            self.current_date_dict["FIRST_DAY_OF_YEAR"] = date(
                python_date.year, 1, 1)

            self.current_date_dict["LAST_DAY_OF_YEAR"] = date(
                python_date.year, 12, 31)

            final_date_dict: Dict = {
                k: self.fns_date_id(v) if k.startswith(
                    ("FIRST", "LAST")) else v
                for k, v in self.current_date_dict.items()
            }
            dim_date.append(final_date_dict)

        return pd.DataFrame(dim_date)
