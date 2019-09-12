from datetime import date, timedelta, datetime
from calendar import monthrange
import os
import sys
import getpass

import pandas as pd

date_int_format = '%Y%m%d'
date_str_format = '%Y-%m-%d'

def fns_date(date_id: int):
    """Convert an integer formatted date to a standard US date format"""
    return datetime.strptime(str(date_id), date_int_format).strftime(date_str_format)

def fns_date_id(dt: datetime):
    """Convert a python date to an integer date_id"""
    return int(dt.strftime(date_int_format))

def gen_dim_date(start_date=date(2019, 1, 1), end_date=date(2019, 12, 31)):
    """Generate a potentail dim_date table in a data warehouse"""
    delta = end_date - start_date
    dim_date = []

    for i in range(delta.days + 1):
        current_date_dict = {}
        python_date = start_date + timedelta(days=i)
        # current_date_dict['PYTHON_DATE'] = python_date
        
        current_date_dict['DATE_ID'] = fns_date_id(python_date)
        
        current_date_dict['FULL_DATE'] = fns_date(current_date_dict['DATE_ID'])

        current_date_dict['DAY_VALUE'] = python_date.day

        current_date_dict['WEEKDAY_NAME'] = python_date.strftime('%A')

        current_date_dict['IS_WEEKDAY'] = 1 if python_date.weekday() <= 4 else 0

        current_date_dict['MONTH_VALUE'] = python_date.month

        current_date_dict['MONTH_NAME'] = python_date.strftime('%B')

        current_date_dict['FIRST_DAY_OF_MONTH'] = python_date.replace(day=1)
        
        monthrange(python_date.year, python_date.month)
        current_date_dict['LAST_DAY_OF_MONTH'] = python_date. \
            replace(day=monthrange(python_date.year, python_date.month)[1])

        current_date_dict['QUARTER_VALUE'] = (python_date.month - 1) // 3 + 1
        
        qtr_val = current_date_dict['QUARTER_VALUE']
        current_date_dict['FIRST_DAY_OF_QUARTER'] = python_date. \
            replace(month=qtr_val * 3 - 2, day=1)
        
        last_quarter_month_start = date(python_date.year, qtr_val * 3, 1)
        current_date_dict['LAST_DAY_OF_QUARTER'] = last_quarter_month_start. \
                replace(day=monthrange(last_quarter_month_start.year, last_quarter_month_start.month)[1])

        current_date_dict['FIRST_DAY_OF_YEAR'] = date(python_date.year, 1, 1)
        
        current_date_dict['LAST_DAY_OF_YEAR'] = date(python_date.year, 12, 31)

        final_date_dict = {k: fns_date_id(v) if k.startswith(('FIRST', 'LAST')) else v for k, v in current_date_dict.items()}
        dim_date.append(final_date_dict)

    return dim_date

if __name__ == '__main__':
    try:
        destination_csv_path = os.path.join(*['/Users', getpass.getuser(), 'Projects/Helper_Functions/dim_date/dim_date.csv'])
        pd.DataFrame(gen_dim_date()).to_csv(destination_csv_path, index=False)
        print('Process completed!')
    except Exception as e:
        print(f'Error occurred: {e}')