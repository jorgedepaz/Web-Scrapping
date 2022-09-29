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
    'https://ayuda.baccredomatic.com/es/comercios-afiliados','https://ayuda.baccredomatic.com/es/comercios-afiliados?field_subcategory=All&page=1'
]
verBancaEmpresarial = [
    'https://ayuda.baccredomatic.com/es/banca-empresarial','https://ayuda.baccredomatic.com/es/banca-empresarial?field_subcategory=All&page=1'
]
verpymes = [
    'https://ayuda.baccredomatic.com/es/pymes'
]

wholePages = [
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=2','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=3',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=4','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=5',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=6', 'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=7',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=8', 'https://ayuda.baccredomatic.com/es/tarjetas-de-credito','https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=2','https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=3',
    'https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=4','https://ayuda.baccredomatic.com/es/cuentas-bancarias-y-tarjetas-de-debito','https://ayuda.baccredomatic.com/es/cuentas-bancarias-y-tarjetas-de-debito?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/codigo-bac','https://ayuda.baccredomatic.com/es/codigo-bac?field_subcategory=All&page=1', 'https://ayuda.baccredomatic.com/es/canales-de-atencion','https://ayuda.baccredomatic.com/es/canales-de-atencion?field_subcategory=All&page=1',
     'https://ayuda.baccredomatic.com/es/prestamos', 'https://ayuda.baccredomatic.com/es/seguros-y-coberturas','https://ayuda.baccredomatic.com/es/comercios-afiliados','https://ayuda.baccredomatic.com/es/comercios-afiliados?field_subcategory=All&page=1',
     'https://ayuda.baccredomatic.com/es/banca-empresarial','https://ayuda.baccredomatic.com/es/banca-empresarial?field_subcategory=All&page=1','https://ayuda.baccredomatic.com/es/pymes'

]

wholeDict = {}
imageCont  = 0

for page in verTodasComerciosAfiliados:
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


