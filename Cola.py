# -*- coding: utf-8 -*-
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
        while (n > -1):
            print ("[%d]  =>  %s" % (n, self.cola[n]))
            n -= 1

    def MostrarPrimerDato(self):
        if (self.Vacio):
            print("Cola Vacía")

        else:
            print("Primera Operacion: %d" % (self.cola[0]))


    def LeerArchivo(self):
        f = open('archivo.txt', 'r')
        #data = f.readlines()
        f.readline()
        f.readline()
        posX = f.readline()
        print filter(self.PosX, posX)
        posY = f.readline()
        print posX
        print posY
        #contador = 0

        #for renglon in data:
            #for palabra in renglon.splitlines():
                #contador += 1
                #print '%d) %s' % (contador, palabra)
                #self.Encolar(palabra)
        f.close()

    def PosX(self, x):

        return x == "%d"