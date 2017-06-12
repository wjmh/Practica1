# -*- coding: utf-8 -*-
from xml.dom import minidom
from Matriz import matriz
matriz = matriz()
from Pila import pila
pila = pila(500)
class Cola():

    def __init__(self):
        self.cola = []
        self.tamano = 0

    def Vacio(self):
        return len(self.cola) == 0

    def Encolar(self, operacion):
        self.cola += [operacion]
        self.tamano += 1

    def Desencolar(self):
        if (self.Vacio()):
            print ("La Cola está Vacía")

        else:
            self.cola = [self.cola[i] for i in range(1, self.tamano)]
            self.tamano -= 1

    def RecorrerCola(self):
        n = self.tamano - 1
        print (".....Operaciones en Cola.....")
        while (n > -1):
            print ("[%d]=>%s" % (n, self.cola[n]))
            n -= 1

    def MostrarPrimerDato(self):
        if (self.Vacio):
            print("Cola Vacía")

        else:
            print("Primera Operacion: %d" % (self.cola[0]))


    def LeerArchivo(self):
        print ("...........Ingrese la ruta con Doble Comillas...........")
        ruta = input("ingrese la ruta del archivo")
        archivo = open(ruta, "r")
        leer = archivo.read()
        print(leer)
        archivo.close()
        print("\n")
        path = leer
        doc = minidom.parseString(path)
        #Dimension X
        print("No.Filas: ")
        FilaX = doc.getElementsByTagName("x")
        for i in FilaX:
            fila = i.firstChild.nodeValue
            print(fila)
            fila = int(fila)
        #Dimension Y
        print("No. Columnas")
        ColumnaY = doc.getElementsByTagName("y")
        for i in ColumnaY:
            columna = i.firstChild.nodeValue
            print(columna)
            columna = int(columna)
        print("La dimension de la Matriz es de: ", fila, "X", columna)
        print("\n")
        operaciones = doc.getElementsByTagName("operacion")
        for i in operaciones:
            operacion = i.firstChild.nodeValue
            self.Encolar(operacion)
        pila.PPush(operacion)
        print("...........Archivo leído Correctamente...........")