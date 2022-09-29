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

gestiones = ["cobertura de tarjeta de débito","cobertura de tarjeta de crédito","actualizar sus datos",
"cancelación de cuenta","reactivación de una cuenta bancaria","administrar correo electrónico para recibir estados de cuenta",
"administrar mensajes bac","administrar tarjetas adicionales (administrador virtual)","bloquear temporalmente una tarjeta de crédito",
"Cambiar el tipo o marca de la tarjeta tc","cambiar la fecha de pago","cancelar anticipadamente un extrafinaciamiento",
"disminuir el límite de crédito","eliminar el retenido de compra de la tarjeta de crédito","pagar la tarjeta de crédito con débito a cuenta",
"referir a un amigo","solicitar conversión de moneda del saldo de crédito","solicitar el traslado o devolución de saldo a favor de su tarjeta de crédito",
"solicitar reversión de cargos de tarjetas de crédito","solicitar tarjeta de crédito adicional","administrar mensajes bac",
"bloquear temporalmente una cuenta bancaria","solicitar emisión cheque de gerencia","solicitar enlace de cuentas propias para realizar transferencias",
"solicitar cuenta bancaria","solicitar una referencia bancaria","consultar acumulación de puntos credomatic",
"solicitar el pin del cajero automático","solicitar la reposición de tarjeta deteriorada","solicitar reclamo atm 5b/bi",
"solicitar tarjeta de débito","solicitar el abono o cancelación de préstamo","solicitar proyección de pago de préstamos personales",
"solicitar activación de asistencia funeraria","solicitar activación de cobertura sos","solicitar activación de seguro atraco atm",
"abrir nuevo objetivo","enviar una queja o sugerencia","solicitar la deshabilitación de adelanto de salario (ads)",
"solicitar servicio tpago","solicitar usuario para el portal de la superintendencia de bancos",
"actualización de datos comercios afiliados","cambio de nombre en tarjeta","solicitud de finiquito",
"solicitar otra tarjeta de crédito","solicitar Cuenta objetivos","solicitar préstamo de auto",
"solicitar préstamo personal","solicitar préstamo hipotecario","solicitar préstamo planilla",
"aumenta el límite de crédito","cancelar pago programado","convierte tus compras a plazos",
"redimir cash o puntos bac credomatic","solicitud de extrafinanciamiento en su tarjeta de crédito ",
"solicitud compass","solicitar afiliación nueva de un comercio","solicitud aprobación de plantillas para transferencias internacionales",
"desbloqueo temporal","administrar mensajes bac","solicitar el traslado o devolución de saldo a favor de su tarjeta de crédito / devolución de saldo a favor",
"solicitar reversión de cargos de tarjetas de crédito /mantenimiento priority pass",
"solicitar reversión de cargos de tarjetas de crédito / reversión cargo seguro","solicitar el abono o cancelación de préstamo",
"solicitud de tarjeta empresarial","solicitud de tarjeta adicional empresarial"
]
#para obtener informacion de temas con paginas
#urlPagina = 'https://ayuda.baccredomatic.com/es/comercios-afiliados' 
wholeDict = {}
href2 = list()
testDict ={}
contadorGT = 0
contadorBel = 0
contadorBM = 0
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
    #
    flagGT = list() 
    flagCRI = list() 
    flagSLV = list() 
    flagHND = list() 
    flagNIC = list() 
    flagPAN = list() 

    flagBel = list()
    flagBM = list()
    #Guatemala
    #Costa Rica
    #El Salvador
    #Honduras   
    #Nicaragua
    #Panamá 
#-------------------------------------------------------------------------------------------------------------
    cont = 0
    #testDict ={}
    #Realizar scrapping dentro del ciclo para analizar si existe la palabra Guatemala dentro del texto
    #El campo "GT" sera True si el articulo contiene la palabra, de lo contrario sera False.
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
        articleLastUpdate = list()   
        for hiperlink in hiperlinkHtmlExtended:
            responseArticle = requests.get(hiperlink)
            htmlArticle = BeautifulSoup(responseArticle.text, 'html.parser')
            articleLastUpdate.append(htmlArticle.find('div', {"class" :"field field--name-node-changed-date field--type-ds field--label-inline"}).find('div',{"class" :"field--item"}))
            soup = htmlArticle.find('div', {"class" :"row bs-1col node node--type-book node--view-mode-full"})
            #soup.lower()
            #------Banca Móvil---------
            if(str(soup).lower().find(gestion)>=0):
                print(str(soup).find(gestion))
                testDict[gestion].setdefault("hipervinculo"+cont,hiperlinkHtmlExtended[cont])
                #flagBM.append(True)
                #contadorBM+=1
            elif(str(soup).find(gestion)<0):
                print(str(soup).find(gestion))
                #flagBM.append(False)
        #Ultima linea de la comprobacion
        cont+=1

    
        

    # Crear una lista de los ultimos updates de cada articulo
    lastUpdates =list()
    for lastUpdate in articleLastUpdate:
        lastUpdates.append(lastUpdate.text.strip())
    #----------------------------------------------------

    #-----------------------------------------------------------------------------------


    
    


    json_data = json.dumps(testDict,ensure_ascii=False,indent=3).encode('utf8')
#print(flagGT)
print('---------------------------------------Abajo el JSON------------------------------------------------')

print(json_data.decode())

#print("Cantidad de articulos con la palabra Guatemala: "+ str(contadorGT))

#print("Articulos identificados que hacen mencion a Banca en Línea: "+ str(contadorBel))
#print("Articulos identificados que hacen mencion a Banca Móvil: "+ str(contadorBM))
#print("Cantidad de articulos con la palabra Costa Rica: "+CRIflag)