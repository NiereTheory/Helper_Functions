import unittest

import pandas as pd

from dim_time import DimTime


class TestDimTime(unittest.TestCase):

    def setUp(self):
        self.dim_time = DimTime()

    def test_right_justify(self):
        assert self.dim_time.right_justify(3) == '03'

    def test_dim_time(self):
        df_dim_time: pd.DataFrame = self.dim_time.gen_dim_time()
        assert len(df_dim_time) == 86400

        first_time_to_test = '000430'
        first_time = pd.DataFrame(
            df_dim_time[df_dim_time.TIME_ID == first_time_to_test])
        assert first_time['TIME_ID'].values[0] == '000430'
        first_time['MILITARY_HOUR'].values[0] == '00'
        first_time['HOUR'].values[0] == '00'
        first_time['MINUTE'].values[0] == '04'
        first_time['SECOND'].values[0] == '30'
        first_time['MILITARY_COMBINED'].values[0], '00: ==4:30'
        first_time['COMBINED'].values[0], '00: ==4:30'
        first_time['AM_PM'].values[0] == 'AM'
        first_time['BUSINESS_HOUR'].values[0] == 0

        random_time_to_test = '153000'
        random_time = pd.DataFrame(
            df_dim_time[df_dim_time.TIME_ID == random_time_to_test])
        assert random_time['TIME_ID'].values[0] == '153000'
        assert random_time['MILITARY_HOUR'].values[0] == '15'
        assert random_time['HOUR'].values[0] == '03'
        assert random_time['MINUTE'].values[0] == '30'
        assert random_time['SECOND'].values[0] == '00'
        assert random_time['MILITARY_COMBINED'].values[0] == '15:30:00'
        assert random_time['COMBINED'].values[0] == '03:30:00'
        assert random_time['AM_PM'].values[0] == 'PM'
        assert random_time['BUSINESS_HOUR'].values[0] == 1


if __name__ == '__main__':
    unittest.main()
