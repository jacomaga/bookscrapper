# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
id_book=input("Insert the book's ID:")
nm_pages= int(input("Insert the total number of pages:"))
i=0
while i <= nm_pages:
    urllib.request.urlretrieve("http://staticbv.am4.com.br/publicacoes/"+id_book+"/p_"+str(i)+".jpg","p_"+str(i)+".jpg")
    i += 1