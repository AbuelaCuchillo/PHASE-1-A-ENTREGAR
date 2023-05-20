class Aircraft:
    '''Defines all "SELFS" from the Aircraft class'''
    def __init__(self):
        self.Callsign = ""
        self.Type = ""
        self.MaxCap = 0
def ShowAircraft(a):
    '''Shows the Aircraft's information'''
    print(a.Callsign,a.Type,a.MaxCap)