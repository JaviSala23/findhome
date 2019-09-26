import Coneccion

class Casa:
	def __init__(self,propietario,direccion,localidad,estado,contrato):
		self.propietario=propietario
		self.direccion=direccion
		self.localidad=localidad
		self.estado=estado
		self.contrato=contrato

	def agregar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="INSERT INTO casas(propietario,direccion,localidad,estado,contrato) VALUES(%s,%s,%s,%s,%s)"
		valores=self.propietario,self.direccion,self.localidad,'LIBRE',self.contrato,
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
	def update(self,con1,filtro):
		cone=con1.conectar()
		cur=cone.cursor()
		query="UPDATE casas SET propietario=%s, direccion=%s, localidad=%s, estado=%s, contrato=%s WHERE direccion=%s "
		valores=self.propietario,self.direccion,self.localidad,self.estado,self.contrato,self.direccion
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
		#TENER EN CUENTA LOS CONTRATOS Y LAS CASAS.
	def eliminar(self,con1,filtro):
		cone=con1.conectar()
		cur=cone.cursor()
		query="DELETE FROM casas WHERE direccion=%s "
		valores=filtro
		con1.eliminar(query,cur,valores)
		cone.commit()
		cone.close()
		#TENER EN CUENTA LOS CONTRATOS Y LOS INQUILINOS.
	def consultar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM casas WHERE direccion=%s ORDER BY direccion"
		registro=con1.consultar(query,cur,self.direccion)
		return registro
	def consultartodos(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM casas ORDER BY direccion"
		registro=con1.consultartodos(query,cur)
		return registro
	def alquilar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="UPDATE casas SET estado='ALQUILADA', contrato=%s WHERE direccion=%s"
		valores=self.contrato,self.direccion
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
	def consultarLibres(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM casas WHERE estado='LIBRE' ORDER BY direccion"
		registro=con1.consultartodos(query,cur)
		return registro
	def desalquilar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="UPDATE casas SET estado='LIBRE', contrato=%s WHERE direccion=%s"
		valores=0,self.direccion
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
	def consultarAlq(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM casas WHERE estado='ALQUILADA' ORDER BY direccion"
		registro=con1.consultartodos(query,cur)
		return registro
