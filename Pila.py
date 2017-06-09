# -*- coding: utf-8 -*-
class pila():

    def __init__(self, size):
        self.lista = []
        self.size = size
        self.top = 0

    def PilaVacia(self):
        if (self.top == 0):
            return True
        else :
            return False

    def Push(self, operacion):
        if(self.top < self.size):
            self.lista += [operacion]
            self.top += 1
        else:
            print("La pila está llena")

    def Pop(self):
        if(self.PilaVacia()):
            print("La pila está Vacía")
        else:
            self.top -= 1
            self.lista = [self.lista[x] for x in range(self.top)]

    def MostrarPila(self):
        i = self.top -1
        while(i > -1):
            print("[%d]  =>  %d" % (i, self.lista[i]))
            i -= 1

    def SizePila(self):
        return self.top

    def Peek(self):
        return self.lista[-1]