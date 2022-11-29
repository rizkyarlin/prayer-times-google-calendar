import abc


class PrayerTimeInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "get_city_prayer_times_for_specific_month")
            and callable(subclass.get_city_prayer_times_for_specific_month)
            and hasattr(subclass, "get_service_name")
            and callable(subclass.get_service_name)
        )

    @abc.abstractmethod
    def get_city_prayer_times_for_specific_month(
        self, city: str, country: str, month: int, year: int
    ):
        """Load in the data set"""
        raise NotImplementedError
