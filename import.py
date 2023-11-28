import json

# Task 1: Lettura del JSON
def leggi_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def stampa_contenuto(data):
    for avventura in data:
        print(f"Isola: {avventura['isola']}")
        print(f"Evento: {avventura['evento']}")
        print("Sconfitta Avversari:")
        for avversario in avventura.get('sconfitta_avversari', []):
            print(f"  - Nome: {avversario['nome']}, Modo di sconfitta: {avversario['modo_sconfitta']}")
        print()

# Task 2: Ricerca nel JSON
def cerca_evento(data, isola_cercata):
    for avventura in data:
        if avventura['isola'].lower() == isola_cercata.lower():
            return avventura
    return None

# Task 3: Aggiornamento del JSON
def aggiungi_evento(data, nuova_avventura):
    data.append(nuova_avventura)
    with open('zoro_adventures.json', 'w') as file:
        json.dump(data, file, indent=2)

# Esempio di utilizzo
file_path = 'zoro_adventures.json'
avventure_di_zoro = leggi_json(file_path)

# Task 1: Stampare il contenuto
print("Contenuto del JSON:")
stampa_contenuto(avventure_di_zoro)
print()

# Task 2: Ricerca nel JSON
isola_da_cercare = input("Inserisci il nome dell'isola per cercare dettagli sull'evento: ")
risultato_ricerca = cerca_evento(avventure_di_zoro, isola_da_cercare)

if risultato_ricerca:
    print(f"Dettagli sull'evento all'isola {isola_da_cercare}: {risultato_ricerca['evento']}")
    print("Sconfitta Avversari:")
    for avversario in risultato_ricerca.get('sconfitta_avversari', []):
        print(f"  - Nome: {avversario['nome']}, Modo di sconfitta: {avversario['modo_sconfitta']}")
else:
    print(f"Nessun evento trovato all'isola {isola_da_cercare}.")
print()

# Task 3: Aggiornamento del JSON
Domandamodifica = input('Vuoi aggiungere nuove avventure?')
if Domandamodifica.lower() == 'si':
    nuova_avventura = {
        "isola": input("Inserisci il nome dell'isola per la nuova avventura: "),
        "evento": input("Inserisci l'evento per la nuova avventura: "),
        "sconfitta_avversari": []
    }

    while True:
        avversario_nome = input("Inserisci il nome dell'avversario (o 'fine' per terminare): ")
        if avversario_nome.lower() == 'fine':
            break
        avversario_modo_sconfitta = input(f"Inserisci il modo di sconfitta per {avversario_nome}: ")
        nuova_avventura['sconfitta_avversari'].append({"nome": avversario_nome, "modo_sconfitta": avversario_modo_sconfitta})

    aggiungi_evento(avventure_di_zoro, nuova_avventura)
    # Stampa il contenuto aggiornato
    print("Contenuto del JSON dopo l'aggiunta di un nuovo evento:")
    stampa_contenuto(avventure_di_zoro)    
else:
    print('Grazie')
    
