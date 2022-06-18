from scipy import spatial
import pandas as pd
import glob2
import numpy as np
import os.path

# src_csv1 e src_csv2 sono i path delle cartelle da cui andare a prendere i csv di cui fare le medie
path = glob2.glob("test_32_sogg/csv_average/*.csv")
src_csv1 = "test_32_sogg/csv_average/EyeB_csv_average/EyeB_average_locali.csv"
src_csv2 = "test_32_sogg/csv_average/EyeB_csv_average/EyeB_average_locali.csv"

# filename1 e filename2 sono i nomi dei file che andrò a creare
# e su cui faccio il controllo se esiste già
filename1 = "test_32_sogg/cosine_similarities/EyeB_cosine_similarities/EyeB_similarity_emo_LocalAverage.csv"
filename2 = "test_32_sogg/cosine_similarities/EyeB_cosine_similarities/EyeB_similarity_emo_GlobalAverage.csv"

def cosineSimilarity(src_csv,filename):

    # controllo se il file csv esiste già
    if os.path.isfile(filename):
        print("FILE ESISTENTE! \nATTENDERE, ELIMINO E RICREO!")
        # cancella il csv vecchio nella destination path
        os.remove(filename)
    else:
        print("FILE INESISTENTE! \nATTENDERE, CREAZIONE DEL FILE!")

    # lista dei risultati similarità per soggetto
    emotions_sim = []

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

    # inizializzo lista di dimensione fixata
    expression_ordered = [None] * 7
    # scorro la lista di dizionari con i soggetti in ordine
    for i, subject in enumerate(col_names_ordered):
        for expression in subject:
            # inizializzo dizionario buffer
            values = {}
            # calcolo indice da usare per accedere alla lista di dimensione fixata
            position = int(expression.split("_")[1]) - 1
            # accedo alla lista con try/except
            try:
                # se nell'indice calcolato c'è già un dizionario
                if len(expression_ordered[position].keys()) > 0:
                    # faccio una shallow copy del dizionario
                    values = expression_ordered[position].copy()
                    # aggiungo un nuovo record al dizionario
                    values[expression] = subject.get(expression)
                    # sostituisco il dizionario all'indice della lista con quello nuovo
                    expression_ordered[position] = values
            except:
                # genero un record per il dizionario
                values[expression] = subject.get(expression)
                # aggiungo il dizionario nella lista all'indice calcolato
                expression_ordered[position] = values


    # calcolo il numero massimo di dati in una colonna
    max_records = 0
    for subject in expression_ordered:
        if len(subject.keys()) > max_records:
            max_records = len(subject.keys())
    # print("NUMERO DI COLONNE MAGGIORE: ", max_records)

    # calcolo delle similarità per ogni espressione
    for i, expression in enumerate(expression_ordered):
        if len(expression.keys()) == 1:
            # print("UNA SOLA ESPRESSIONE: ", expression)
            emotions_sim.append([1.0])
        else:
            for subject in expression:
                similarity_column = []
                # print("ATTENDERE STO GENERANDO I CSV DI :", subject)
                for subject_compare in expression:
                    similarity_column.append(
                        1 - spatial.distance.cosine(
                            expression[subject], expression[subject_compare]))
                    # print("CALCOLATO DISTANZA TRA: ", expression, "E ", expression_compare)
                    # fine for di comparazione

                # riempio la lista complessiva dei risultati con i risultati della colonna corrente
                emotions_sim.append(similarity_column)

    # al termine del calcolo dei risultati delle similarità, la lista avrà sottoliste di dimensioni diverse
    # per normalizzare aggiungo il valore 0.0 per tutte le sottoliste con meno elementi del numero massimo di records
    for result_list in emotions_sim:
        if len(result_list) < max_records:
            for i in range(len(result_list), max_records):
                result_list.append(0.0)

    # creo lista per nomi delle colonne da inserire nell'header del csv da generare
    csv_col_names = []
    for dict in expression_ordered:
        for expression in dict:
            csv_col_names.append(expression)

    # itero per tot volte quanto il numero di colonne da generare
    for i in range(0, len(csv_col_names)):
        df_similarities.insert(loc=i, column=csv_col_names[i], value=emotions_sim[i], allow_duplicates=True)

    # generazione del csv
    df_similarities.to_csv(filename, sep=",", index=None)
    # print(expression_ordered)


cosineSimilarity(src_csv1,filename1)
cosineSimilarity(src_csv2,filename2)
