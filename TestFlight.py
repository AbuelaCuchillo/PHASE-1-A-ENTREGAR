import Flight

y = Flight.Flight()
z = Flight.Flight()
y.DepAirport = "BCN"
y.ArrAirport = "PMI"
y.DepTimeH = 2
y.DepTimeM = 30
y.ArrTimeH = 4
y.ArrTimeM = 30
y.Pax = 150
y.TotalTime = (y.ArrTimeH - y.DepTimeH)*60 + (y.ArrTimeM - y.DepTimeM)
z.d = 400
Flight.show_flight(y)
Flight.flight_duration(y)
Flight.delay_flight(y,z)

