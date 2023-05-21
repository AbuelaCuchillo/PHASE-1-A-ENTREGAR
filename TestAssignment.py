import Assignment

# Create an instance of the Assignment class
A = Assignment.Assignment()

# Assign an aircraft
aircraft = "A320"
A.assign_aircraft(aircraft)

# Assign flights
flight1 = (aircraft, "10:00", "12:00", "Flight 1")
flight2 = (aircraft, "13:00", "15:00", "Flight 2")
A.assign_flight(flight1)
A.assign_flight(flight2)

# Display the assignments
A.show_assignments()

# Plot the assignments
A.plot_assignment()