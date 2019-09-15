import pandas as pd
from typing import List, Dict


class DimTime():
    def __init__(self):
        pass

    def right_justify(self, num: int) -> str:
        return str(num).rjust(2, '0')

    def gen_dim_time(self) -> pd.DataFrame:
        dim_time: List = []

        for hour in range(24):
            for minute in range(60):
                for second in range(60):
                    current_time_dict: Dict = {}
                    current_time_dict["TIME_ID"] = ''.join([self.right_justify(hour), self.right_justify(
                        minute), self.right_justify(second)])
                    current_time_dict["MILITARY_HOUR"] = self.right_justify(
                        hour)
                    current_time_dict["HOUR"] = current_time_dict["MILITARY_HOUR"] if int(current_time_dict[
                        "MILITARY_HOUR"]) < 13 else self.right_justify(int(current_time_dict["MILITARY_HOUR"]) - 12)  # walrus operator would be nice
                    current_time_dict["MINUTE"] = self.right_justify(minute)
                    current_time_dict["SECOND"] = self.right_justify(second)
                    current_time_dict["MILITARY_COMBINED"] = ':'.join(
                        [current_time_dict["MILITARY_HOUR"], current_time_dict["MINUTE"], current_time_dict["SECOND"]])
                    current_time_dict["COMBINED"] = ':'.join(
                        [current_time_dict["HOUR"], current_time_dict["MINUTE"], current_time_dict["SECOND"]])
                    current_time_dict["AM_PM"] = "AM" if int(
                        current_time_dict["MILITARY_HOUR"]) < 12 else "PM"
                    current_time_dict["BUSINESS_HOUR"] = 1 if 9 <= int(
                        current_time_dict['MILITARY_HOUR']) <= 17 else 0
                    dim_time.append(current_time_dict)

        return pd.DataFrame(dim_time)


if __name__ == '__main__':
    dt: DimTime = DimTime()
    df = dt.gen_dim_time()
    print(df.head())
    print(df.tail())
