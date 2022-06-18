import pandas as pd
import csv
import glob2
import os.path

# path1 e path2 sono i path delle cartelle da cui andare a prendere i csv di cui fare le medie
path1 = glob2.glob("test_32_sogg/csv_distances/csv_local_distances/Eyes_csv_local_distances/*.csv")
path2 = glob2.glob("test_32_sogg/csv_distances/csv_global_distances/Eyes_csv_global_distances/*.csv")

# filename1 e filename2 sono i nomi dei file che andrò a creare
# e su cui faccio il controllo se esiste già
filename1 = "test_32_sogg/csv_average/Eyes_csv_average/Eyes_average_locali.csv"
filename2 = "test_32_sogg/csv_average/Eyes_csv_average/Eyes_average_globali.csv"

# definisco una funzione per il calcolo delle medie a cui passo
# il path da cui prendere i csv e il nome del file che devo creare
def average(path, filename):
    # controllo se il file csv esiste già
    if os.path.isfile(filename):
        print("FILE ESISTENTE! \nATTENDERE, ELIMINO E RICREO!")
        # cancella il csv vecchio nella destination path
        os.remove(filename)
    else:
        print("FILE INESISTENTE! \nATTENDERE, CREAZIONE DEL FILE!")
    files = path

    # inizializzo un dataframe in cui inserirò le medie
    data_frame = pd.DataFrame()
    column = 0
    listafile = []
    # eseguo un ciclo che ad ogni iterazione apre un file csv su cui calcolo le medie
    for f in files:
        # apro il csv per contare il numero di colonne presenti nel file per settare un
        # range per i calcolo delle medie
        df = pd.read_csv(f)

        # conto il numero di colonne del file csv corrente
        total_cols = len(df.axes[1])
        # print("numcol",total_cols)

        # assegno il numero di colonne del file ad una variabile
        ran = int(total_cols)
        # stampa di controllo

        # print(ran)
        if(ran>8):
            # calcolo l'indice di partenza da cui calcolare la media che è il 20% del numero di colonne
            # startmed = round(ran * 20 / 100, 0)

            # splitto il path del csv per tenere traccia del csv che sto leggendo ed
            # inserirlo come intestazione colonna
            filepath = os.path.split(f)
            listafile.append(filepath[1][:-7] + '_' + filepath[1][-7:-4])

            # prendo le 4 colonne prima dell'elemento centrale
            startmed = round((ran / 2) - 4, 0)
            # print("inidiceinizio",startmed)

            # calcolo l'indice di fine di cui calcolare la media che è il 60% del numero di colonne
            # finmed = round(ran * 60 / 100, 0)

            # prendo le 4 colonne dopo l'elemento centrale
            finmed = round((ran / 2) + 4, 0)
            # print("indicefine",finmed)

            # setto un indice per poter incrementare l'indice colonna di cui fare la media
            j = int(startmed)

            # inizializzo una lista per salvarmi le medie da inserire nel file csv
            listmedia = []

            # eseguo un ciclo a partire dalla 4 colonna prima dell'elemento centrale
            # fino alla 4 colonna dopo l'elemento centrale delle colonne
            # (questo perchè con il 20/60% delle colonne non ho liste della stessa dimensione)
            # per poter passare alla colonna successiva su cui fare la media
            for x in range(int(startmed), int(finmed)):
                # inizializzo una lista in cui mettere gli elementi della colonna
                # che sto prendendo in considerazione
                colselem = []
                # Apro il file
                with open(f) as file_obj:

                    # Create reader object by passing the file
                    reader_obj = csv.reader(file_obj)

                    # setto un indice per poter contare quante righe ci sono nella colonna
                    i = 0
                    # Iterate over each row in the csv file
                    # using reader object
                    for row in reader_obj:
                        # inserisco gli elementi della colonna j-esima nella lista
                        colselem.append(row[j])

                        # incremento l'indice per contare le righe
                        i += 1

                    # effettuo la somma degli elementi presenti nella lista
                    somma = sum(list(map(float, colselem)))
                    # print("la somma è",j, somma)

                    # calcolo la media dei punti della colonna che sto prendendo in considerazione
                    media = somma / i
                    # print("la media", j,"del file",f,"è", media)
                    listmedia.append(media)
                    # incremento l'indice per calcolare la media della colonna successiva
                    j += 1

            # stampa di controllo della lista
            # print(listmedia)

            # inserisco gli elementi della lista in un dataframe che poi inserisco nel csv
            data_frame.insert(loc=column, column=listafile[column], value=listmedia, allow_duplicates=True)
            data_frame.to_csv(filename, sep=",", index=None)

            # incremento l'indice di colonna per poter inserire nell'header il soggetto_emozione
            column += 1

average(path1, filename1)
average(path2, filename2)


