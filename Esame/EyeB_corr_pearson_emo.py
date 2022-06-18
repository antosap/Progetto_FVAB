import pandas as pd

path1 = "test_32_sogg/csv_average/EyeB_csv_average/EyeB_average_locali.csv"
path2 = "test_32_sogg/csv_average/EyeB_csv_average/EyeB_average_globali.csv"
pathdest1 = "test_32_sogg/corr_pearson/EyeB_corr_pearson/EyeB_corr_pearson_emo_locali/"
pathdest2 = "test_32_sogg/corr_pearson/EyeB_corr_pearson/EyeB_corr_pearson_emo_globali/"
expression_csv = "test_32_sogg/cosine_similarities/EyeB_cosine_similarities/EyeB_similarity_emo_GlobalAverage.csv"


def corr_pearson_emo(path, pathdest):
    # lettura csv
    df = pd.read_csv(path)

    # lista di colonne ordinate per espressione
    col_expressions = list(pd.read_csv(expression_csv).columns)
    col_expressions_ordered = []

    # creazione lista di lista di espressioni
    expressions_list = []
    for i, col in enumerate(col_expressions):
        # aggiungo espressione alla lista buffer
        expressions_list.append(col)
        # controllo se il prossimo elemento esiste
        if i + 1 < len(col_expressions):
            # controllo se il prossimo elemento si riferisce a una nuova espressione
            if col.split("_")[1] != col_expressions[i + 1].split("_")[1]:
                # aggiungo la lista di soggetti con espressioni uguali alla lista di lista ordinata
                col_expressions_ordered.append(expressions_list)
                # svuoto il buffer
                expressions_list = []
        # se mi trovo all'ultimo elemento
        else:
            # aggiungo la lista buffer alla lista di lista ordinata
            col_expressions_ordered.append(expressions_list)
            # svuoto il buffer
            expressions_list = []

    # scorro la lista ordinata per espressioni
    for subject in col_expressions_ordered:
        # ottengo il sub-dataframe per espressione
        df_subject = df.get(subject)
        # calcolo correlazione e genero csv
        df_subject.corr(method="pearson").to_csv(pathdest + "emo_" + subject[0].split("_")[1] + ".csv", sep=",")
        # print(subject[0].split("_")[1])


corr_pearson_emo(path1, pathdest1)
corr_pearson_emo(path2, pathdest2)

