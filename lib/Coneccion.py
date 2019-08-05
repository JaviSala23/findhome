# -*- coding: utf-8 -*-
import psycopg2
import sys
import wx

class Coneccion:
        def __init__(self,host,bd,user,passw):
		self.host=host
		self.bd=bd
		self.user=user
		self.passw=passw
	def conectar(self):
                try:
                        con = psycopg2.connect(host=self.host,database=self.bd, user=self.user, password=self.passw)
                        return con
                except psycopg2.DatabaseError, e:
                        return False
                	

        def actualizar(self,query,cur,valores):
                cur.execute(query,(valores))
        def eliminar(self,query,cur,valores):
                cur.execute(query,(valores,))

        def consultar(self,query,cur,valores):      
                cur.execute(query,(valores,))
                registro  = cur.fetchone()
                return registro
        def consultartodos(self,query,cur):      
                cur.execute(query)
                registro  = cur.fetchall()
                return registro
        def concont(self,query,cur,valores):
                cur.execute(query,(valores,))
                registro  = cur.fetchall()
                return registro
        def ShowMessage(self):
                wx.MessageBox('Usuario y Contraseña Incorrectos', 'Imposible Conectar',wx.OK | wx.ICON_INFORMATION)