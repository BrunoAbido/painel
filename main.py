from Fila import Fila


class Sistema:

    def getSenha(self):
        self.senhas.enqueue(self.counter)
        self.counter += 1
        return 


    def __init__(self):
        self.counter = 0
        self.password = Fila()
        self.old_passwords = Fila()


    def callNext(self):
        if(self.old_passwords.__len__() == 5):
            self.old_passwords.dequeue()
        return self.old_passwords.enqueue(self.senhas.dequeue())
    
    def show_password(self):
        print("Últimas senhas chamadas: ", self.old_passwords.__str__())
    
    
sistema = Sistema()

sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()
sistema.getSenha()

sistema.callNext()
sistema.callNext()
sistema.callNext()
sistema.callNext()
sistema.callNext()
sistema.callNext()
sistema.callNext()
sistema.callNext()
sistema.callNext()

sistema.mostrarSenhas()
