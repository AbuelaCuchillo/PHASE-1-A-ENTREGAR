class Airline:
    def init(self):
        self.name = ""
        self.fleet = []
        self.operations = []
        self.schedule = []

def show_airline(a):
    """Prints on the screen the data of the airline"""
    print("Airline name: ", a.name)
    print("Fleet: ", a.fleet)
    print("Flights: ", a.operations)

def add_aircraft (a, ac):
    """Input: airline (a), aircraft (ac). Output: True/False
    Adds the aircraft to the fleet. Return true if is added correctly, False if not."""
    for i in a.fleet:
        if i == ac:
            a.fleet.append(ac)
            return True
        return False

def add_operation (a, f):
    """Input: airline (a), flight (f). Output: True/False.
    Adds a flight to the operations list. Return true if is added correctly, false if not.
    """
    for i in a.operations:
        if i.departureairport == f.departureairport and i.arrivalairport == f.arrivalairport and i.departuretime == f.departuretime:
            return False
        else:
            a.operations.append(f)
            return True