# -*- coding: utf-8 -*-
from NodoMatriz import nodoMatriz
class matriz():

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def Vacio(self):
        return self.primero == None

    def Agregar(self, posx, posy):
        if (self.Vacio()):
            self.primero = self.ultimo = nodoMatriz()
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodoMatriz()

    def Recorrer(self):
        aux = self.primero
        while (aux != None):
            print (aux.posx)
            print (aux.posy)
            aux = aux.siguiente





















        #self.matriz = []
        #self.aux = []
        #self.x = 0
        #self.y = 0
    #def LlenarMatriz(self, x, y):
        #for i in range(x):
            #aux = []
            #for j in range(y):
                #elemento = raw_input("Ingrese valor en la posicion [%d][%d]:"%(i, j))
                #aux += [elemento]
                #j += 1
            #i += 1
            #self.matriz += [aux]
        #print ("\n")
        #print("Datos Ingresados")

    #def MostrarMatriz(self):
        #for mostrar in self.matriz:
            #print mostrar

    #def MatrizTranspuesta(self):
        #matrizTrans = []
        #matrizTrans = self.matriz
        #fila = self.x
        #columna = self.y
        #for mostrar in matrizTrans:
            #for z in mostrar:
                #for j in range(columna):
                    #temp = []
                    #for i in range(fila):
                        #temp += temp[i][j]
                        #matrizTrans[j][i] = temp[i][j]
                        #print(matrizTrans)
                    #print(matrizTrans)
                #print (matrizTrans)
        #for i in matrizTrans:
            #print (i)