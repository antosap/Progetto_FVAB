from scipy import spatial
import pandas as pd
import glob2
import numpy as np
import os.path

# src_csv1 e src_csv2 sono i path delle cartelle da cui andare a prendere i csv di cui fare le medie
path = glob2.glob("csv_average/*.csv")
src_csv1 = "csv_average/Lips_csv_average/Lips_average_locali.csv"
src_csv2 = "csv_average/Lips_csv_average/Lips_average_locali.csv"
filename1="cosine_similarities/Lips_cosine_similarities/Lips_similarity_Sogg_LocalAverage.csv"
filename2="cosine_similarities/Lips_cosine_similarities/Lips_similarity_Sogg_GlobalAverage.csv"

def cosineSimilarity(src_csv,filename):
    # filename1 e filename2 sono i nomi dei file che andrò a creare
    # e su cui faccio il controllo se esiste già

    # controllo se il file csv esiste già
    if os.path.isfile(filename):
        print("FILE ESISTENTE, ELIMINO E RICREO ")
        # se esiste cancella il csv vecchio nella destination path
        os.remove(filename)
    else:
        print("FILE INESISTENTE")

    # lista dei risultati similarità per soggetto
    subjects_sim = []

    # dataframe similarità da riempire
    df_similarities = pd.DataFrame()

    # apro il csv
    df = pd.read_csv(src_csv)

    # nomi delle colonne (S010_001)
    col_names = list(df.columns)

    # lista di dizionari con nome soggetto ed espressione + valori
    col_names_ordered = []

    # raggruppamento dei dati per ogni soggetto con espressione
    buf = {}
    data_list = np.array(df.values.tolist())
    # siccome prendo i valori per riga, faccio la trasposta per ottenere i valori sotto al soggetto
    data_list = data_list.transpose()

    # costruzione del dizionario
    for i, name in enumerate(col_names):
        # creo dizionario con chiave il nome del soggetto+emozione e valore i dati
        buf[name] = data_list[i]
        # controllo overflow sul numero di elementi che scorro
        if i+1 < len(col_names):
            # controllo se il nome del soggetto corrente è diverso dal successivo
            if name.split("_")[0] != col_names[i + 1].split("_")[0]:
                # in tal caso aggiungo il dizionario alla lista di dizionari e resetto il dizionario buffer
                col_names_ordered.append(buf)
                buf = {}
        else:
            # aggiungo il dizionario alla lista di dizionari
            col_names_ordered.append(buf)

    # calcolo il numero massimo di dati in una colonna
    max_records = 0
    for subject in col_names_ordered:
        if len(subject.keys()) > max_records:
            max_records = len(subject.keys())
    # print("NUMERO DI COLONNE MAGGIORE: ", max_records)

    # calcolo delle similarità per ogni soggetto alternando emozioni
    for i, subject in enumerate(col_names_ordered):
        # print("SONO IL SOGGETTO: ", subject)

        if len(subject.keys()) == 1:
            # print("NON CI SONO ALTRE ESPRESSIONI PER IL SOGGETTO: ", subject)
            subjects_sim.append([1.0])
        else:
            for expression in subject:
                # print("SONO EXPRESSION: ", expression)
                similarity_column = []
                for expression_compare in subject:
                    # print("SONO EXPRESSION PER COMPARARE: ", expression_compare)
                    similarity_column.append(
                        1 - spatial.distance.cosine(
                            subject[expression], subject[expression_compare]))
                    # print("CALCOLATO DISTANZA TRA: ", expression, "E ", expression_compare)
                    # fine for di comparazione
                # print("TERMINATO CALCOLO SU: ", expression)
                # riempio la lista complessiva dei risultati con i risultati della colonna corrente
                subjects_sim.append(similarity_column)

    # al termine del calcolo dei risultati delle similarità, la lista avrà sottoliste di dimensioni diverse
    # per normalizzare aggiungo il valore 1.0 per tutte le sottoliste con meno elementi del numero massimo di records
    for result_list in subjects_sim:
        if len(result_list) < max_records:
            for i in range(len(result_list), max_records):
                result_list.append(0)

    # creo lista per nomi delle colonne da inserire nell'header del csv da generare
    csv_col_names = []
    for subject in col_names_ordered:
        for expression in subject:
            csv_col_names.append(expression)

    # itero per tot volte quanto il numero di colonne da generare
    for i in range(0, len(csv_col_names)):
        df_similarities.insert(loc=i, column=csv_col_names[i], value=subjects_sim[i], allow_duplicates=True)

    # generazione del csv
    df_similarities.to_csv(filename, sep=",", index=None)


print("\nATTENDERE! STO GENERANDO I CSV DELLE SIMILARITA' PER SOGGETTO \nSULLE MEDIE LOCALI E SULLE MEDIE GLOBALI\n")
cosineSimilarity(src_csv1, filename1)
cosineSimilarity(src_csv2, filename2)
print("\nCSV DELLE SIMILARITA' PER SOGGETTO SU DISTANZE LOCALI GENERATO")
print("CSV DELLE SIMILARITA' PER SOGGETTO SU DISTANZE GLOBALI GENERATO")