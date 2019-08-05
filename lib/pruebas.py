import Coneccion
import Propietario
con1=Coneccion.Coneccion('localhost','raices','postgres','Celeste14')
Javier=Propietario.Propietario('Celeste','asdasd','asdsa','asdsa','asdsdas','asds')
registro= Javier.consultar(con1,Javier.nombre)
print registro

