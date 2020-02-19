# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
id_book=input("Insert the book's ID:")
nm_pages= int(input("Insert the total number of pages:"))
name_book= input("What's the book name?")
acess_rights = "0o755"
i=1
images = []
try:
    os.mkdir(name_book)
except OSError:
    print ("Creation of the directory %s failed" % name_book)
else:
    print ("Successfully created the directory %s" % name_book)

while i <= nm_pages:
    urllib.request.urlretrieve("http://www.agricultura.gov.br/noticias/cao-e-usado-pela-primeira-vez-na-fiscalizacao-agropecuaria-brasileira/"+str(i)+".jpg", "p_"+str(i)+".jpg")
    images.append("p_"+str(i)+".jpg")
    i += 1
    urllib.request.urlretrieve("http://www.agricultura.gov.br/noticias/cao-e-usado-pela-primeira-vez-na-fiscalizacao-agropecuaria-brasileira/"+str(i)+".jpg", "p_"+str(i)+".jpg")
    images.append("p_"+str(i)+".jpg")
    i += 1
    urllib.request.urlretrieve("http://www.agricultura.gov.br/noticias/cao-e-usado-pela-primeira-vez-na-fiscalizacao-agropecuaria-brasileira/"+str(i)+".jpg", "p_"+str(i)+".jpg")
    images.append("p_"+str(i)+".jpg")
    i += 1
    urllib.request.urlretrieve("http://www.agricultura.gov.br/noticias/cao-e-usado-pela-primeira-vez-na-fiscalizacao-agropecuaria-brasileira/"+str(i)+".jpg", "p_"+str(i)+".jpg")
    images.append("p_"+str(i)+".jpg")
    i += 1
print(images)    
"""
    urllib.request.urlretrieve("http://www.agricultura.gov.br/noticias/cao-e-usado-pela-primeira-vez-na-fiscalizacao-agropecuaria-brasileira/"+id_book+"/p_"+str(i)+".jpg", "p_"+str(i)+".jpg")
    images.append("p_"+str(i)+".jpg")
    i += 1
    urllib.request.urlretrieve("http://URL.com.br/publicacoes/"+id_book+"/p_"+str(i)+".jpg","p_"+str(i)+".jpg")
    images.append("p_"+str(i)+".jpg")
    i += 1
    urllib.request.urlretrieve("http://URL.com.br/publicacoes/"+id_book+"/p_"+str(i)+".jpg","p_"+str(i)+".jpg")
    images.append("p_"+str(i)+".jpg")
    i += 1
    urllib.request.urlretrieve("http://URL.com.br/publicacoes/"+id_book+"/p_"+str(i)+".jpg","p_"+str(i)+".jpg")
    images.append("p_"+str(i)+".jpg")
    i += 1
"""