import sys
import os
import ConfigParser
import datetime
from datetime import date
import wx
import wx.xrc
from lib.Propietario import Propietario
from lib.Coneccion import Coneccion
from lib.Casas import Casa
from lib.Contratos import Contrato
import lib.modulos
from lib.Inquilinos import Inquilino
from lib.Descuentos import Descuentos
from wx.lib.masked import NumCtrl
import report
#BORRAR AL TERMINAR ----------------------------------
import psycopg2
con1=Coneccion('localhost','raices','postgres','Celeste14') #Eliminar esta Linea
#################

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 241,200 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.Inquilino=Inquilino('','','','','','')
		self.registro=self.Inquilino.consultartodos(con1)
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Contrato:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Inquilino:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = []
		i = 0
		while i < len(self.registro):
			m_comboBox1Choices.append(self.registro[i][0])
			i = i + 1
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		bSizer1.Add( self.m_comboBox1, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.guardar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def guardar( self, event ):
		cone=con1.conectar()
		cur=cone.cursor()
		inquilino=self.m_comboBox1.GetValue()
		contrato=self.m_textCtrl1.GetValue()
		query="UPDATE contratos SET inquilino=%s WHERE ncontrato=%s "
		valores=inquilino,contrato
		con1.actualizar(query,cur,valores)
		cone.commit()
		wx.MessageBox('Contrato Actualizado', 'Info', wx.OK | wx.ICON_INFORMATION)
		cone.close()
		event.Skip()
	

app = wx.App(False)
ventana = MyFrame1(None)
ventana.Show()
app.MainLoop()
