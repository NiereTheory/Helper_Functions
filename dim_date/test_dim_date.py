import unittest
from datetime import date

import pandas as pd

from dim_date import DimDate


class TestDimDate(unittest.TestCase):

    def setUp(self):
        self.dim_date = DimDate()

    def test_fns_date(self):
        print('My val is:', self.dim_date.date_int_format)
        self.assertEqual(self.dim_date.fns_date(20190101), '2019-01-01')

    def test_fns_date_id(self):
        self.assertEqual(self.dim_date.fns_date_id(date(2019, 1, 1)), 20190101)

    def test_dim_date(self):
        df_dim_date = self.dim_date.gen_dim_date()
        self.assertEqual(len(df_dim_date), 365)

        first_day_to_test = 20190101
        first_day = pd.DataFrame(
            df_dim_date[df_dim_date.DATE_ID == first_day_to_test])
        self.assertEqual(first_day['DATE_ID'].values[0], 20190101)
        self.assertEqual(first_day['FULL_DATE'].values[0], '2019-01-01')
        self.assertEqual(first_day['DAY_VALUE'].values[0], 1)
        self.assertEqual(first_day['WEEKDAY_NAME'].values[0], 'Tuesday')
        self.assertEqual(first_day['IS_WEEKDAY'].values[0], 1)
        self.assertEqual(first_day['MONTH_VALUE'].values[0], 1)
        self.assertEqual(first_day['MONTH_NAME'].values[0], 'January')
        self.assertEqual(first_day['FIRST_DAY_OF_MONTH'].values[0], 20190101)
        self.assertEqual(first_day['LAST_DAY_OF_MONTH'].values[0], 20190131)
        self.assertEqual(first_day['QUARTER_VALUE'].values[0], 1)
        self.assertEqual(first_day['FIRST_DAY_OF_QUARTER'].values[0], 20190101)
        self.assertEqual(first_day['LAST_DAY_OF_QUARTER'].values[0], 20190331)
        self.assertEqual(first_day['FIRST_DAY_OF_YEAR'].values[0], 20190101)
        self.assertEqual(first_day['LAST_DAY_OF_YEAR'].values[0], 20191231)

        random_day = df_dim_date[df_dim_date.DATE_ID == 20190720]
        self.assertEqual(random_day['DATE_ID'].values[0], 20190720)
        self.assertEqual(random_day['FULL_DATE'].values[0], '2019-07-20')
        self.assertEqual(random_day['DAY_VALUE'].values[0], 20)
        self.assertEqual(random_day['WEEKDAY_NAME'].values[0], 'Saturday')
        self.assertEqual(random_day['IS_WEEKDAY'].values[0], 0)
        self.assertEqual(random_day['MONTH_VALUE'].values[0], 7)
        self.assertEqual(random_day['MONTH_NAME'].values[0], 'July')
        self.assertEqual(random_day['FIRST_DAY_OF_MONTH'].values[0], 20190701)
        self.assertEqual(random_day['LAST_DAY_OF_MONTH'].values[0], 20190731)
        self.assertEqual(random_day['QUARTER_VALUE'].values[0], 3)
        self.assertEqual(random_day['FIRST_DAY_OF_QUARTER'].values[0], 20190701)
        self.assertEqual(random_day['LAST_DAY_OF_QUARTER'].values[0], 20190930)
        self.assertEqual(random_day['FIRST_DAY_OF_YEAR'].values[0], 20190101)
        self.assertEqual(random_day['LAST_DAY_OF_YEAR'].values[0], 20191231)


if __name__ == '__main__':
    unittest.main()
