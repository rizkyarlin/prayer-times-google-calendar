package prayer_times_service

import (
	"encoding/json"
	"net/http"
	"strconv"
)

var baseURL = "http://api.aladhan.com/v1"
var calculationMethod = 2

func GetCityPrayerTimesForSpecificMonth(city string, country string, month int, year int) ([]aladhanResponse, error) {
	var err error
	var client = &http.Client{}
	var data []aladhanResponse

	request, err := http.NewRequest("GET", baseURL+"/calendarByCity?city="+
		city+"&country="+country+"&method="+strconv.Itoa(calculationMethod)+
		"&month="+strconv.Itoa(month)+"&year="+strconv.Itoa(year), nil)
	if err != nil {
		return nil, err
	}

	response, err := client.Do(request)
	if err != nil {
		return nil, err
	}
	defer response.Body.Close()

	err = json.NewDecoder(response.Body).Decode(&data)
	if err != nil {
		return nil, err
	}

	return data, nil
}
