import os

# directory
# path = r"C:\Users\macro\Documents\GitHub\Progetto_FVAB\Esame\Dataset\cohn_kanade_3\S042\003\\"
path = r"C:\Users\macro\Documents\GitHub\Progetto_FVAB\Esame\Dataset\cohn_kanade_7\S125\008\\"
# nuovo _00x_
new_emotion = "_003_"
# lista di tutti i file nella directory inserita
files_in_dir = os.listdir(path)

# per ogni file nella directory
for file in files_in_dir:
    print(file)
    new_name = path + r"\\" + file.split("_")[0] + new_emotion + file.split("_")[2]
    os.rename(path + file, new_name)





