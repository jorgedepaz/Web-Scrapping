#Web scrapping para la categoria de Banca En Línea Y Banca Móvil

# Importar módulos
from ast import If
import urllib.request as urllib2
import requests
import json
from bs4 import BeautifulSoup

#Ruta raiz
root = 'https://ayuda.baccredomatic.com/'

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


#para obtener informacion de temas con paginas
urlPagina = 'https://ayuda.baccredomatic.com/es/seguros-y-coberturas?subcategory=Tipos%20de%20Seguro' 
# Ejecutar GET-Request
response = requests.get(urlPagina)

# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')

# Extraer el titulo de los articulos + la descripcion + el hipervinculo
articleTitlesHtml = html.find_all('h3', class_="field-content")

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
flagGT = list() 
flagCRI = list() 
flagSLV = list() 
flagHND = list() 
flagNIC = list() 
flagPAN = list() 

#Guatemala
#Costa Rica
#El Salvador
#Honduras   
#Nicaragua
#Panamá 

articleLastUpdate = list()   
for hiperlink in hiperlinkHtmlExtended:
    responseArticle = requests.get(hiperlink)
    htmlArticle = BeautifulSoup(responseArticle.text, 'html.parser')
    articleLastUpdate.append(htmlArticle.find('div', {"class" :"field field--name-node-changed-date field--type-ds field--label-inline"}).find('div',{"class" :"field--item"}))
    soup = htmlArticle.find('div', {"class" :"row bs-1col node node--type-book node--view-mode-full"}) 
    
    #------Guatemala---------
    if(str(soup).find("Guatemala")>=0):
        print(str(soup).find("Guatemala"))
        flagGT.append(True)
    elif(str(soup).find("Guatemala")<0):
        print(str(soup).find("Guatemala"))
        flagGT.append(False) 
    #------Costa Rica---------
    if(str(soup).find("Costa Rica")>=0):
        print(str(soup).find("Costa Rica"))
        flagCRI.append(True)
    elif(str(soup).find("Costa Rica")<0):
        print(str(soup).find("Costa Rica"))
        flagCRI.append(False) 
    #------El Salvador---------
    if(str(soup).find("El Salvador")>=0):
        print(str(soup).find("El Salvador"))
        flagSLV.append(True)
    elif(str(soup).find("El Salvador")<0):
        print(str(soup).find("El Salvador"))
        flagSLV.append(False) 
    #------Honduras---------
    if(str(soup).find("Honduras")>=0):
        print(str(soup).find("Honduras"))
        flagHND.append(True)
    elif(str(soup).find("Honduras")<0):
        print(str(soup).find("Honduras"))
        flagHND.append(False)
    #------Nicaragua---------
    if(str(soup).find("Nicaragua")>=0):
        print(str(soup).find("Nicaragua"))
        flagNIC.append(True)
    elif(str(soup).find("Nicaragua")<0):
        print(str(soup).find("Nicaragua"))
        flagNIC.append(False) 
    #------Panamá---------
    if(str(soup).find("Panamá")>=0):
        print(str(soup).find("Panamá"))
        flagPAN.append(True)
    elif(str(soup).find("Panamá")<0):
        print(str(soup).find("Panamá"))
        flagPAN.append(False) 
    

# Crear una lista de los ultimos updates de cada articulo
lastUpdates =list()
for lastUpdate in articleLastUpdate:
    lastUpdates.append(lastUpdate.text.strip())
#----------------------------------------------------




#---------------------------------------------- a partir de aqui se conforma el JSON


# cont = 0
# testDict ={}
# #Realizar scrapping dentro del ciclo para analizar si existe la palabra Guatemala dentro del texto
# #El campo "GT" sera True si el articulo contiene la palabra, de lo contrario sera False.
# for title in articleTitles:

#     testDict.setdefault(title,{})
#     testDict[title].setdefault("hipervinculo",hiperlinkHtmlExtended[cont])
#     testDict[title].setdefault("descripcion",descriptionTitles[cont])
#     testDict[title].setdefault("Última actualización",lastUpdates[cont])
#     testDict[title].setdefault("GT",flagGT[cont])
#     testDict[title].setdefault("CRI",flagCRI[cont])
#     testDict[title].setdefault("SLV",flagSLV[cont])
#     testDict[title].setdefault("HND",flagHND[cont])
#     testDict[title].setdefault("NIC",flagNIC[cont])
#     testDict[title].setdefault("PAN",flagPAN[cont])
#     cont+=1
    


# json_data = json.dumps(testDict,ensure_ascii=False,indent=3).encode('utf8')
# print(flagGT)
# print('---------------------------------------Abajo el JSON------------------------------------------------')
# #print(articleLastUpdate)
# print(json_data.decode()) 