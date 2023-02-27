#Web scrapping para la categoria de Banca En Línea Y Banca Móvil
# Importar módulos
from ast import For, If
import urllib.request as urllib2
import requests
import json
from bs4 import BeautifulSoup
import os

# Whole pages es el array que contiene todas los links de las paginas
from searchData import wholePages
# Gestiones es el array que contiene todas las gestiones a buscar
from searchData import gestiones

#Ruta raiz
root = 'https://ayuda.baccredomatic.com/'

"""
#Ruta de la categoria, se agrega el numero correlativo de las catrogia
urlCategoria = 'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?subcategory='

# Dirección dentro del centro de ayuda
urlsTemas = ['COMPASS','Pagos%20de%20servicios','Problemas%20en%20Banca%20en%20Línea%20y%20Banca%20Móvil','Solicitudes%20y%20gestiones%20en%20línea','Transferencias','Usuario%20y%20contraseña']
"""

#Diccionario con la data para generar el indice en formato JSON
centroDeAyuda = {}

#para obtener informacion de temas con paginas
#urlPagina = 'https://ayuda.baccredomatic.com/es/comercios-afiliados' 
wholeDict = {}
href2 = list()
testDict ={}
contadorGT = 0
contadorBel = 0
contadorBM = 0
print(len(gestiones))

for page in wholePages:
    urlPagina = page
    response = requests.get(urlPagina)

    # Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
    html = BeautifulSoup(response.text, 'html.parser')

    # Extraer el titulo de los articulos + la descripcion + el hipervinculo
    articleTitlesHtml = html.find_all('h3', class_="field-content")
    descriptionTitlesHtml = html.find_all('div', class_="field field--name-field-summary field--type-string-long field--label-hidden field--item")

    #para encontrar si tienen numero de pagina
    pageNumber = html.find_all('ul', class_="pagination js-pager__items")

    # Crear una lista de los titulos de los articulos
    articleTitles = list()
    for articleTitle in articleTitlesHtml:    
        articleTitles.append(articleTitle.text.strip())

    # Crear una lista de los numeros de paginas
    # articleTitles = list()
    # for articleTitle in articleTitlesHtml:    
    #     articleTitles.append(articleTitle.text.strip())

    # Crear una lista de los hipervinculos de cada articulo
    hiperlinkHtml = list()
    for article in articleTitlesHtml:
        hiperlinkHtml.append(article.find('a')['href'])

    #Lista concatenada con la ruta completa
    hiperlinkHtmlExtended = list()
    for link in hiperlinkHtml:
        link = root+str(link)
        hiperlinkHtmlExtended.append(link)

    # Crear una lista de las descripciones de los articulos
    descriptionTitles = list()
    for descriptionTitle in descriptionTitlesHtml:
        descriptionTitles.append(descriptionTitle.text.strip()) 


    #Web scrapping del articulo para setear el flag GT y obtener la última actualización 
    flagGT = list() 
    flagCRI = list() 
    flagSLV = list() 
    flagHND = list() 
    flagNIC = list() 
    flagPAN = list() 

    flagBel = list()
    flagBM = list()
#-------------------------------------------------------------------------------------------------------------
    cont = 0
    #Realizar scrapping dentro del ciclo para analizar si existe la palabra Guatemala dentro del texto
    #Se arma un arra
    for gestion in gestiones:
        testDict.setdefault(gestion,{})
        # testDict[title].setdefault("hipervinculo",hiperlinkHtmlExtended[cont])
        # testDict[title].setdefault("descripcion",descriptionTitles[cont])
        # testDict[title].setdefault("Última actualización",lastUpdates[cont])
        # testDict[title].setdefault("BeL",flagBel[cont])
        # testDict[title].setdefault("BM",flagBM[cont])
        # testDict[title].setdefault("GT",flagGT[cont])
        # testDict[title].setdefault("CRI",flagCRI[cont])
        # testDict[title].setdefault("SLV",flagSLV[cont])
        # testDict[title].setdefault("HND",flagHND[cont])
        # testDict[title].setdefault("NIC",flagNIC[cont])
        # testDict[title].setdefault("PAN",flagPAN[cont])
        # articleLastUpdate = list()   
        # cont+=1
    
    articleLastUpdate = list() 
    #Lista para indexar los hiperviculos de cada gestión 
    
    for hiperlink in hiperlinkHtmlExtended:
        cont = 0
        hiperlinksList = list()
        responseArticle = requests.get(hiperlink)
        htmlArticle = BeautifulSoup(responseArticle.text, 'html.parser')
        articleLastUpdate.append(htmlArticle.find('div', {"class" :"field field--name-node-changed-date field--type-ds field--label-inline"}).find('div',{"class" :"field--item"}))
        #Se encuentra filtra solo el texto del Body
        soup = htmlArticle.find('div', {"class" :"row bs-1col node node--type-book node--view-mode-full"})
        #soup.lower()

        #Ciclo para buscar las gestiones por nombre
        for gestion in gestiones:
            if(str(soup).lower().find(gestion)>=0):
                print(str(soup).find(gestion))
                
                hiperlinksList.append(hiperlink)
                testDict[gestion].setdefault("hipervinculo "+str(cont),hiperlink)
                cont+=1    
            elif(str(soup).find(gestion)<0):
                print(str(soup).find(gestion))
            
    wholeDict.update(testDict)

    # Crear una lista de los ultimos updates de cada articulo
    # lastUpdates =list()
    # for lastUpdate in articleLastUpdate:
    #     lastUpdates.append(lastUpdate.text.strip())
    #----------------------------------------------------

    #-----------------------------------------------------------------------------------
    #Se crea el documento JSON
    json_data = json.dumps(testDict,ensure_ascii=False,indent=3).encode('utf8')
    
    #Crear el archivo
with open(os.path.join('C:/Users/jorge.depazr/Documents/Dev/Web Scrapping/results','gestiones.json'), 'w', encoding="utf-8") as f:
    #str(wholeDict).encode('utf-8')  #<---Se agregaria esta linea de código si la data no estubiera codificada en utf-8
    json.dump(wholeDict, f,ensure_ascii=False, indent=2)
    print("Archivo json creado")

#print(flagGT)
print('---------------------------------------Abajo el JSON------------------------------------------------')
print(json_data.decode())
#print("Cantidad de articulos con la palabra Guatemala: "+ str(contadorGT))
#print("Articulos identificados que hacen mencion a Banca en Línea: "+ str(contadorBel))
#print("Articulos identificados que hacen mencion a Banca Móvil: "+ str(contadorBM))
#print("Cantidad de articulos con la palabra Costa Rica: "+CRIflag)