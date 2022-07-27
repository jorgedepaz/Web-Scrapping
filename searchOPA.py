#Web scrapping para la categoria de Banca En Línea Y Banca Móvil

# Importar módulos
from ast import If
import urllib.request as urllib2
import requests

import json
import csv  

from bs4 import BeautifulSoup

#Ruta raiz
root = 'https://ayuda.baccredomatic.com'

#Diccionario con la data para generar el indice en formato JSON
centroDeAyuda = {}

verTodasBancaEnLinea = [
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=2','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=3',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=4','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=5',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=6', 'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=7',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=8'
    ]

verTodasTarjetasDeCredito = [
    'https://ayuda.baccredomatic.com/es/tarjetas-de-credito','https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=2','https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=3',
    'https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=4'
]

verTodasCuentasBancarias = [
    'https://ayuda.baccredomatic.com/es/cuentas-bancarias-y-tarjetas-de-debito','https://ayuda.baccredomatic.com/es/cuentas-bancarias-y-tarjetas-de-debito?field_subcategory=All&page=1'
]

verTodasCodigoBAC = [
    'https://ayuda.baccredomatic.com/es/codigo-bac','https://ayuda.baccredomatic.com/es/codigo-bac?field_subcategory=All&page=1'
]
verTodasCanalesDeAtencion=[
    'https://ayuda.baccredomatic.com/es/canales-de-atencion','https://ayuda.baccredomatic.com/es/canales-de-atencion?field_subcategory=All&page=1'
]
verTodasPrestamos = [
    'https://ayuda.baccredomatic.com/es/prestamos'
]

verTodasSeguroYCoverturas =[
    'https://ayuda.baccredomatic.com/es/seguros-y-coberturas'
]

verTodasComerciosAfiliados = [
    'https://ayuda.baccredomatic.com/es/comercios-afiliados'
]

wholePages = [
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=2','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=3',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=4','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=5',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=6', 'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=7',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=8','https://ayuda.baccredomatic.com/es/tarjetas-de-credito','https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=2','https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=3',
    'https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=4','https://ayuda.baccredomatic.com/es/cuentas-bancarias-y-tarjetas-de-debito','https://ayuda.baccredomatic.com/es/cuentas-bancarias-y-tarjetas-de-debito?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/codigo-bac','https://ayuda.baccredomatic.com/es/codigo-bac?field_subcategory=All&page=1','https://ayuda.baccredomatic.com/es/canales-de-atencion','https://ayuda.baccredomatic.com/es/canales-de-atencion?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/prestamos','https://ayuda.baccredomatic.com/es/seguros-y-coberturas','https://ayuda.baccredomatic.com/es/comercios-afiliados'
]
wholeDict = {}
href2 = list()
for page in wholePages:
    #para obtener informacion de temas con paginas
    #urlPagina = 'https://ayuda.baccredomatic.com/es/seguros-y-coberturas?subcategory=Tipos%20de%20Seguro' 
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



    #Web scrapping del articulo para setear el flag GT y obtener la última actualización 
    href = list()
    flagOPA = list()

    testDict ={}
    cont = 0
    for hiperlink in hiperlinkHtmlExtended:
        responseArticle = requests.get(hiperlink)
        htmlArticle = BeautifulSoup(responseArticle.text, 'html.parser')
        soup = htmlArticle.find('div', {"class" :"row bs-1col node node--type-book node--view-mode-full"}) 
        
        for a in soup.find_all('a', href=True):
            href.append(a['href'])
            href2.append(a['href'])

        testDict.setdefault(articleTitles[cont],{})
        testDict[articleTitles[cont]].setdefault("direccion",hiperlink)
        testDict[articleTitles[cont]].setdefault("hipervinculos",href)
        href = list()
        cont+=1
    
    wholeDict.update(testDict)
    testDict ={}
    
json_data = json.dumps(wholeDict,ensure_ascii=False,indent=3).encode('utf8')
#print(json_data.decode()) 
with open('article_hiperlinks.json', 'w') as f:
    json.dump(wholeDict, f, indent=2)
    print("Archivo json creado")




with open('hiperlinks.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(href2)
    print("Archivo csv creado")

print("Cantidad de articulos analizados: "+str(len(wholeDict)))     
print("Cantidad total de hiperviculos encontrados: "+str(len(href2)))     
#2143
