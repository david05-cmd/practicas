class Validacion():
    def __init__(self):
        pass

    def validarNombre(self,n):
        if n != "":
            if (ord(n) >= 65 and ord(n) <= 90) and (ord(n) >= 97 and ord(n) <= 122):
                return False
            else:
                return False
        else:
            return "Cajas vacias"