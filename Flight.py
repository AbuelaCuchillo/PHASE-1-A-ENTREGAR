from Aircraft import x.MaxCap
class Flight:
    '''define all "selfs" from the Flight class'''
    def __init__(self):
        self.DepAirport = ""
        self.ArrAirport = ""
        self.DepTimeH = ""
        self.DepTimeM = ""
        self.ArrTimeH = ""
        self.ArrTimeM = ""
        self.Pax = ""
        self.TotalTime = ""
        self.d = ""
def show_flight(f):
    '''A print of everything contained in (flight)'''
    print(f.DepAirport,f.ArrAirport,f.DepTimeH,":",f.DepTimeM,f.ArrTimeH,":",f.ArrTimeM,f.Pax)
def flight_duration(f):
    '''To get the total time we substract the departure time from de arrival time'''
    print(f.TotalTime)
def delay_flight(f,d):
    '''We have to add the delay time to the total sum of minutes'''
    if (f.TotalTime + d.d) <= 1440:
        print(f.TotalTime + d.d)
    else:
        print("FALSE")
def fits_flight_in_aircraft(f,a):
    '''If Pax is superior to MaxCap it means that there are more pasengers than seats'''
    if (x.MaxCap - f.Pax) >= 0:
        print("TRUE")
    else:
        print("FALSE")
def fuel(f):
    '''gallons = fuel use * duration of the flight + a safety 15%
    We convert the total minutes in hours and multiply it by the fuel use/h'''
    f.fuel_use = ((f.TotalTime /60)*280) + ((f.TotalTime / 60)*280)*0.15
    print(f.fuel_use,"GALLONS")