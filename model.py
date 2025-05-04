import json
from datetime import date
from utils import curs_valutar

class Tranzactie:
    def __init__(self, tip, suma, moneda, categorie, descriere, data=None):
        self.tip = tip
        self.suma = float(suma)
        self.moneda = moneda.upper()
        self.categorie = categorie
        self.descriere = descriere
        self.data = data if data else str(date.today())
        self.suma_lei = self.converteste_in_lei()  # Calculează suma în lei

    def converteste_in_lei(self):
     curs = curs_valutar(self.moneda)
     if curs is None:
        print(f"Moneda necunoscută: {self.moneda}. Folosesc suma originală.")
        return round(self.suma, 2)
     return round(self.suma * curs, 2)

    def to_dict(self):
        return {
            "tip": self.tip,
            "suma": self.suma,
            "moneda": self.moneda,
            "categorie": self.categorie,
            "descriere": self.descriere,
            "data": self.data,
        }

class ManagerBuget:
    def __init__(self, fisier="buget_gui.json"):
        self.fisier = fisier
        self.tranzactii = self._incarca()

    def _incarca(self):
        try:
            with open(self.fisier, "r") as f:
                date = json.load(f)
                for tranzactie in date:
                    if 'moneda' not in tranzactie:
                        tranzactie['moneda'] = 'RON'
                    if 'suma_lei' in tranzactie:
                        del tranzactie['suma_lei']
                return [Tranzactie(**t) for t in date]
        except FileNotFoundError:
            return []

    def salveaza(self):
        with open(self.fisier, "w") as f:
            json.dump([t.to_dict() for t in self.tranzactii], f, indent=2)

    def adauga(self, tranzactie):
        self.tranzactii.append(tranzactie)
        self.salveaza()

    def sterge(self, index):
        if 0 <= index < len(self.tranzactii):
            self.tranzactii.pop(index)
            self.salveaza()

    def buget_total(self):
        total = 0
        for t in self.tranzactii:
            if t.tip == "venit":
                total += t.suma_lei
            else:
                total -= t.suma_lei
        return total

    def __iter__(self):
        return iter(self.tranzactii)