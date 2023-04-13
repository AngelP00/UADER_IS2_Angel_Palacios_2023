# Creamos nuestra propia excepción heredando
# de la clase Exception
class ExcepcionUserText(Exception):
    def __init__(self, text_info):
        self.text_info = text_info