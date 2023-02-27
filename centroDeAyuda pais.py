#Web scrapping para la categoria de Banca En Línea Y Banca Móvil

# Importar módulos
from ast import For, If
import urllib.request as urllib2
import requests
import json
from bs4 import BeautifulSoup

from searchData import wholePages
#Ruta raiz
root = 'https://ayuda.baccredomatic.com/'

#Ruta de la categoria, se agrega el numero correlativo de las catrogia
urlCategoria = 'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?subcategory='

# Dirección dentro del centro de ayuda
urlsTemas = ['COMPASS','Pagos%20de%20servicios','Problemas%20en%20Banca%20en%20Línea%20y%20Banca%20Móvil','Solicitudes%20y%20gestiones%20en%20línea','Transferencias','Usuario%20y%20contraseña']

#Numero de pagina donde se hará el scrapping, se utilizara mas adelante para realizar un loop
page = 0
#Diccionario con la data para generar el indice en formato JSON
centroDeAyuda = {}

# Ejecutar GET-Request
#response = requests.get(urlCategoria+str(urlsTemas[1]))


#para obtener informacion de temas con paginas
#urlPagina = 'https://ayuda.baccredomatic.com/es/comercios-afiliados' 
wholeDict = {}
href2 = list()
testDict ={}
contadorGT = 0
contadorCRI = 0 
contadorSLV = 0 
contadorHND = 0 
contadorNIC = 0 
contadorPAN = 0

def getCountries():
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

        articleLastUpdate = list()   
        for hiperlink in hiperlinkHtmlExtended:
            responseArticle = requests.get(hiperlink)
            htmlArticle = BeautifulSoup(responseArticle.text, 'html.parser')
            articleLastUpdate.append(htmlArticle.find('div', {"class" :"field field--name-node-changed-date field--type-ds field--label-inline"}).find('div',{"class" :"field--item"}))
            soup = htmlArticle.find('div', {"class" :"row bs-1col node node--type-book node--view-mode-full"}) 
            #------Guatemala---------
            if(str(soup).find("Guatemala")>=0):
                flagGT.append(True)
                contadorGT+=1
            elif(str(soup).find("Guatemala")<0):
                flagGT.append(False) 
            #------Costa Rica---------
            if(str(soup).find("Costa Rica")>=0):
                flagCRI.append(True)
                contadorCRI+=1
            elif(str(soup).find("Costa Rica")<0):
                flagCRI.append(False) 
            #------El Salvador---------
            if(str(soup).find("El Salvador")>=0):
                flagSLV.append(True)
                contadorSLV+=1
            elif(str(soup).find("El Salvador")<0):
                flagSLV.append(False) 
            #------Honduras---------
            if(str(soup).find("Honduras")>=0):
                flagHND.append(True)
                contadorHND+=1
            elif(str(soup).find("Honduras")<0):
                flagHND.append(False)
            #------Nicaragua---------
            if(str(soup).find("Nicaragua")>=0):
                flagNIC.append(True)
                contadorNIC+=1
            elif(str(soup).find("Nicaragua")<0):
                flagNIC.append(False) 
            #------Panamá---------
            if(str(soup).find("Panamá")>=0):
                flagPAN.append(True)
                contadorPAN+=1
            elif(str(soup).find("Panamá")<0):
                flagPAN.append(False) 
            

        # Crear una lista de los ultimos updates de cada articulo
        lastUpdates =list()
        for lastUpdate in articleLastUpdate:
            lastUpdates.append(lastUpdate.text.strip())
        #----------------------------------------------------

        #-----------------------------------------------------------------------------------


        cont = 0
        #testDict ={}
        #Realizar scrapping dentro del ciclo para analizar si existe la palabra Guatemala dentro del texto
        #El campo "GT" sera True si el articulo contiene la palabra, de lo contrario sera False.
        for title in articleTitles:

            testDict.setdefault(title,{})
            testDict[title].setdefault("hipervinculo",hiperlinkHtmlExtended[cont])
            testDict[title].setdefault("descripcion",descriptionTitles[cont])
            testDict[title].setdefault("Última actualización",lastUpdates[cont])
            testDict[title].setdefault("GT",flagGT[cont])
            testDict[title].setdefault("CRI",flagCRI[cont])
            testDict[title].setdefault("SLV",flagSLV[cont])
            testDict[title].setdefault("HND",flagHND[cont])
            testDict[title].setdefault("NIC",flagNIC[cont])
            testDict[title].setdefault("PAN",flagPAN[cont])
            cont+=1
        


        json_data = json.dumps(testDict,ensure_ascii=False,indent=3).encode('utf8')
        print(json_data.decode())
#print(flagGT)


dictRes={
    "Cantidad de articulos con mencion a Guatemala: ": str(contadorGT),
    "Cantidad de articulos con mencion a Costa Rica: ": str(contadorCRI),
    "Cantidad de articulos con mencion a El Salvador: ": str(contadorSLV),
    "Cantidad de articulos con mencion a Honduras: ": str(contadorHND),
    "Cantidad de articulos con mencion a Nicaragua: ": str(contadorNIC),
    "Cantidad de articulos con mencion a Panama: ": str(contadorPAN)
}
return()
#print("Cantidad de articulos con la palabra Costa Rica: "+CRIflag)