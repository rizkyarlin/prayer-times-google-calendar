package prayer_times_service

type timings struct {
	fajr    string
	dhuhur  string
	asr     string
	maghrib string
	isha    string
}

type gregorian struct {
	date string
}

type date struct {
	gregorian gregorian
}

type aladhanResponse struct {
	timings timings
	date    date
}
