import fnmatch
import os,sys
import pandas as pd
import shutil
import numpy as np

df = pd.read_csv('/hampiholidata/Project/Datasets/imdb/Augment/augment.csv')
img_files = df['Images']
#pth = df['Path']
#print(img_files) 
mypath='/hampiholidata/Project/Datasets/imdb/'
file_list= []
for i, files in enumerate(img_files):
   images= os.path.join(mypath,files) 
   print("Copying",images)
   #if len(images) > 0:
    # file_list.append(os.path.join(pth[i],images[0]))
     #ages.append(age[i])
   shutil.copy(os.path.join(mypath,images),'/hampiholidata/Project/Datasets/imdb/Augment/augment_imdb')
#df1 = pd.DataFrame({'Images': file_list})
#df2 = pd.DataFrame({'Ages': ages})
#df1.to_csv('/home/hampiholi/Project/Datasets/imdb/Adience_refined_Image.csv')  
#df2.to_csv('/home/hampiholi/Project/Datasets/imdb/Adience_refined_ages.csv') 
#np.savetxt('/home/hampiholi/Project/Datasets/imdb/Adience_refined.csv',file_list)
print('Done')
