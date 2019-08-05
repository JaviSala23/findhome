import Coneccion
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.platypus import Image
import datetime
from datetime import date
import time

class Contrato:
	def __init__(self,numero,direccion,inquilino,fechain,fechavto,propietario,comision):
		self.numero=numero
		self.direccion=direccion
		self.inquilino=inquilino
		self.fechain=fechain
		self.fechavto=fechavto
		self.propietario=propietario
		self.comision=comision


#Modificiar Operaciones...

	def agregar(self,con1,descuento,monto,imprimiep,imprimei,imprimier,coddes):
		cone=con1.conectar()
		cur=cone.cursor()
		query="INSERT INTO contratos(ncontrato,descripcion,direccion,inquilino,fechain,fechavto,propietario,comision,imprimiep,imprimei,imprimier,monto,coddes) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		valores=self.numero,descuento,self.direccion,self.inquilino,self.fechain,self.fechavto,self.propietario,self.comision,imprimiep,imprimei,imprimier,monto,coddes
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
	def update(self,con1,filtro):
		cone=con1.conectar()
		cur=cone.cursor()
		query="UPDATE descuentos SET codigo=%s, descripcion=%s "
		valores=self.codigo,self.descuento,filtro
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
		#TENER EN CUENTA LOS CONTRATOS Y LAS CASAS.
	def eliminar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="DELETE FROM contratos WHERE ncontrato=%s "
		valores=self.numero
		con1.eliminar(query,cur,valores)
		cone.commit()
		cone.close()
	def consultartodos(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM contratos ORDER BY ncontrato"
		registro=con1.consultartodos(query,cur)
		return registro
	def consultar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM contratos WHERE ncontrato=%s ORDER BY coddes"
		registro=con1.concont(query,cur,self.numero)
		return registro
	
	def consultarVencidos(self,con1,numero):
		cone=con1.conectar()
		cur=cone.cursor()
                query="SELECT * FROM contratos WHERE ncontrato=%s ORDER BY direccion"
                registro=con1.concont(query,cur,numero)
                if registro!='':
                        d=date.today()
                        day=int(d.day)
                        month=int(d.month)
                        year=int(d.year)
                        reg=registro[0]
                        i=0
                        for i in range(len(reg)):
                                fechan=reg[5].split('/')
                                year1=int(fechan[2])
                                month1=int(fechan[1])
                                day1=int(fechan[0])
                                if year1<year:
                                        return 'VENCIDO'
                                        i=i+1
                                elif year1 == year:
                                        if month1 < month:
                                                return 'VENCIDO'
                                                i=i+1
                                        elif month1== month:
                                                if day1 < day:
                                                        return 'VENCIDO'
                                                        i=i+1

                                                else:
                                                        return "en orden"
                                                        i=i+1
                                        else:
                                                return "en orden"
                                                i=i+1        
                                else:
                                        return "en orden"
                                        i=i+1
                else:
                        return 'null'
                
