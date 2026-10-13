#classe che rappresenta un prestito di uno strumento a un allievo
class Prestito:
    def __init__(self, codP, data, id_strumento, cognome_allievo):
        self.codP = codP #codice del prestito (es. P1)
        self.data = data
        self.id_strumento = id_strumento #codice dello strumento prestato
        self.cognome_allievo = cognome_allievo

    #stringa leggibile usata da print()
    def __str__(self):
        return f'{self.data} {self.id_strumento} {self.cognome_allievo}'
    #rappresentazione usata quando l'oggetto è dentro una lista
    def __repr__(self):
        return str(self)