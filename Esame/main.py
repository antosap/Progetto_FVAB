# i landmark sono già stati generati, di conseguenza gli import sono stati commentati

# import Lips_csv_landmark
# import EyeB_csv_landmark
# import Eyes_csv_landmark

# questo import richiama il codice di estrazione di Soggetto ed Emozione e li mette in un csv
print("\nGENERAZIONE FILE LABEL.CSV CONTENENTE SOGGETTI ED EMOZIONI")
import label
print("FILE LABEL.CSV GENERATO CON SUCCESSO")

print("\n|-----------LIPS-------------------------------------------------------------|\n")
print("GENERAZIONE DEI DATI PER LIPS\n")

# Gli import di seguito lavoreranno sui csv relativi ai punti estratti dalle labbra
# local_distances e global_distances calcolano le distanze locali e globali per ogni frame
print("GENERAZIONE DEI FILE CONTENENTI LE DISTANZE LOCALI PER LIPS")
import Lips_local_distances
print("FILE DELLE DISTANZE LOCALI GENERATO CON SUCCESSO")

print("\nGENERAZIONE DEI FILE CONTENENTI LE DISTANZE GLOBALI PER LIPS")
import Lips_global_distances
print("FILE DELLE DISTANZE GLOBALI GENERATO CON SUCCESSO")

# average distances calcola la media delle colonne nel csv delle distanze prendendo in considerazione
# le 4 colonne prima e dopo la colonna centrale del csv
print("\nGENERAZIONE DEI FILE CONTENENTI LE MEDIE PER DISTANZE LOCALI E GLOBALI PER LIPS")
import Lips_average_distances
print("FILE DELLE MEDIE GENERATI CON SUCCESSO")

# cosine_similarity_Sogg, fissando un soggetto e facendo variare l'emozione
# calcola la similarità che c'è tra le colonne all'interno dei file medie
print("\nGENERAZIONE DEI FILE CONTENENTI LE SIMILARITA' PER SOGGETTO PER LIPS")
import Lips_cosine_similarity_sogg
print("FILE DELLE SIMILARITA' PER SOGGETTO GENERATI CON SUCCESSO")

print("\nGENERAZIONE DEI FILE CONTENENTI LE SIMILARITA' PER EMOZIONE PER LIPS")
import Lips_cosine_similarities_emo
print("FILE DELLE SIMILARITA' PER EMOZIONE GENERATI CON SUCCESSO")

# corr_pearson_sogg calcola la correlazione di Pearson sui csv delle medie
# fissando un soggetto e facendo variare l'emozione
print("\nGENERAZIONE DEI FILE CONTENENTI LE CORRELAZIONI DI PEARSON' PER SOGGETTO PER LIPS")
import Lips_corr_pearson_sogg
print("FILE DELLE CORRELAZIONI PER SOGGETTO GENERATI CON SUCCESSO")

# corr_pearson_sogg calcola la correlazione di Pearson sui csv delle medie
# fissando l'emozione e facendo variare i soggetti
print("\nGENERAZIONE DEI FILE CONTENENTI LE CORRELAZIONI DI PEARSON' PER EMOZIONE PER LIPS")
import Lips_corr_pearson_emo
print("FILE DELLE CORRELAZIONI PER EMOZIONE GENERATI CON SUCCESSO")

# Gli import di seguito svolgono le stesse cose dei precedenti
# ma lavoreranno sui csv relativi ai punti estratti dagli occhi
print("\n|-----------EYES-------------------------------------------------------------|\n")
print("GENERAZIONE DEI DATI PER EYES\n")

print("GENERAZIONE DEI FILE CONTENENTI LE DISTANZE LOCALI PER EYES")
import Eyes_local_distances
print("FILE DELLE DISTANZE LOCALI GENERATO CON SUCCESSO")


print("\nGENERAZIONE DEI FILE CONTENENTI LE DISTANZE GLOBALI PER EYES")
import Eyes_global_distances
print("FILE DELLE DISTANZE GLOBALI GENERATO CON SUCCESSO")

print("\nGENERAZIONE DEI FILE CONTENENTI LE MEDIE PER DISTANZE LOCALI E GLOBALI PER EYES")
import Eyes_average_distances
print("FILE DELLE MEDIE GENERATI CON SUCCESSO")


print("\nGENERAZIONE DEI FILE CONTENENTI LE SIMILARITA' PER SOGGETTO PER EYES")
import Eyes_cosine_similarity_sogg
print("FILE DELLE SIMILARITA' PER SOGGETTO GENERATI CON SUCCESSO")

print("\nGENERAZIONE DEI FILE CONTENENTI LE SIMILARITA' PER EMOZIONE PER EYES")
import Eyes_cosine_similarities_emo
print("FILE DELLE SIMILARITA' PER EMOZIONE GENERATI CON SUCCESSO")


print("\nGENERAZIONE DEI FILE CONTENENTI LE CORRELAZIONI DI PEARSON' PER SOGGETTO PER EYES")
import Eyes_corr_pearson_sogg
print("FILE DELLE CORRELAZIONI PER SOGGETTO GENERATI CON SUCCESSO")


print("\nGENERAZIONE DEI FILE CONTENENTI LE CORRELAZIONI DI PEARSON' PER EMOZIONE PER EYES")
import Eyes_corr_pearson_emo
print("FILE DELLE CORRELAZIONI PER EMOZIONE GENERATI CON SUCCESSO")


# Gli import di seguito svolgono le stesse cose dei precedenti
# ma lavoreranno sui csv relativi ai punti estratti dalle sopracciglia
print("\n|-----------EYEBROWS-------------------------------------------------------------|\n")
print("GENERAZIONE DEI DATI PER EYEBROWS\n")


print("GENERAZIONE DEI FILE CONTENENTI LE DISTANZE LOCALI PER EYEBROWS")
import EyeB_local_distances
print("FILE DELLE DISTANZE LOCALI GENERATO CON SUCCESSO")


print("\nGENERAZIONE DEI FILE CONTENENTI LE DISTANZE GLOBALI PER EYEBROWS")
import EyeB_global_distances
print("FILE DELLE DISTANZE GLOBALI GENERATO CON SUCCESSO")

print("\nGENERAZIONE DEI FILE CONTENENTI LE MEDIE PER DISTANZE LOCALI E GLOBALI PER EYEBROWS")
import EyeB_average_distances
print("FILE DELLE MEDIE GENERATI CON SUCCESSO")


print("\nGENERAZIONE DEI FILE CONTENENTI LE SIMILARITA' PER SOGGETTO PER EYEBROWS")
import EyeB_cosine_similarity_sogg
print("FILE DELLE SIMILARITA' PER SOGGETTO GENERATI CON SUCCESSO")

print("\nGENERAZIONE DEI FILE CONTENENTI LE SIMILARITA' PER EMOZIONE PER EYEBROWS")
import EyeB_cosine_similarities_emo
print("FILE DELLE SIMILARITA' PER EMOZIONE GENERATI CON SUCCESSO")


print("\nGENERAZIONE DEI FILE CONTENENTI LE CORRELAZIONI DI PEARSON' PER SOGGETTO PER EYEBROWS")
import EyeB_corr_pearson_sogg
print("FILE DELLE CORRELAZIONI PER SOGGETTO GENERATI CON SUCCESSO")


print("\nGENERAZIONE DEI FILE CONTENENTI LE CORRELAZIONI DI PEARSON' PER EMOZIONE PER EYEBROWS")
import EyeB_corr_pearson_emo
print("FILE DELLE CORRELAZIONI PER EMOZIONE GENERATI CON SUCCESSO")



# import table
