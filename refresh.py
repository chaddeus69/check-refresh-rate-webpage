import requests
import time

def misura_tempo_refresh(url):
    while True:
        try:
            # Effettua la richiesta
            inizio = time.time()
            response = requests.get(url)
            fine = time.time()

            if response.status_code == 200:
                tempo_richiesta = fine - inizio
                print(f"Tempo della richiesta per il sito: {tempo_richiesta} secondi")
            else:
                print(f"La richiesta per il sito ha restituito un codice di stato non valido.")

            # Aspetta prima di fare la prossima richiesta
            time.sleep(1)

        except requests.exceptions.RequestException as e:
            print(f"Errore durante la richiesta: {e}")

try:
    # Chiedi all'utente di inserire l'URL del sito da testare
    url_da_testare = input("Inserisci l'URL del sito da testare: ")
    
    # Esegui il test di misurazione del tempo di refresh
    misura_tempo_refresh(url_da_testare)

except KeyboardInterrupt:
    print("Programma interrotto manualmente.")
