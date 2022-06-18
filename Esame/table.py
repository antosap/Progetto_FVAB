import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

# lista di file da cui estrarre la tabella a video
src_csv1 = "test_32_sogg/cosine_similarities/Lips_cosine_similarities/Lips_similarity_Sogg_LocalAverage.csv"
src_csv2 = "test_32_sogg/cosine_similarities/Lips_cosine_similarities/Lips_similarity_Sogg_GlobalAverage.csv"
src_csv3 = "test_32_sogg/csv_average/Lips_csv_average/Lips_average_locali.csv"
src_csv4 = "test_32_sogg/csv_average/Lips_csv_average/Lips_average_globali.csv"

src_csv5 = "test_32_sogg/cosine_similarities/Eyes_cosine_similarities/Eyes_similarity_Sogg_LocalAverage.csv"
src_csv6 = "test_32_sogg/cosine_similarities/Eyes_cosine_similarities/Eyes_similarity_Sogg_GlobalAverage.csv"
src_csv7 = "test_32_sogg/csv_average/Eyes_csv_average/Eyes_average_locali.csv"
src_csv8 = "test_32_sogg/csv_average/Eyes_csv_average/Eyes_average_globali.csv"

src_csv9 = "test_32_sogg/cosine_similarities/EyeB_cosine_similarities/EyeB_similarity_Sogg_LocalAverage.csv"
src_csv10 = "test_32_sogg/cosine_similarities/EyeB_cosine_similarities/EyeB_similarity_Sogg_GlobalAverage.csv"
src_csv11 = "test_32_sogg/csv_average/EyeB_csv_average/EyeB_average_locali.csv"
src_csv12 = "test_32_sogg/csv_average/EyeB_csv_average/EyeB_average_globali.csv"

def show_table(filepath1):
    # apro il csv
    df = pd.read_csv(filepath1)
    # prendo in input il soggetto di cui mostrare i dati
    print("Inserisci il soggetto di cui vuoi visualizzare i dati: ")
    print("CONSULTARE IL FILE LABEL.CSV PER VEDERE I SOGGETTI DISPONIBILI")

    substring = input()
    sub_upp = substring.upper()
    start=0
    # inizializzo una lista per salvarmi le colonne che mi interessano
    listacolonne=[]
    # scansiono i nomi delle colonne
    for i, subject in enumerate(df.columns):
        # se la sottostringa (nome soggetto esempio: S010 ) è contenuta nel nome
        if sub_upp in df.columns[i]:

            start=i

            # print(df.columns[i])
            start += 1
            # print(start)
            listacolonne.append(int(start))
            # print("Found!")
        # else:
        #     print("Not found!")

    startindex=(listacolonne[0])
    endindex=(listacolonne[-1])
    listafinale=[]
    j=startindex-1
    for x in range(int(startindex), int(endindex+1)):
        # inizializzo una lista in cui mettere gli elementi della colonna
        # che sto prendendo in considerazione
        colselem = []
        # Apro il file
        with open(filepath1) as file_obj:

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
            listafinale.append(colselem)
            j += 1

    numpy_array = np.array(listafinale)
    transpose = numpy_array.T
    transpose_list = transpose.tolist()

    fig, ax =plt.subplots(dpi=1000)

    data=transpose_list
    ax.axis('tight')
    ax.axis('off')
    table= ax.table(cellText=data,loc="center")
    table.scale(1.2,1.5)
    ax.set_title(filepath1.split("/")[2],
                 fontweight="bold")
    plt.show()

print("Digita il numero corrispondente al file di cui vuoi mostrare i dati?")
print("1. Lips_similarity_Sogg_LocalAverage.csv\n2. Lips_similarity_Sogg_GlobalAverage.csv")
print("3. Lips_average_locali.csv\n4. Lips_average_globali.csv")

print("5. Eyes_similarity_Sogg_LocalAverage.csv\n6. Eyes_similarity_Sogg_GlobalAverage.csv")
print("7. Eyes_average_locali.csv\n8. Eyes_average_globali.csv")

print("9. EyeB_similarity_Sogg_LocalAverage.csv\n10. EyeB_similarity_Sogg_GlobalAverage.csv")
print("11. EyeB_average_locali.csv\n12. EyeB_average_globali.csv")

a= int(input())
print(a)

if (a==1):
    # Lips_similarity_Sogg_LocalAverage.csv
    show_table(src_csv1)

if (a==2):
    # Lips_similarity_Sogg_GlobalAverage.csv
    show_table(src_csv2)

if (a == 3):
    # Lips_average_locali.csv
    show_table(src_csv3)

if (a == 4):
    # Lips_average_globali.csv
    show_table(src_csv4)


if (a==5):
    # Eyes_similarity_Sogg_LocalAverage.csv
    show_table(src_csv5)

if (a==6):
    # Eyes_similarity_Sogg_GlobalAverage.csv
    show_table(src_csv6)

if (a == 7):
    # Eyes_average_locali.csv
    show_table(src_csv7)

if (a == 8):
    # Eyes_average_globali.csv
    show_table(src_csv8)


if (a==9):
    # EyeB_similarity_Sogg_LocalAverage.csv
    show_table(src_csv9)

if (a==10):
    # EyeB_similarity_Sogg_GlobalAverage.csv
    show_table(src_csv10)

if (a == 11):
    # EyeB_average_locali.csv
    show_table(src_csv11)

if (a == 12):
    # EyeB_average_globali.csv
    show_table(src_csv12)