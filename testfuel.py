import Flight
'''Import everything from the Flight to use it's functions'''

y = Flight.Flight()
y.DepTimeH = 2
y.DepTimeM = 30
y.ArrTimeH = 5
y.ArrTimeM = 30
y.TotalTime = (y.ArrTimeH - y.DepTimeH)*60 + (y.ArrTimeM - y.DepTimeM)
Flight.fuel(y)