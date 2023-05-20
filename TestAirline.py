import Aircraft
import Flight
import Airline
def createXicaAirline ():
    '''Function createXicaAirline
    ==============================
    This function has no input parameters
    Returns an airline with 2 aircraft and 4 flights
    '''
    '''creates first aircraft with some values'''
    AC1 = Aircraft.Aircraft()
    AC1.callsign = "EC234"
    AC1.type = "A320"
    AC1.seats = 280
    # creates a second aircraft with other values
    AC2 = Aircraft.Aircraft()
    AC2.callsign = "EC504"
    AC2.type = "A321"
    AC2.seats = 310
    # creates first flight with some values
    FL1 = Flight.Flight()
    FL1.dep = "Barcelona"
    FL1.arr = "Budapest"
    FL1.time_dep = 860
    FL1.time_arr = 1160
    FL1.passengers = 54
    # creates second flight with some values
    FL2 = Flight.Flight()
    FL2.dep = "Barcelona"
    FL2.arr = "Istambul"
    FL2.time_dep = 960
    FL2.time_arr = 12.560
    FL2.passengers = 154
    # creates third flight with some values
    FL3 = Flight.Flight()
    FL3.dep = "Istambul"
    FL3.arr = "Budapest"
    FL3.time_dep = 1760
    FL3.time_arr = 19.2560
    FL3.passengers = 140
    # creates fourth flight with some values
    FL4 = Flight.Flight()
    FL4.dep = "Budapest"
    FL4.arr = "Barcelona"
    FL4.time_dep = 2060
    FL4.time_arr = 2360
    FL4.passengers = 97
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

