
        ##Programación Orientada a Objetos##

class Usuario:
    def __init__(self, nombreUsuario, password):
        self.userName = nombreUsuario
        self.password = password
    
    def changePassword(self):
        test = input("Ingrese su contraseña actual: ")
        if test == self.password:
            newPassword = input("Ingrese la contraseña nueva: ")
            newPassword2 = input("Confirme la contraseña nueva: ")
            if newPassword == newPassword2:
                self.password = newPassword
                print("Se ha cambiado la contraseña.")
            else:
                print("Las contraseñas no coinciden")
        else:
            print("Contraseña incorrecta")
    
    def setUsername(self):
        newName = input("Ingrese su nuevo nombre de usuario: ")
        if input("¿Seguro que quieres cambiar tu nombre de usuario? s/n: ") == 's':
            self.userName = newName
            print("Se ha cambiado su nombre de usuario.")
        else:
            print("Se ha cancelado la operación.")
    
    def setPassword(self):
        newPassword = input("Ingrese su contraseña nueva: ")
        newPassword2 = input("Confirme su contraseña: ")
        if newPassword == newPassword2:
            self.password = password
            print("Se ha actualizado su contraseña.")
        else:
            print("Las contraseñas no coinciden.")
        


class UsuarioPremium(Usuario):

    def __init__(self,nombreUsuario,password,suscripcion):
        self.userName = nombreUsuario
        self.password = password
        self.suscription = suscripcion
    
    def getSus(self):
        print("Tu suscripción es de: ",self.suscription," meses")


user = Usuario("OscarAyala", "3312")
userPremium = UsuarioPremium("OscarAyala2", "12345","8")

user.changePassword()
userPremium.changePassword() ##userPremium puede acceder al método changePassword() ya que es una clase hija de la clase Usuario, por lo que hereda todos sus metodos y atributos

userPremium.getSus()

##user.getSus() Este instrucción marcará un error ya que user es una instancia de Usuario, mientras que el método getSus() es de la clase UsuarioPremiun
