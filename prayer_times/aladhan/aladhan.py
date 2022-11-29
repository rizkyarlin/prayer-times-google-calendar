from urllib.request import Request, urlopen
from prayer_times.interface import PrayerTimeInterface
import json


class AladhanPrayerTimeService(PrayerTimeInterface):
    """
    docs https://aladhan.com/prayer-times-api
    example: http://api.aladhan.com/v1/calendarByCity?city=London&country=United Kingdom&method=2&month=04&year=2017
    """

    BASE_URL = "http://api.aladhan.com/v1"
    CALCULATION_METHOD = 3  # Muslim World League

    def get_city_prayer_times_for_specific_month(
            self, city: str, country: str, month: int, year: int
    ):
        req = Request(
            url=f"{self.BASE_URL}/calendarByCity?city={city}&country={country}&method={self.CALCULATION_METHOD}&month={month}&year={year}"
        )
        res = urlopen(req)
        data = res.read().decode("utf-8")
        # TODO implement response dataclass
        data = json.loads(data)
        return data['data']
