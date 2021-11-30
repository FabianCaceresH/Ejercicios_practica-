# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json


def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    persona = {"nombre":"rodolfo el reno"
             ,"apellido":"el reno",
              "dni":7,
              "vestimenta":[{"prenda:":"zapatilla","cantidad":4},
                            {"prenda:":"remeras","cantidad":12}]





    }
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}

    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina

    # Observe el archivo y verifique que se almaceno lo deseado
    with open('persona.json','w') as jsonfile:
        data = [persona]
        json.dump(data,jsonfile,indent=4)
def deserializar():
    print("Funcion que lee un archivo JSON")
    persona2 = {"nombre":"santa claus"
             ,"apellido":"claus",
              "dni":6,
              "vestimenta":[{"prenda:":"zapatilla","cantidad":4},
                            {"prenda:":"remeras","cantidad":12}]}


    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior
    with open('persona.json','r') as jsonfile:
        current_data=json.load(jsonfile)
        current_data.append(persona2)
    with open('persona.json','w') as jsonfile:
        json.dump(current_data,jsonfile,indent = 4)
    with open('persona.json','r') as jsonfile:
        json_data = json.load(jsonfile)
        print("muesta del contenido del archivo perona-json")
if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    serializar()
    deserializar()
    print("terminamos")