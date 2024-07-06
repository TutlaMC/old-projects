class Electron:
    def __init__(self,energy):
        self.energy = 0

class Proton:
    def __init__(self,energy):
        self.energy = 0

class Atom: 
    def __init__(self,protons,electrons): 
        self.count = len(protons)+len(electrons)
        self.protons = protons
        self.electrons = electrons
        
    