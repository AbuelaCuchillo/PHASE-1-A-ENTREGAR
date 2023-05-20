import Aircraft
import Airline
import Flight

def createXicaAirline ():
    """ Function createXicaAirline
    ==============================
    This function has no input parameters
    Returns an airline with 2 aircraft and 4 flights
    """
    # creates first aircraft with some values
    AC1 = Aircraft.Aircraft()
    AC1.Callsign = "EC234"
    AC1.Type = "A320"
    AC1.MaxCap = 280
    # creates a second aircraft with other values
    AC2 = Aircraft.Aircraft()
    AC2.Callsign = "EC504"
    AC2.Type = "A321"
    AC2.MaxCap = 310
    # creates first flight with some values
    FL1 = Flight.Flight()
    FL1.DepAirport = "Barcelona"
    FL1.ArrAirport = "Budapest"
    FL1.DepTimeM = 8*60
    FL1.ArrTimeM = 11*60
    FL1.Pax = 54
    # creates second flight with some values
    FL2 = Flight.Flight()
    FL2.DepAirport = "Barcelona"
    FL2.ArrAirport = "Istambul"
    FL2.DepTimeM = 9*60
    FL2.ArrTimeM = 12.5*60
    FL2.Pax = 154
    # creates third flight with some values
    FL3 = Flight.Flight()
    FL3.DepAirport = "Istambul"
    FL3.ArrAirport = "Budapest"
    FL3.DepTimeM= 17*60
    FL3.ArrTimeM = 19.25*60
    FL3.Pax = 140
    # creates fourth flight with some values
    FL4 = Flight.Flight()
    FL4.DepAirport = "Budapest"
    FL4.ArrAirport = "Barcelona"
    FL4.DepTimeM = 20*60
    FL4.ArrTimeM = 23*60
    FL4.Pax = 97
    # creates the airline
    Xica = Airline.Airline()
    Xica.name = "Xica Airline"
    Airline.add_aircraft(Xica, AC1)
    Airline.add_aircraft(Xica, AC2)
    Airline.add_operation(Xica, FL1)
    Airline.add_operation(Xica, FL2)
    Airline.add_operation(Xica, FL3)
    Airline.add_operation(Xica, FL4)
    return Xica
# main
print ("Phase1 test program")
A = createXicaAirline()
Airline.show_airline(A)
print ("Phase1 test program end")