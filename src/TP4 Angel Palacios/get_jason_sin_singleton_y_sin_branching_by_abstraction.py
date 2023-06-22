# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55
import json, sys

if(sys.argv[1] == "-h"):
    print("Help:")
    
    
    print(
    '''
Extractor de token para acceso API Servicios Banco XXX (version 1.0)

Este programa permite extraer la clave de acceso API para utilizar los servicios del 
Banco XXX.

El programa operara como un microservicio invocado mediante:

        {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json

ej.
        ./getJason.pyc ./sitedata.json

El token podra recuperarse mediante el standard output de ejecucion en el formato

       {1.0}XXXX-XXXX-XXXX-XXXX

Para obtener un mensaje de ayuda detallado ejecutar

       ./getJason.pyc -h
    ''')
    

    print("")

    sys.exit(2)

if(len(sys.argv) != 3):
    print("Debe ingresar dos argumentos: 1) El archivo .json y 2) El nombre del toquen o -h para obtener ayuda")
    sys.exit(1)

jsonfile = sys.argv[1]
jsonkey = sys.argv[2]


try:
    with open(jsonfile, 'r') as (myfile):
        data = myfile.read()
except:
    print("No se encontro el archivo .json en la ruta indicada")
    sys.exit(3)

obj = json.loads(data)
try:
    print(str(obj[jsonkey]))
except:
    print("token no encontrado")
# okay decompiling getJason.pyc
