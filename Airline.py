from Flight import *
from Aircraft import *


# definition of the class ailine
class Airline:
    def __init__(self):
        self.name = ""
        self.fleet = []
        self.operations = []
        self.schedule = []


# Prints on the screen the data of the airline, including all the fleet and the operations
def show_airline(a):
    print(f"Airline Name: {a.name}")
    print("Fleet:")
    for ac in a.fleet:
        print(f"\t{ac.Callsign}: ({ac.Type} with {ac.MaxCap} seats)")
    print("Operations:")
    for f in a.operations:
        print(
            f"\t{f.DepAirport} - {f.ArrAirport}, {f.DepTimeM // 60}:{f.DepTimeM % 60} - {f.ArrTimeM // 60}:{f.ArrTimeM % 60}, with {f.Pax} passengers")


# adds the aircraft ac to the fleet of airline a. Returns False if the aircraft (same callsign) is already in the fleet, True in case it can be added correctly.
def add_aircraft(a, ac):
    for aircraft in a.fleet:
        if aircraft == ac:
            return False
    a.fleet.append(ac)
    return True


#  adds the flight f to the operations of airline a. Returns False if the flight is already in the operations list, True in case it can be added correctly. An operation is repeated if the origin, destination and departure time are the same.
def add_operation(a, f):
    for op in a.operations:
        if (op.DepAirport == f.DepAirport) and (op.ArrAirport == f.ArrAirport) and (op.DepTimeM == f.DepTimeM) and (op.ArrTimeM == f.ArrTimeM) and (op.Pax == f.Pax):
            return False
    a.operations.append(f)
    return True
