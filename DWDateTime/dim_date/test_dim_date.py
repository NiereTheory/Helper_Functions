import unittest
from datetime import date

import pandas as pd

from dim_date import DimDate


class TestDimDate(unittest.TestCase):

    def setUp(self):
        self.dim_date = DimDate(date_str_format=r'%Y-%m-%d')

    def test_fns_date(self):
        assert self.dim_date.fns_date(20190101) == '2019-01-01'

    def test_fns_date_id(self):
        assert self.dim_date.fns_date_id(date(2019, 1, 1)) == 20190101

    def test_dim_date(self):
        df_dim_date = self.dim_date.gen_dim_date()
        assert len(df_dim_date) == 365

        first_day_to_test = 20190101
        first_day = pd.DataFrame(
            df_dim_date[df_dim_date.DATE_ID == first_day_to_test])
        assert first_day['DATE_ID'].values[0] == 20190101
        assert first_day['FULL_DATE'].values[0] == '2019-01-01'
        assert first_day['DAY_VALUE'].values[0] == 1
        assert first_day['WEEKDAY_NAME'].values[0] == 'Tuesday'
        assert first_day['IS_WEEKDAY'].values[0] == 1
        assert first_day['MONTH_VALUE'].values[0] == 1
        assert first_day['MONTH_NAME'].values[0] == 'January'
        assert first_day['FIRST_DAY_OF_MONTH'].values[0] == 20190101
        assert first_day['LAST_DAY_OF_MONTH'].values[0] == 20190131
        assert first_day['QUARTER_VALUE'].values[0] == 1
        assert first_day['FIRST_DAY_OF_QUARTER'].values[0] == 20190101
        assert first_day['LAST_DAY_OF_QUARTER'].values[0] == 20190331
        assert first_day['FIRST_DAY_OF_YEAR'].values[0] == 20190101
        assert first_day['LAST_DAY_OF_YEAR'].values[0] == 20191231

        random_day = df_dim_date[df_dim_date.DATE_ID == 20190720]
        assert random_day['DATE_ID'].values[0] == 20190720
        assert random_day['FULL_DATE'].values[0] == '2019-07-20'
        assert random_day['DAY_VALUE'].values[0] == 20
        assert random_day['WEEKDAY_NAME'].values[0] == 'Saturday'
        assert random_day['IS_WEEKDAY'].values[0] == 0
        assert random_day['MONTH_VALUE'].values[0] == 7
        assert random_day['MONTH_NAME'].values[0] == 'July'
        assert random_day['FIRST_DAY_OF_MONTH'].values[0] == 20190701
        assert random_day['LAST_DAY_OF_MONTH'].values[0] == 20190731
        assert random_day['QUARTER_VALUE'].values[0] == 3
        assert random_day['FIRST_DAY_OF_QUARTER'].values[0] == 20190701
        assert random_day['LAST_DAY_OF_QUARTER'].values[0] == 20190930
        assert random_day['FIRST_DAY_OF_YEAR'].values[0] == 20190101
        assert random_day['LAST_DAY_OF_YEAR'].values[0] == 20191231


if __name__ == '__main__':
    unittest.main()
