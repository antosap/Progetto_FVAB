import pandas as pd

path1 = "test_32_sogg/csv_average/Eyes_csv_average/Eyes_average_locali.csv"
path2 = "test_32_sogg/csv_average/Eyes_csv_average/Eyes_average_globali.csv"
pathdest1 = "test_32_sogg/corr_pearson/Eyes_corr_pearson/Eyes_corr_pearson_sogg_locali/"
pathdest2 = "test_32_sogg/corr_pearson/Eyes_corr_pearson/Eyes_corr_pearson_sogg_globali/"


def corr_pearson_sogg(path, pathdest):
    # lettura csv
    df = pd.read_csv(path)

    # lettura colonne
    col_names = list(df.columns)
    # inizializzo lista per poter identificare i soggetti nei file csv
    col_names_ordered = []
    subject_list = []

    # ciclo che mi permette di mettere in liste separate i soggetti con relativi dati
    for i, col in enumerate(col_names):
        subject_list.append(col)
        if i + 1 < len(col_names):
            if col.split("_")[0] != col_names[i + 1].split("_")[0]:
                col_names_ordered.append(subject_list)
                subject_list = []

    # ciclo che mi permette di andare ad effettuare la correlazione di pearson per soggetto
    # prendendo in considerazione ogni lista di soggetti
    # (correlazione sulla lista contenente il soggetto X) e generare più file CSV
    for subject in col_names_ordered:
        df_subject = df.get(subject)
        df_subject.corr(method="pearson").to_csv(pathdest + subject[0].split("_")[0] + ".csv", sep=",")


corr_pearson_sogg(path1, pathdest1)
corr_pearson_sogg(path2, pathdest2)
