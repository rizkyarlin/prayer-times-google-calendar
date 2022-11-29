from prayer_times.aladhan.aladhan import AladhanPrayerTimeService

ser = AladhanPrayerTimeService()
data = ser.get_city_prayer_times_for_specific_month('Makassar', 'Indonesia', 11, 2022)

for day in data:
    # POC for prayer times API is completed
    print(day['date']['readable'])
