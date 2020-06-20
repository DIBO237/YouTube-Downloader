from pytube import YouTube# misc
import os
import shutil
import math
import datetime
import progressbar 
from tqdm import tqdm

print('''
          ==========================================
          =     YouTUBE VIDEO DoWNlOader V 1.0     =                                                                           
          =             By DIBO237#                =
          ==========================================
          

''')
try:
    f = input(" Enter Full VIdeo LINK: ")
    print("  Please Wait Till it Dowloads.... :)")
    
    video = YouTube(f)
    ytvideo=YouTube(f).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('./Downloaded VIdeo'):
        os.makedirs('./Downloaded VIdeo')
    ytvideo.download('./Downloaded VIdeo')
    
    for data in tqdm(iterable = ytvideo.iter_content(chunk_size = chunk_size),
                     total = size/chunk_size, unit = 'KB'):
        print("  Downlode Completed............. :)")
    
    
except:
      print()
      print(" <====> You have entered Incorrect LInk... ; (  <====>  ")
        
