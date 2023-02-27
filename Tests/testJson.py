import json

#centroDeAyuda = {'Centro de ayuda':{'Banca en linea y banca movil':{'Compass':{}}}}

#compass=centroDeAyuda['Centro de ayuda']['Banca en linea y banca movil']
hiperLinks = ['https://ayuda.baccredomatic.com//es/banca_en_linea_y_banca_movil/compass/solicitar-compass-de-bac-credomatic', 'https://ayuda.baccredomatic.com//es/banca_en_linea_y_banca_movil/compass/ingresar-compass-e-instalar-el-dispositivo']
descriptionArticles = ['Conozca cómo puede activar el servicio Compass de manera digital. Con Compass, puede pagar el parqueo o peajes de manera automática, rápida y sin filas.', 'Conozca cómo instalar el sticker o dispositivo Compass que ha recibido. También puede ingresar a Compass X app para pagar el parqueo o peaje de manera automática.']
titlesAticles = ['Solicitar Compass de BAC Credomatic', 'Ingresar a Compass e instalar el dispositivo']
#print(compass)
testDict = {}
articulos = list()
# "Solicitar Compass de BAC Credomatic":
#                         {
#                           "hipervinculo":"www.google.com",
#                           "descripcion":"Este es un articulo"
#                         }
#print(hiperLinkPlusArticle)
#print(titlesAticles)
#centroDeAyuda

cont = 0
for title in titlesAticles:
    testDict.setdefault(title,{})
    testDict[title].setdefault("hipervinculo",hiperLinks[cont])
    testDict[title].setdefault("descripcion",descriptionArticles[cont])
    cont+=1
    print(title)

json_data = json.dumps(testDict,ensure_ascii=False,indent=3).encode('utf8')
print(json_data.decode())   


#ejemplo de diccionarios
# dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
# valor = dic.setdefault(‘e’,5)
# dic → {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4 , ‘e’ : 5}