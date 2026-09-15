class Hero:
    def __init__(self,jmeno:str, lvl:int, lokace:str):
        self.jmeno = jmeno
        self.lvl = lvl
        self.lokace = lokace

        pass

    def pokrik(self):
        return("AAAA")

    def predstav_se(self):
        return f"jmenuji se {self.jmeno} a muj lvl je {self.lvl}"

    def kde_jsi(self):
        return f"jsem v {self.lokace}"

    def presun_se(self, nove_misto:str):
        self.misto = nove_misto
        return f"letim do {nove_misto}"

hero = Hero("klaun",36,"Rokycany")

print(hero.jmeno)
print(hero.lvl)
print(hero.lokace)

print(hero.pokrik())
print(hero.predstav_se())
print(hero.kde_jsi())
print(hero.presun_se("Třebíč"))