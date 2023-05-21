import matplotlib.pyplot as plt


class Assignment:
    def __init__(self):
        self.aircraft = None
        self.flights = []

    def show_assignments(self, assign):
        print(f"Aircraft:{assign.aircraft}")
        for f in assign.flights:
            print(f)

    def assign_aircraft(self, ac):
        if not self.aircraft and not self.flights:
            self.aircraft = ac
            return True
        else:
            return False

    def assign_flight(self, assign, f):
        if not assign.aircraft or not assign.flights:
            return False
        if assign.aircraft.type != f.type:
            return False
        last_flight = assign.flights[-1]
        if f.tdep < last_flight.tarr:
            return False
        if last_flight.arr != f.dep:
            return False
        assign.flights.append(f)
        return True

    def plot_assignment(self, assign):
        if not assign.aircraft or not assign.flights:
            return False
        else:
            durations = []
            for f in assign.flights:
                durations.append((f.tdep, f.tarr - f.tdep))
            y = [assign.aircraft.type]
            x = durations
            x_range = ('00:00', '23:59')
            plt.plot(x, y)
            plt.xlabel("Flight Time")
            plt.ylabel("Aircraft Type")
            plt.xlim(x_range)
            plt.show()

    def plot_assignments(self, vector_assig):
        # Iterate over each assignment in the vector
        for assign in vector_assig:
            if not assign.aircraft or not assign.flights:
                continue

            # Get the flight durations and aircraft type
            durations = []
            aircrafts = []
            for f in assign.flights:
                durations.append((f.tdep, f.tarr))
                aircraft_type = assign.aircraft.type
                aircrafts.append(aircraft_type)
            x = durations
            x_range = ('00:00', '23:59')
            y = aircrafts
            y_range = (min(y), max(y))

            # Set up the plot
            plt.plot(x, y)
            plt.xlim(x_range)
            plt.ylim(y_range)
            plt.xlabel("Flight Time")
            plt.ylabel("Aircraft Type")
            plt.show()