# -*- coding: utf-8 -*-
class nodo:
    def __init__(self, user, password, cola):
        self.user = user
        self.password = password
        self.cola = cola
        self.siguiente = None
        self.anterior = None

