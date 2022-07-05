#Web scrapping para la categoria de Banca En Línea Y Banca Móvil
# git config --global user.email "you@example.com"
# git config --global user.name "Your Name"
# Importar módulos
import requests
import json
from bs4 import BeautifulSoup

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
urlPagina = 'https://ayuda.baccredomatic.com/es/comercios-afiliados' 
response = requests.get(urlPagina)

# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')

# Extraer el titulo de los articulos + la descripcion + el hipervinculo
articleTitlesHtml = html.find_all('h3', class_="field-content")
descriptionTitlesHtml = html.find_all('div', class_="field field--name-field-summary field--type-string-long field--label-hidden field--item")
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
print(hiperlinkHtmlExtended)
print('--------------------------------------------------------')
# Crear una lista de las descripciones de los articulos
descriptionTitles = list()
for descriptionTitle in descriptionTitlesHtml:
    descriptionTitles.append(descriptionTitle.text.strip()) 
print(descriptionTitles)
# Para hacer el test: combinar y mostrar las entradas de ambas listas
aList=list()
for t in zip(descriptionTitles,hiperlinkHtmlExtended):
    #print(list(t))
    #print(len(list(t)))
    aList.append(list(t))

#Se crea una matriz con los datos, el primer indice es para visualizar el articulo el numero varia segun el tema
#el segundo indice puede ser 0 ó 1 para visualizar la descripcion o el hipervinculo
#print(aList)
#print(len(aList))
#print('-----------------------------------')
#print(aList[0])
#print(articleTitles)
#Codigo para indexar cada elemento de la lista en un nuevo objeto
#for article in articleTitles:

#Codigo para generar archivo JSON.
centroDeAyuda = {'Centro de ayuda':{'Banca en linea y banca movil':articleTitles}}

json_data = json.dumps(centroDeAyuda,ensure_ascii=False,indent=3).encode('utf8')
print(json_data.decode())

cont = 0
testDict ={}
#Realizar scrapping dentro del ciclo para analizar si existe la palabra Guatemala dentro del texto
#El campo "GT" sera True si el articulo contiene la palabra, de lo contrario sera False.
for title in articleTitles:
    testDict.setdefault(title,{})
    testDict[title].setdefault("hipervinculo",hiperlinkHtmlExtended[cont])
    testDict[title].setdefault("descripcion",descriptionTitles[cont])
    testDict[title].setdefault("GT",False)
    cont+=1
    print(title)

json_data = json.dumps(testDict,ensure_ascii=False,indent=3).encode('utf8')
print('-----------------------------------------------------------------------')
print(json_data.decode()) 