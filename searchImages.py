#Web scrapping para la categoria de Banca En Línea Y Banca Móvil

# Importar módulos
from ast import If
import urllib.request as urllib2
import requests

import json
import csv  

from bs4 import BeautifulSoup
from searchData import wholePages
#Ruta raiz
root = 'https://ayuda.baccredomatic.com'

#Diccionario con la data para generar el indice en formato JSON
centroDeAyuda = {}


wholeDict = {}
imageCont  = 0

for page in wholePages:
    #Para obtener informacion de temas con paginas
    # Ejecutar GET-Request
    response = requests.get(page)

    # Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
    html = BeautifulSoup(response.text, 'html.parser')

    # Extraer el titulo de los articulos + la descripcion + el hipervinculo
    articleTitlesHtml = html.find_all('h3', class_="field-content")

    # Crear una lista de los titulos de los articulos
    articleTitles = list()
    for articleTitle in articleTitlesHtml:    
        articleTitles.append(articleTitle.text.strip())
    
    # Crear una lista de los hipervinculos de cada articulo
    hiperlinkHtml = list()

    for article in articleTitlesHtml:
        hiperlinkHtml.append(article.find('a')['href'])

    #Lista concatenada con la ruta completa
    hiperlinkHtmlExtended = list()

    for link in hiperlinkHtml:
        link = root+str(link)
        hiperlinkHtmlExtended.append(link)



    #Web scrapping del articulo para setear el flag GT y obtener la última actualización 
    src = list()
    alt = list()
    
    

    testDict ={}
    cont = 0
    
    for hiperlink in hiperlinkHtmlExtended:
        responseArticle = requests.get(hiperlink)
        htmlArticle = BeautifulSoup(responseArticle.text, 'html.parser')
        soup = htmlArticle.find('div', {"class" :"row bs-1col node node--type-book node--view-mode-full"}) 
        
        for image in soup.find_all('img'):
            src.append(image['src'])
            alt.append(image['alt'])
            imageCont  += 1    #Para contar la cantidad total de imágenes

        testDict.setdefault(articleTitles[cont],{})
        testDict[articleTitles[cont]].setdefault("direccion",hiperlink)
        testDict[articleTitles[cont]].setdefault("imagen",src)
        testDict[articleTitles[cont]].setdefault("descripcion imagen",alt)
        src = list()
        alt = list()
        cont+=1
    
    wholeDict.update(testDict)
    testDict ={}

json_data = json.dumps(wholeDict,ensure_ascii=False,indent=3).encode('utf8')
#print(json_data.decode()) 
with open('article_images.json', 'w') as f:
    json.dump(wholeDict, f, indent=2)
    print("Archivo json creado")


print("Cantidad de articulos analizados: "+str(len(wholeDict)))     
print("Cantidad total de imagenes encontradas: "+str(imageCont))     


