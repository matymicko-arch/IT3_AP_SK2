class Robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        
        pass

    def zvuk(self):
        return("PIPUPIPI")
    
    def diagnostika(self):
        return f"me oznaceni je {self.oznaceni} a moje baterie je {self.baterie}%"
    
    def aktualni_ukol(self):
        return f"Muj ukol v tento moment je {self.ukol}"
    
    def Novy_ukol(self, novy_ukol:str):
        self.ukol = novy_ukol
        return f"zmenil se mi ukol, ted musim {novy_ukol}"
    
robot = Robot("clanker", 67, "umejt hajzly")

print(robot.oznaceni)
print(robot.baterie)
print(robot.ukol)

print(robot.zvuk())
print(robot.diagnostika())
print(robot.aktualni_ukol())
print(robot.Novy_ukol("podelavat kone"))