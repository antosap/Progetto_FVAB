import glob2
import cv2
import pandas as pd

# mediap_util è il codice della Dott. Bisogni, LIPS la funzione per gli occhi e nel codice della
# bisogni ho cancellato il ritorno di num , ovvero il conteggio dei volti, perchè non mi serve
from mediap_util import LEYEB, REYEB

pathtemp= glob2.glob("imgcampioni/**/*.png")
pathList = [glob2.glob("Dataset/cohn_kanade_1/**/*.png"),
            glob2.glob("Dataset/cohn_kanade_2/**/*.png"),
            glob2.glob("Dataset/cohn_kanade_3/**/*.png"),
            glob2.glob("Dataset/cohn_kanade_4/**/*.png"),
            glob2.glob("Dataset/cohn_kanade_5/**/*.png"),
            glob2.glob("Dataset/cohn_kanade_6/**/*.png"),
            glob2.glob("Dataset/cohn_kanade_7/**/*.png"),
            glob2.glob("Dataset/cohn_kanade_8/**/*.png"),
            glob2.glob("Dataset/cohn_kanade_9/**/*.png")]

def landmark(path):
    # path per la cartella temporanea, glob usa gli ** come wildcard, in questo modo non c'è bisogno di passare staticamente
    # le cartelle e le sottocartelle andando ad automatizzare il processo di scorrimento delle directory
    # for per lo scorrimento delle directory
    for i, file in enumerate(path):

        # creo il dataframe
        image=cv2.imread(file)
        cordL = LEYEB(image)
        cordR = REYEB(image)
        df = pd.DataFrame(cordL+cordR, columns=['x', 'y', 'z'])
        # nome del file
        fileName = ""
        for c in file[::-1]:
            if c == "\\":
                break
            fileName += c
        fileName = fileName[::-1]
        fileName = fileName.replace(".png", "")

        # creo i csv
        pathFile = "csv_landmark/EyeB_csv_landmark/" + fileName + ".csv"
        df.to_csv(pathFile.format(i), sep=',', index=False)

        # incremento contatore file csv
        print(i)


# landmark(pathtemp)

# eseguire manualmente su 2/3 cartelle per volta per evitare errore di memoria fino a soluzione contraria.
landmark(pathList[0])