import Coneccion

class Descuentos:
	def __init__(self,codigo,descuento):
		self.codigo=codigo
		self.descuento=descuento

	def agregar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="INSERT INTO descuentos(coddes,descripcion) VALUES(%s,%s)"
		valores=self.codigo,self.descuento
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
	def update(self,con1,filtro):
		cone=con1.conectar()
		cur=cone.cursor()
		query="UPDATE descuentos SET  descripcion=%s WHERE descripcion=%s"
		valores=self.descuento,filtro
		con1.actualizar(query,cur,valores)
		cone.commit()
		cone.close()
		#TENER EN CUENTA LOS CONTRATOS Y LAS CASAS.
	def eliminar(self,con1,filtro):
		cone=con1.conectar()
		cur=cone.cursor()
		query="DELETE FROM descuentos WHERE descripcion=%s "
		valores=filtro
		con1.eliminar(query,cur,valores)
		cone.commit()
		cone.close()

		#TENER EN CUENTA EN CONTRATOS.
	def consultartodos(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM descuentos ORDER BY coddes"
		registro=con1.consultartodos(query,cur)
		return registro
	def consultar(self,con1):
		cone=con1.conectar()
		cur=cone.cursor()
		query="SELECT * FROM descuentos WHERE descripcion=%s ORDER BY coddes"
		registro=con1.consultar(query,cur,self.descuento)
		return registro
