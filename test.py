'''
Esercizio 1: Fondamenta di Python (Tema: Roronoa Zoro - One Piece)
Task 1: Variabili e Stringhe
Crea una variabile spadaccino e assegnale il nome "Roronoa Zoro".
Stampa un messaggio che descrive Zoro, includendo il suo sogno di diventare il più grande spadaccino del mondo.
'''
spadaccino = 'Ronoroa Zoro'

print(f"{spadaccino} è un abile spadaccino e membro fondamentale dell'equipaggio dei Cappelli di Paglia. Con una determinazione inossidabile e una maestria impressionante nella spada, {spadaccino} si distingue per la sua forza inarrestabile in battaglia. La sua lealtà al capitano Monkey D. Luffy è evidente in ogni azione, e la sua presenza aggiunge un elemento di potenza e risolutezza al gruppo. Con il sogno di diventare il più grande spadaccino del mondo, {spadaccino} continua a sfidare i suoi limiti, dimostrando che la sua strada verso l'eccellenza è intrisa di coraggio e impegno.")






'''
Task 2: Liste e Cicli
Crea una lista delle spade famose usate da Zoro (es. Wado Ichimonji, Sandai Kitetsu, Shusui).
Utilizza un ciclo for per stampare ogni spada con una breve descrizione o storia.
'''

spade_di_Zoro = [
    {"nome": "Wado Ichimonji", "descrizione": "Spada di grande valore, originariamente di Kuina."},
    {"nome": "Sandai Kitetsu", "descrizione": "Spada maledetta di grado inferiore."},
    {"nome": "Shusui", "descrizione": "Spada leggendaria con grande forza e resistenza."}
]

for i in spade_di_Zoro:
    print(f"{spadaccino} possiede {i['nome']} che è una spada {i['descrizione']} ")






'''Task 3: Condizioni
Scrivi un piccolo gioco di scelta. Chiedi all'utente di scegliere tra due tecniche di spada di Zoro (es. Oni Giri, Tatsumaki) e stampa un risultato diverso a seconda della scelta.
'''
scelta = input(f"Se tu fossi il grande {spadaccino} e stessi affrontando Mihawk chi vorresti avere come compagno in battaglia?")
if scelta == 'nessuno': {
    print(f"Sei un grande, il mitico {spadaccino} non vorrebbe essere MAI aiutato nella sua battaglia finale")
}
else:
    print(f"Ripensaci")




#Task 4: Dizionari
#Crea un dizionario che mappa i nomi dei nemici affrontati da Zoro ai rispettivi combattimenti.
#Stampa dettagli su un combattimento specifico quando l'utente inserisce il nome di un nemico.
combattimenti_di_Zoro = {
    "Mihawk": "Zoro affronta il leggendario Dracule Mihawk in una battaglia epica.",
    "Kuma": "Zoro sacrifica la sua vita per proteggere i suoi compagni durante lo scontro con Bartholomew Kuma.",
    "Daz Bones": "Zoro combatte contro Daz Bones, noto come Mr. 1, durante l'Arc di Alabasta.",
    "Ohm": "Zoro affronta Ohm sull'isola di Skypiea durante l'Arc di Skypiea.",
    "Ryuma": "Zoro combatte contro Ryuma, uno zombi samurai, nell'Arc di Thriller Bark.",
    "Hody Jones": "Zoro affronta Hody Jones sott'acqua durante l'Arc dell'Isola degli Uomini-Pesce.",
    "Pica": "Zoro combatte contro Pica, un ufficiale di alto rango di Donquixote Doflamingo, durante l'Arc di Dressrosa.",
    "Monet": "Zoro si scontra con Monet, una combattente di Punk Hazard servitore di Caesar Clown.",
    "Kaku": "Zoro affronta Kaku, uno degli agenti CP9, durante l'Arc di Enies Lobby.",
    "Basil Hawkins": "Zoro combatte contro Basil Hawkins, uno dei pirati di Kaido, sull'isola di Wano.",
    "Kaido": "Zoro partecipa alla battaglia contro Kaido, il capitano dei Pirati delle Cento Bestie, sull'isola di Wano."
}


nemico_scelto = input("Inserisci il nome di un nemico affrontato da Zoro: ")


if nemico_scelto in combattimenti_di_Zoro:
    print(combattimenti_di_Zoro[nemico_scelto])
else:
    print(f"{spadaccino} non ha affrontato questo nemico. P.S. i nomi vanno con la maiuscola")




#Task 5: Funzioni
#Scrivi una funzione che accetta il nome di un'isola visitata dall'equipaggio e restituisce un evento significativo che coinvolge Zoro in quella località.
#Testa la funzione con un'isola a scelta.

def evento_isola(isola):
    eventi_isola = {
        "Whiskey Peak": f"{spadaccino} sconfigge i membri della Baroque Works sull'isola di Whiskey Peak.",
        "Little Garden": f"{spadaccino} affronta dinosauri giganti e giganti su Little Garden.",
        "Drum Island": f"{spadaccino} combatte contro il malvagio Wapol sull'isola di Drum.",
        "Alabasta": f"{spadaccino} partecipa alla battaglia contro Baroque Works sull'isola di Alabasta.",
        "Jaya": f"{spadaccino} scopre informazioni cruciali sull'isola volante di Skypiea a Jaya.",
        "Skypiea": f"{spadaccino} affronta pericoli celesti e divinità su Skypiea.",
        "Water 7": f"{spadaccino} lotta contro il CP9 e contribuisce a salvare Nico Robin a Water 7.",
        "Enies Lobby": f"{spadaccino} combatte contro il CP9 per salvare Nico Robin durante l'Arc di Enies Lobby.",
        "Thriller Bark": f"{spadaccino} affronta creature spettrali e il samurai zombi Ryuma sull'isola di Thriller Bark.",
        "Sabaody Archipelago": f"{spadaccino} si scontra con Bartholomew Kuma a Sabaody Archipelago.",
        "Punk Hazard": f"{spadaccino} partecipa alla battaglia contro i subordinati di Caesar Clown su Punk Hazard.",
        "Dressrosa": f"{spadaccino} combatte contro Pica durante l'Arc di Dressrosa.",
        "Zou": f"{spadaccino} raggiunge l'isola vivente di Zou e si prepara per l'Arc di Wano."
    }
    return eventi_isola.get(isola, f"{spadaccino} non ha avuto un evento significativo su questa isola.")

isola_scelta = input("Inserisci il nome di un'isola visitata dall'equipaggio: ")
print(evento_isola(isola_scelta))

