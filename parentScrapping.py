from CentroAyudaGestionesArray import CAGestion
from centroDeAyudaPais import getCountries
import json
import os

menu = {1:"Mentioned gestions bel/bm", 2:"Mentioned countries in articles",3:"Href inside articles",4:"BeL BM mentions on articles"}
print("Welcome to the Centro de Ayuda's web scrapping :D")
for task in menu:
    print(str(task)+": "+menu[task])
index = input("Select the index of the data you want to get and press enter \n")

match index:
    case "1":
        res = CAGestion()
        fileName = "gestiones.json"
    case "2":
        res = getCountries()
        fileName = "countries.json"
    case "3":
        print("OPA's")
    case "4":
        print("BeL BM")
        

try:
    #--------------------------------Json file
    #print(type(res[0]))#Es el diccionario para convertir a archivo 
    with open(os.path.join('C:/Users/jorge.depazr/Documents/Dev/Web Scrapping/results',fileName), 'w', encoding="utf-8") as f:
        #str(wholeDict).encode('utf-8')  #<---Se agregaria esta linea de código si la data no estubiera codificada en utf-8
        json.dump(res[0], f,ensure_ascii=False, indent=2)
    print("Json file created")
    #--------------------------------Json string
    print("Json string")
    print(res[1].decode())
except:
    print("Something else went wrong")
  



    