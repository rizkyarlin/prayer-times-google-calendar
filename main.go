package main

import (
	"fmt"
	"prayer-times-google-calendar/prayer_times_service"
)

func main() {
	//var err error
	//calendar_service.Run()
	prayerTimes, _ := prayer_times_service.GetCityPrayerTimesForSpecificMonth("Makassar", "Indonesia", 12, 2022)
	fmt.Printf("%+v\n", prayerTimes)
}
