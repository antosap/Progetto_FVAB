import glob2
import pandas as pd
import os.path

# controllo se il file csv esiste già

if os.path.isfile('test_32_sogg/label/label.csv'):
        print("FILE ESISTENTE! \nATTENDERE, ELIMINO E RICREO!")
        # cancella il csv vecchio nella destination path
        os.remove('test_32_sogg/label/label.csv')
else:
        print("FILE INESISTENTE! \nATTENDERE, CREAZIONE DEL FILE!")


path = glob2.glob("test_32_sogg/csv_landmark/Lips_csv_landmark/*.csv")
path_dest = ("test_32_sogg/label/")

sogg_list = []
emo_list = []
pivot = 0

# scorro i csv
for file in path:

    # nome del file
    fileName = ""
    for c in file[::-1]:
        if c == "\\":
            break
        fileName += c
    fileName = fileName[::-1]
    # fileName = fileName.replace(".csv", "")
    s = fileName.split('_')

    sogg = s[0]
    emozioni = s[1]
    # print(sogg)

    # faccio la lista inerente al soggetto e all'emozione
    sogg_list.append(sogg)
    emo_list.append(emozioni)
    # print(emozioni)
    df = pd.DataFrame({'Soggetti': sogg_list, 'emozioni': emo_list})

    df_duplicates_removed = df.drop_duplicates(subset=['emozioni'])
    # print(df_duplicates_removed)

    dfuno = pd.DataFrame(df, columns=['Soggetti', 'emozioni'])

    df_duplicates_removed = dfuno.drop_duplicates()
    # print(df_duplicates_removed)
    df_duplicates_removed.to_csv(path_dest + "label.csv", sep=",", index=None)

# print(df_duplicates_removed)