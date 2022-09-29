#Web scrapping para la categoria de Banca En Línea Y Banca Móvil

# Importar módulos
from ast import For, If
import urllib.request as urllib2
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



wholePages = [#Actualizado 29/09/2022
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=2','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=3',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=4','https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=5',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=6', 'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=7',
    'https://ayuda.baccredomatic.com/es/banca-en-linea-y-banca-movil?field_subcategory=All&page=8','https://ayuda.baccredomatic.com/es/tarjetas-de-credito','https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=2','https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=3',
    'https://ayuda.baccredomatic.com/es/tarjetas-de-credito?field_subcategory=All&page=4','https://ayuda.baccredomatic.com/es/cuentas-bancarias-y-tarjetas-de-debito','https://ayuda.baccredomatic.com/es/cuentas-bancarias-y-tarjetas-de-debito?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/codigo-bac','https://ayuda.baccredomatic.com/es/codigo-bac?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/canales-de-atencion','https://ayuda.baccredomatic.com/es/canales-de-atencion?field_subcategory=All&page=1',
    'https://ayuda.baccredomatic.com/es/prestamos',
    'https://ayuda.baccredomatic.com/es/seguros-y-coberturas',
    'https://ayuda.baccredomatic.com/es/comercios-afiliados','https://ayuda.baccredomatic.com/es/comercios-afiliados?field_subcategory=All&page=1'
]
#para obtener informacion de temas con paginas
#urlPagina = 'https://ayuda.baccredomatic.com/es/comercios-afiliados' 
wholeDict = {}
href2 = list()
testDict ={}
contadorGT = 0
contadorBel = 0
contadorBM = 0

for x in range(10):
    print(x)
    urlPagina = page
    response = requests.get("https://g.bac.gt/requestTest")
    print(response)

print("Ojala esta mierda no nos afecte")
