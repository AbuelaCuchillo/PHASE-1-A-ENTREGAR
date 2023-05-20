class Aircraft:
    def __init__(self):
        self.Callsign = ""
        self.Type = ""
        self.MaxCap = ""
def ShowAircraft(a):
    print(a.Callsign,a.Type,a.MaxCap)