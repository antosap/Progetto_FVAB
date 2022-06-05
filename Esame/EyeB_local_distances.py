import glob2
import numpy as np
import pandas as pd
import os

# path dei csv
path_src = "csv_landmark/EyeB_csv_landmark/"
path_dest = "csv_distances/csv_local_distances/EyeB_csv_local_distances/"

# cancella i vecchi csv prodotti nella destination path
for f in os.listdir(path_dest):
    os.remove(path_dest + f)

# funzione per calcolare la distanza tra i csv tramite la funzione euclidea
def euclidean_dist(df1, df2):
    return np.linalg.norm(df1.values - df2.values, axis=1)

def dist_locali(path):
    data_frame = pd.DataFrame()
    column = 0
    # scorro i csv
    for i, file in enumerate(path):
        curr_rdx = ""
        next_rdx = ""
        # controllo che il next file sia presente nella lista
        if i + 1 < len(path):
            # controllo le radici dei nomi file
            for c in file[::-1]:
                if c == "\\":
                    break
                curr_rdx += c

            for c in path[i + 1][::-1]:
                if c == "\\":
                    break
                next_rdx += c

            curr_rdx = curr_rdx[::-1].split("_")[0] + curr_rdx[::-1].split("_")[1]
            next_rdx = next_rdx[::-1].split("_")[0] + next_rdx[::-1].split("_")[1]

            if curr_rdx.find(next_rdx) != -1:
                # leggo il primo csv dei landmark
                a = pd.read_csv(file)

                # leggo di nuovo i csv
                b = pd.read_csv(path[i + 1])

                # assegno una var sulla chiamata della funzione per il calolo della distanza per poter creare il df
                distglocale = (euclidean_dist(a, b))
                # print(distglocale)

                # dataframe per ogni soggetto
                data_frame.insert(loc=column, column=column, value=distglocale, allow_duplicates=True)
                data_frame.to_csv(path_dest + curr_rdx + ".csv", sep=",", index=None)
                column += 1
            else:
                data_frame = pd.DataFrame()
                column = 0


# lista files csv da scansionare nella source path
files = glob2.glob(path_src + "*.csv")
print("\nATTENDERE! STO GENERANDO I CSV DELLE DISTANZE LOCALI")

dist_locali(files)
# import sys
# sys.stdout.flush()
print("\nCSV DISTANZE LOCALI GENERATI")