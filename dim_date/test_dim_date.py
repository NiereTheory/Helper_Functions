import unittest
from generate_dim_date import fns_date, fns_date_id, gen_dim_date
from datetime import date
"""test with `python -m unittest discover .`"""

class TestDimDate(unittest.TestCase):

    def setUp(self):
        self.dim_date = gen_dim_date()

    def test_fns_date(self):
        self.assertEqual(fns_date(20190101), '2019-01-01')

    def test_fns_date_id(self):
        self.assertEqual(fns_date_id(date(2019, 1, 1)), 20190101)

    def test_dim_date(self):
        self.assertEqual(len(self.dim_date), 365)
        
        first_day = self.dim_date[0]
        self.assertEqual(first_day['DATE_ID'], 20190101)
        self.assertEqual(first_day['FULL_DATE'], '2019-01-01')
        self.assertEqual(first_day['DAY_VALUE'], 1)
        self.assertEqual(first_day['WEEKDAY_NAME'], 'Tuesday')
        self.assertEqual(first_day['IS_WEEKDAY'], 1)
        self.assertEqual(first_day['MONTH_VALUE'], 1)
        self.assertEqual(first_day['MONTH_NAME'], 'January')
        self.assertEqual(first_day['FIRST_DAY_OF_MONTH'], 20190101)
        self.assertEqual(first_day['LAST_DAY_OF_MONTH'], 20190131)
        self.assertEqual(first_day['QUARTER_VALUE'], 1)
        self.assertEqual(first_day['FIRST_DAY_OF_QUARTER'], 20190101)
        self.assertEqual(first_day['LAST_DAY_OF_QUARTER'], 20190331)
        self.assertEqual(first_day['FIRST_DAY_OF_YEAR'], 20190101)
        self.assertEqual(first_day['LAST_DAY_OF_YEAR'], 20191231)

        random_day = [d for d in self.dim_date if d['DATE_ID'] == 20190720][0]
        self.assertEqual(random_day['DATE_ID'], 20190720)
        self.assertEqual(random_day['FULL_DATE'], '2019-07-20')
        self.assertEqual(random_day['DAY_VALUE'], 20)
        self.assertEqual(random_day['WEEKDAY_NAME'], 'Saturday')
        self.assertEqual(random_day['IS_WEEKDAY'], 0)
        self.assertEqual(random_day['MONTH_VALUE'], 7)
        self.assertEqual(random_day['MONTH_NAME'], 'July')
        self.assertEqual(random_day['FIRST_DAY_OF_MONTH'], 20190701)
        self.assertEqual(random_day['LAST_DAY_OF_MONTH'], 20190731)
        self.assertEqual(random_day['QUARTER_VALUE'], 3)
        self.assertEqual(random_day['FIRST_DAY_OF_QUARTER'], 20190701)
        self.assertEqual(random_day['LAST_DAY_OF_QUARTER'], 20190930)
        self.assertEqual(random_day['FIRST_DAY_OF_YEAR'], 20190101)
        self.assertEqual(random_day['LAST_DAY_OF_YEAR'], 20191231)

if __name__ == '__main__':
    unittest.main()