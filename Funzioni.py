
def MostraPoz(df):
    print('\t\tLISTA POZIONI')
    df.sort_values(by=['punteggio'],ascending = False,inplace=False)
    print(df)


def MostraIng(df):
    print('\t\tLISTA INGREDIENTI')
    print(df)


def EliminaPoz(df):
    el = input("inserisci il nome della pozione da eliminare: ")
    for x in df.index:
        if df.loc[x, 'nome'] == el:
            df.drop(x, inplace = True)
    print(df)


def ModificaPoz(df):
    ind = int(input("inserisci il numero della pozione che vuoi modificare"))
    cella = input('inserisci cosa modificare: ')
    mod = input(f"inserisci il {cella}")
    df.loc[ind, cella] = mod
    print(df)


def DettagliPoz(df, dfpoz):
    ind = int(input("inserisci il numero della pozione che vuoi visualizzare: "))
    d = (dfpoz.loc[ind,'ingredienti']).split(',')
    print(f"    POZIONE ->{dfpoz.loc[ind,'nome']}")
    for i in d:
        for x in df.index:
            if df.loc[x, 'ingredienti'] == i:
                print(f'''Ingrediente: {df.loc[x,'ingredienti']}
 * punti acqua: {df.loc[x,'punteggio acqua']}
 * punti fuoco: {df.loc[x,'punteggio fuoco']}
 * punti terra: {df.loc[x,'punteggio terra']}
 * punti aria:  {df.loc[x,'punteggio aria']}''')

def NewPozione(df,dfI):
    name = input('Inserisci il nome della pozione: ')
    ing = []
    ingr = ""
    MostraIng
    nuovaRiga = {'nome':name, 'punteggio':87, 'ingredienti':'ciaidisadas'}
    df = df.append(nuovaRiga, ignore_index=True, verify_integrity=False)
    return df

