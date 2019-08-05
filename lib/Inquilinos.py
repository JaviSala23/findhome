import Coneccion

class Inquilino:
	def __init__(self,nombre,direccion,localidad,telefono,celular,email):
		self.nombre=nombre
		self.direccion=direccion
		self.localidad=localidad
		self.telefono=telefono
		self.celular=celular
		self.email=email

	def agregar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="INSERT INTO inquilinos(nombre,direccion,localidad,telefono,celular,email) VALUES(%s,%s,%s,%s,%s,%s)"
		valores=self.nombre,self.direccion,self.localidad,self.telefono,self.celular,self.email
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
	def update(self,con1,filtro):
		cone=con1.conectar()
		cur=cone.cursor()
		query="UPDATE inquilinos SET nombre=%s, direccion=%s, localidad=%s, telefono=%s, celular=%s, email=%s WHERE nombre=%s "
		valores=self.nombre,self.direccion,self.localidad,self.telefono,self.celular,self.email, filtro
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
		#TENER EN CUENTA LOS CONTRATOS Y LAS CASAS.
	def eliminar(self,con1,filtro):
		cone=con1.conectar()
		cur=cone.cursor()
		query="DELETE FROM inquilinos WHERE nombre=%s "
		valores=filtro
		con1.eliminar(query,cur,valores)
		cone.commit()
		cone.close()

		#TENER EN CUENTA LOS CONTRATOS.
	def consultar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM inquilinos WHERE nombre=%s ORDER BY nombre"
		registro=con1.consultar(query,cur,self.nombre)
		return registro
	def consultartodos(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM inquilinos ORDER BY nombre"
		registro=con1.consultartodos(query,cur)
		return registro
