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