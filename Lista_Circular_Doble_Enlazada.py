# -*- coding: utf-8 -*-
from Nodo import nodo

class ListaCircular:

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacio(self):
        if(self.primero is None):
            return True
        else:
            return False

    def AgregarInicio(self, user, password):
        if (self.Vacio()):
            self.primero = self.ultimo = nodo()
        else:
            aux = nodo(user, password)
            aux.siguiente = self.primero
            self.primero.anterior = aux
            self.primero = aux
        self.__UnirNodos()



    def AgregarFinal(self, user, password):
        if(self.Vacio()):
            self.primero = self.ultimo = nodo(user, password)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo(user, password)
            self.ultimo.anterior = aux
        self.__UnirNodos()

    def __UnirNodos(self):
        if(self.primero != None):
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def recorrerInicia_a_Fin(self):
        aux = self.primero
        while (aux):
            print (aux.user)
            aux = aux.siguiente
            if(aux == self.primero):
                break



    def recorrerFin_a_Inicio(self):
        aux = self.ultimo
        while (aux):
            print (aux. user)
            aux = aux.anterior
            if(aux == self.ultimo):
                break

    def EliminarInicio(self):
        if (self.Vacio()):
            print("La lista está vacía.")

        elif (self.primero == self.ultimo):
            self.primero = self.ultimo = None

        else:
            self.primero = self.primero.siguiente

        self.__UnirNodos()



    def EliminarUltimo(self):
        if (self.Vacio()):
            print("La lista está vacía.")

        elif (self.primero == self.ultimo):
            self.primero = self.ultimo = None

        else:
            self.ultimo = self.ultimo.anterior

        self.__UnirNodos()


    def Buscar(self, user, password):
        aux = self.primero
        while(aux):
            if (aux.user == user and aux.password == password):
                return True

            else:
                aux = aux.siguiente
                if(aux == self.primero):
                    return False



