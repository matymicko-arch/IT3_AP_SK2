class Vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int,stav_nadrze=100):
        self.znacka = znacka
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze

    def zvuk_motoru(self):
        return f"???"
    
    def info(self):
        return f"vozidlo {self.znacka}, rok {self.rok_vyroby}"
    
    def startuj(self):
        if self.stav_nadrze > 0:
            return f"vozidlo nastartovalo {self.zvuk_motoru()}"
        else:
            return f"vozidlo nenastartovalo neni béňo"
        



class Autiko(Vozidlo):
    def __init__(self, znacka: str, rok_vyroby: int, typ_prevodovky:str, stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_prevodovky

    def zvuk_motoru(self):
        return f"Vrum Vrum!"
    
    def zatrub(self):
        return f"TUUUUUUUUU"
    
class Moped(Vozidlo):
    def __init__(self, znacka: str, rok_vyroby: int, ma_slapadla:str, stav_nadrze = 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.ma_slapadla = ma_slapadla


    def zvuk_motoru(self):
        return f"TUTUTUTUTUTUT"
    
    def slapej(self):
        return f"Šlapeeeej!!!!"
    

garaz = []

Auto = Vozidlo("volkswagen beatle", 1985, 100)
babeta = Moped("jawa", 2012, True)

garaz.append(Auto)
garaz.append(babeta)

for vozidla in garaz:
    print(vozidla.info())
    print(vozidla.startuj())


