#classe che rappresenta un singolo strumento del deposito
class Strumento:
    def __init__(self, codUnivoco, tipo, marca, anno_acquisto, valore):
        self.codUnivoco = codUnivoco #codice identificativo (es. S1)
        self.tipo = tipo
        self.marca = marca
        self.anno_acquisto = anno_acquisto
        self.valore = valore #valore in euro

    #stringa leggibile usata da print()
    def __str__(self):
        return f'{self.codUnivoco} {self.tipo} {self.marca} {self.anno_acquisto} {self.valore}'

    #rappresentazione usata quando l'oggetto è dentro una lista
    def __repr__(self):
        return str(self)