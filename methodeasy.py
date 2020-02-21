# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
from PIL import Image
import glob
import time


#id_book is an optional, bcs in certains cases the URL off the books need to be personalized example: https://libraryoffchicago/books/"id_book"/image1.jpg 
id_book=input("Insert the book's ID:")
nm_pages= int(input("Insert the total number of pages:"))
#name_book = the name off the folder who will be created
name_book= input("What's the book name? ")
#acess rights off the folders 
acess_rights = "0o755"
i=1
images = []
dir_book= os.getcwd()+"/"+name_book
try:
    os.mkdir(name_book)
except OSError:
    print ("Creation of the directory %s failed" % name_book)
else:
    print ("Successfully created the directory %s" % name_book)
begin = time.time()

while i <= nm_pages:
    
    try:

        urllib.request.urlretrieve("http://www.agricultura.gov.br/noticias/cao-e-usado-pela-primeira-vez-na-fiscalizacao-agropecuaria-brasileira/"+str(i)+".jpg"+str(i)+".jpg", name_book+"/p_"+str(i)+".jpg")
        images.append("p_"+str(i)+".jpg")
        i += 1
    

             
    except: print("A problem ocurred")

end=time.time()
print(begin-end)

#After we scrapped the images, now we gonna convert the images into a pdf file
dir_book= os.getcwd()+"/"+name_book
conv_imgs = []

for i in range (len(images)):
    ref = ('%s'% dir_book+"/"+images[i])
    image = Image.open(r'%s'%ref)
    conv_imgs.append(image.convert('RGB'))
    
del(conv_imgs[0])
image1=Image.open(r'%s'% dir_book+"/"+images[0])
img1 = image1.convert('RGB')
img1.save(r''+dir_book+"/"+name_book+".pdf", save_all=True,append_images=conv_imgs)
    

    
    
 
