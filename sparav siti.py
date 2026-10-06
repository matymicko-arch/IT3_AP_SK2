class SitoveZarizeni:
    def __init__(self, nazev:str, ip_adresa:str, online = False):
        self.nazev = nazev
        self.ip_adresa = ip_adresa
        self.online = online

    def zmen_stav(self):
        self.online = not self.online

        if self.online:
            return f"{self.nazev} je nyni ONLINE"
        else:
            return f"{self.nazev} je nyni OFFLINE"
        
    def diagnostika(self):
        return f"spoustim obecnou diagnostiku zarizeni..."
    

class Router(SitoveZarizeni):
    def __init__(self, nazev: str, pocet_portu:int, ip_adresa:str, online=False,):
        super().__init__(nazev, ip_adresa, online)
        self.pocet_portu = pocet_portu

    def diagnostika(self):
        return super().diagnostika() + "Kontroluji Lan porty"
    
    def restartuj_wifi(self):
        return f"wify routeru {self.nazev} byla restartovana"
    

class Server(SitoveZarizeni):
    def __init__(self, nazev: str, os:str, ip_adresa:str, online=False):
        super().__init__(nazev, ip_adresa, online)
        self.os = os

    def diagnostika(self):
        return super().diagnostika() + " Kontroluji vytizeni cpu a stav disku"
    
router = Router("router1", "192.168.1.1", 4)
server = Server("server1", "192.168.10.2", "Ubuntu")

site = [router,server]

for zarizeni in site:
    print(zarizeni.zmen_stav())
    print(zarizeni.diagnostika())