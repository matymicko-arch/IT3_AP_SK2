class robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str):
        self.oznaceni = oznaceni
        self.baterie = baterie
        self.ukol = ukol
        
        pass

    def zvuk(self):
        return("PIPUPIPI")
    
    def diagnostika(self):
        return f"me oznaceni je {self.oznaceni} "