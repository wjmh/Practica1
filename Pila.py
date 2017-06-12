# -*- coding: utf-8 -*-
class pila():

    def __init__(self, size):
        self.EPila = []
        self.PPila = []
        self.size = size
        self.top = 0


    def PilaVacia(self):
        if (self.top == 0):
            return True
        else:
            return False

    def EPush(self, operacion):
        operadores = "+-*"
        while (self.PilaVacia()):
            if (self.EPeek() in operadores):
                self.PPush(self.OperarPila(self.EPop(), self.PPop(), self.PPop()))
            self.top += 1
        else:
            self.PPush(self.EPop())

    def PPush(self, operacion):
        while (self.PilaVacia()):
            self.PPila += [operacion]
            self.top += 1
        else:
            print("La pila está llena")



    def EPop(self):
        if(self.PilaVacia()):
            print("La pila está Vacía")
        else:
            self.top -= 1
            self.E = [self.EPila[x] for x in range(self.top)]

    def PPop(self):
        if(self.PilaVacia()):
            print("La pila está Vacía")
        else:
            self.top -= 1
            self.E = [self.PPila[x] for x in range(self.top)]

    def MostrarPila(self):
        i = self.top -1
        while(i > -1):
            print("[%d]  =>  %s" % (i, self.EPila[i]))
            i -= 1

    def SizePila(self):
        return self.top

    def EPeek(self):
        print self.EPila[-1]
    def PPeek(self):
        print self.PPila[-1]

    def OperarPila(self, operador, x, y):
        x = int(x)
        y = int(y)
        if (operador == '+'):
            return (x + y)
        if (operador == '-'):
            return (x - y)
        if (operador == '*'):
            return (x * y)
