import csv #per leggere il file csv
from strumento import Strumento
from prestito import Prestito

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile


        self.lista_strumenti = []  #lista di tutti gli oggetti
        self.lista_prestiti = [] #lista dei prestiti in corso
        self.contatore_prestiti = 0 #serve a generare codici prestito univoci

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as infile: #apro il file in lettura
                reader = csv.reader(infile, delimiter=',') #ogni riga diventa una lista di valori
                for row in reader:  #per ogni riga del file
                    try: #estraggo i singoli valori delle colonne
                        codUnivoco = row[0]
                        tipo = row[1]
                        marca = row[2]
                        anno_acquisto = int(row[3]) #converto in intero
                        valore = float(row[4]) #converto in decimale

                        strumento = Strumento(codUnivoco, tipo, marca, anno_acquisto, valore) #creo l'oggetto strumento con i dati della riga

                        self.lista_strumenti.append(strumento) #aggiungo l'oggetto strumento alla lista

                    except IndexError: #riga con meno colonne del previsto
                        print("Attenzione: errore sugli indici, riga incompleta.")
                    except ValueError: #anno o valore non numerici
                        print("Attenzione: valori non validi.")

        except FileNotFoundError:
            print(f'Errore: file {file_path} non trovato.') #errore di file inesistente
        except Exception:
            print(f'Errore imprevisto.') #altro errore imprevisto

        return self.lista_strumenti #restituisce lista aggiornata anche se vuota




    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        codUnivoco = f'S{len(self.lista_strumenti)+1}' #genero il codice in base al numero di strumenti
        self.lista_strumenti.append(Strumento(codUnivoco, tipo, marca, anno_acquisto, valore)) #creo e aggiungo il nuovo strumento
        return self.lista_strumenti

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        for strumento in self.lista_strumenti:   # in una sola riga, al posto di usare il ciclo: return sorted(self.lista_strumenti, key=lambda strumento: strumento.marca)
            sorted(self.lista_strumenti,key=strumento.marca) #ordino usando la marca come chiave
        return self.lista_strumenti

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        for strumento in self.lista_strumenti: #cerco lo strumento nel deposito
            if id_strumento == strumento.codUnivoco:
                for prestito in self.lista_prestiti: #controllo che non sia già prestato
                    if id_strumento == prestito.id_strumento:
                        raise Exception("Lo strumento è già imprestato.") #facendo raise Exception() non serve inserire try all'inizio
                self.contatore_prestiti+=1 #incremento per avere un nuovo codice
                prestito = Prestito(f'P{self.contatore_prestiti}', data, id_strumento, cognome_allievo) #creo il prestito
                self.lista_prestiti.append(prestito) #lo registro tra i prestiti in corso
                return prestito
        raise Exception("Lo strumento non è presente nel deposito.") #nessuno strumento trovato con quel codice





    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for prestito in self.lista_prestiti: #cerco il prestito tramite il codice
            if id_prestito == prestito.codP:
                self.lista_prestiti.remove(prestito) #rimuovendolo lo strumento torna disponibile
                return self.lista_prestiti
        raise Exception("Il prestito non esiste.") #nessun prestito trovato con quel codice
