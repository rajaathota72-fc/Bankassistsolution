import os
D = os.listdir("./user_database")
D.remove(".DS_Store")
print(D)
import shutil
for i in range(len(D)):
    path1 = "user_database/"+D[i]+"/"+D[i]+".wav"
    path2 = "Training_speakervoice/development_sets/"+D[i]+".wav"
    shutil.copyfile(path1,path2)


