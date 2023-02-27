#Web scrapping para la categoria de Banca En Línea Y Banca Móvil
 
 #Ruta raiz

# Importar módulos
import requests
import json
import csv
from bs4 import BeautifulSoup
root = 'https://ayuda.baccredomatic.com/'
urlCategoria = 'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?subcategory='
# Dirección dentro del centro de ayuda
urlsTemas = ['COMPASS','Pagos%20de%20servicios','Problemas%20en%20Banca%20en%20Línea%20y%20Banca%20Móvil','Solicitudes%20y%20gestiones%20en%20línea','Transferencias','Usuario%20y%20contraseña']

#Numero de pagina donde se hará el scrapping, se utilizara mas adelante para realizar un loop
page = 0
#Diccionario con la data para generar el indice en formato JSON
centroDeAyuda = {}

# Ejecutar GET-Request
response = requests.get(urlCategoria+str(urlsTemas[2]))

# Analizar sintácticamente el archivo HTML de BeautifulSoup del texto fuente
html = BeautifulSoup(response.text, 'html.parser')

# Extraer el titulo de los articulos + la descripcion + el hipervinculo
articleTitlesHtml = html.find_all('h3', class_="field-content")
descriptionTitlesHtml = html.find_all('div', class_="field field--name-field-summary field--type-string-long field--label-hidden field--item")

# Crear una lista de los titulos de los articulos
articleTitles = list()
for articleTitle in articleTitlesHtml: 
    #print(articleTitle.text.strip())   
    articleTitles.append(articleTitle.text.strip())
print('-----------------------------')
print(articleTitles)
print('-----------------------------')
# Crear una lista de los hipervinculos de cada articulo
hiperlinkHtml = list()
for article in articleTitlesHtml:
    hiperlinkHtml.append(article.find('a')['href'])

# Crear una lista de las descripciones de los articulos
descriptionTitles = list()
for descriptionTitle in descriptionTitlesHtml:
    descriptionTitles.append(descriptionTitle.text.strip()) 

#Testing
#print(articleTitles,descriptionTitles)
#Codigo para generar archivo JSON.

centroDeAyuda = {'Centro de ayuda':{'Banca en linea y banca movil':articleTitles}}
json_data = json.dumps(centroDeAyuda,indent=3).encode('utf8')
print(json_data)