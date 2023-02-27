#Web scrapping para la categoria de Banca En Línea Y Banca Móvil

# Importar módulos
from ast import If
import urllib.request as urllib2
import requests

import json
import csv  
from searchData import wholePages

from bs4 import BeautifulSoup

#Ruta raiz
root = 'https://ayuda.baccredomatic.com'

#Diccionario con la data para generar el indice en formato JSON
centroDeAyuda = {}


wholeDict = {}
h22 = list()
for page in wholePages:
##--------------------------Código para la pagina de temas, aqui se obtiene la data de cada articulo de ver todos--------------------------------
    #para obtener informacion de temas con paginas 
    urlPagina = page 
    # Ejecutar GET-Request
    response = requests.get(urlPagina)
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



    #Web scrapping del articulo para buscar todos lo H2 dentro de cada articulo
    h2 = list()
    flagOPA = list()

    testDict ={}
    cont = 0
    for hiperlink in hiperlinkHtmlExtended:
        responseArticle = requests.get(hiperlink)
        htmlArticle = BeautifulSoup(responseArticle.text, 'html.parser')
        #-------La linea de abajo hace referencia a todo el body-------
        soup = htmlArticle.find('div', {"class" :"row bs-1col node node--type-book node--view-mode-full"}) 
        
        #------La linea siguiente busca todos los anchor, se comentará para dejar el template
        # for a in soup.find_all('a', href=True):
        #     href.append(a['href'])
        #     href2.append(a['href'])
        
        #------La linea siguiente buscará todos los h2
        
        #all_in = soup.find('h2', {"class" :"content-navigation-0 arrow-up accordion-h2"})
        all_in =  soup.find_all('h2')
        print(all_in)
        for header2 in all_in:
            h2.append(header2.text.strip())
            h22.append(header2.text.strip())

        testDict.setdefault(articleTitles[cont],{})
        testDict[articleTitles[cont]].setdefault("direccion",hiperlink)
        testDict[articleTitles[cont]].setdefault("headers 2",h2)
        h2 = list()
        cont+=1
    
    wholeDict.update(testDict)
    #testDict ={} ojo con esta asignacion
    
json_data = json.dumps(wholeDict,ensure_ascii=False,indent=3).encode('utf8')
print(json_data.decode()) 

with open('article_h2.json', 'w') as f:
    json.dump(wholeDict, f,ensure_ascii=False, indent=2)
    print("Archivo json creado")

with open('h2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(h22)
    print("Archivo csv creado")

print("Cantidad de articulos analizados: "+str(len(wholeDict)))     
print("Cantidad total de h2 encontrados: "+str(len(h22)))    

#print("Todos los H2 del último articulo: "+str(all_in))
#2143
