#clases
class Usuario :
    def __init__(self, nombre,apellido,email,password=1234):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
    
    def getNombre(self):
        return self.nombre
    
    
    def getApellido(self):
        return self.apellido

    def getEmail(self):
        return self.email

    def getPassword(self):
        return self.password




user = Usuario("Jose Ali","Mendoza","191287@ids.upchiapas.edu.mx")
nombre = user.getNombre()
apellido = user.getApellido()
email = user.getEmail()
password = user.getPassword()
print(nombre," ",apellido," ",email," ",password)


