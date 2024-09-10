# las clases, modulos, las funciones etc tienen que estar abiertas para la extencion , pero cerrada para la modificacion, osea poder agregar nuevas funcionalidades sin cambiar el codigo fuentes de las entidades

class Notificador:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def notificar(self):
        raise NotImplementedError #$ asegurar que una clase base defina ciertos métodos que son esenciales, pero cuya implementación específica depende de las subclases
    

class NotificadorEmail(Notificador):
    def __init__(self, usuario, mensaje):
        super().__init__(usuario, mensaje)

    def notificar(self):
        print(f"enviando mensaje a {self.usuario.email}")


class NotificadorSMS(Notificador):
    def __init__(self, usuario, mensaje):
        super().__init__(usuario, mensaje)

    def notificar(self):
        print(f"enviando SMS a {self.usuario.sms}")

class NotificadorWhatsApp(Notificador):
    def __init__(self, usuario, mensaje):
        super().__init__(usuario, mensaje)

    def notificar(self):
        print(f"enviando WhatsApp a {self.usuario.WhatsApp}")