import os
D = os.listdir("./user_database")
D.remove(".DS_Store")
print(D)
import shutil
for i in range(len(D)):
    path1 = "user_database/"+D[i]+"/"+D[i]+".wav"
    path2 = "Training_speakervoice/development_sets/"+D[i]+".wav"
    shutil.copyfile(path1,path2)
    path3 = "user_database/" + D[i] + "/" + D[i] + ".png"
    #os.mkdir("Training_speakervoice/image_development_sets/"+D[i])
    path4 = "Training_speakervoice/image_development_sets/" + D[i]+".png"
    shutil.copyfile(path3, path4)

