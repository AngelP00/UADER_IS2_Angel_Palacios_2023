"""
Este es un ejemplo de docstring para un módulo en Python.

Autor: Angel Palacios
Fecha de creación: jue. 13/4(abr.)/2023
"""

import sys
import openai

# developer
#from ExceptionsDeveloper import *
from ExceptionsDeveloper import ExcepcionUserText
# ……. [ mas Código de inicialización aqui ] …………
openai.api_key = "-------api_key-------"
TOP_P = 1
FREQ_PENALTY = 0
PRES_PENALTY = 0
STOP = None
MAX_TOKENS = 1024
TEMPERATURE = 0.75
NMAX = 1
MODEL_ENGINE = "text-davinci-003"

# '''
# …..[otra lógica necesaria – el texto del prompt debe colocarse en userText]…..
option = ""
#si el usuario ingresa --convers el programa se configura para el modo conversacional
if len(sys.argv)>1 and sys.argv[1] == "--convers":
    option="--convers"
    print('modo conversacion activado')
    STOP=["\n","You:","chatGPT:"]

buffer = ""
seguir = True #variable para controlar el bucle
while seguir:
    try:
        #input para que el usuario ingresa su consulta
        userText = input("Realizar una consulta(para finalizar la ejecucion apriete enter):")
        if userText is None:#si la variable no esta definida
            seguir = False#si el usuario no ingresa ingresa texto la ejecucion del bucle se para
            raise ExcepcionUserText("""exception: la variable userText debe ser diferente a None
                                    y no debe estar vacia""")
        if userText== '':#si el usuario no ingresa texto
            seguir = False#si el usuario no ingresa ingresa texto la ejecucion del bucle se para
            break
        print('You: '+userText)
        buffer+='\nYou: '+userText+".\nchatGPT:"#se guarda la consulta y la respuesta en el buffer
        if option != "--convers":
            #es es igual a "--convers" entonces el programa se configura para el modo consulta
            buffer = userText

        try:# Set up the model and prompt
            completion = openai.Completion.create(
                engine=MODEL_ENGINE,
                prompt=buffer,
                max_tokens=MAX_TOKENS,
                n=NMAX,
                top_p=TOP_P,
                frequency_penalty=FREQ_PENALTY,
                presence_penalty=PRES_PENALTY,
                temperature=TEMPERATURE,
                stop=STOP)#se envia el promt a chatGPT
        except NameError as ex:#ocurrio un problema con chatGPT
            #print(type(ex))
            print("exception3: ocurrio un problema en el envio del promt a openai")
            break
        buffer += completion.choices[0].text.strip()#se agrega al buffer la respuesta de chatGPT
        print('chatGPT:'+completion.choices[0].text)#muestra el resultado de la consulta
    except ExcepcionUserText as ex:
        print(ex.args[0])#muestra el resultado de la excepcion
