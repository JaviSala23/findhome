# -*- coding: utf-8 -*- 

import wx
import wx.xrc

from lib.Casas import Casa
from lib.Coneccion import Coneccion
from lib.Propietario import Propietario

#BORRAR AL TERMINAR---------------------------------------- 
import psycopg2
con1=Coneccion('localhost','raices','postgres','Celeste14') #Eliminar esta Linea
Casa1=Casa('','','','','')
registro=Casa1.consultartodos(con1)
propietario1=Propietario('','','','','','')
registro1=propietario1.consultartodos(con1)
#---------------------------------------------------------

class casas ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = 1, title = u"Actualizar Propiedades", pos = wx.DefaultPosition, size = wx.Size( 1115,280 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 247, 148, 130 ) )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.Colour( 13, 88, 164 ) )
		
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText161 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Propietario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )
		self.m_staticText161.Hide()
		
		gSizer5.Add( self.m_staticText161, 0, wx.ALL, 5 )
		m_comboBox4Choices1 = []
		i = 0
		while i < len(registro1):
			m_comboBox4Choices1.append(registro1[i][0])
			i = i + 1
		self.m_comboBox4 = wx.ComboBox( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250, 23), m_comboBox4Choices1, 0 )
		self.m_comboBox4.Hide()
		
		gSizer5.Add( self.m_comboBox4, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Propietario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		self.m_staticText17.Hide()
		
		gSizer5.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.m_textCtrl131 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250, 23), 0 )
		self.m_textCtrl131.Hide()
		
		gSizer5.Add( self.m_textCtrl131, 0, wx.ALL, 5 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Direccion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer5.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		self.m_textCtrl11 = wx.TextCtrl( self.m_panel5, 2, wx.EmptyString, wx.DefaultPosition, (250, 23), 0 )
		gSizer5.Add( self.m_textCtrl11, 0, wx.ALL, 5 )
		self.m_textCtrl11.Enable( False )

		self.m_staticText14 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Localidad:", wx.DefaultPosition, (250, 23), 0 )
		self.m_staticText14.Wrap( -1 )
		gSizer5.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.m_textCtrl12 = wx.TextCtrl( self.m_panel5, 3, wx.EmptyString, wx.DefaultPosition, (250, 23), 0 )
		gSizer5.Add( self.m_textCtrl12, 0, wx.ALL, 5 )
		self.m_textCtrl12.Enable( False )

		self.m_staticText15 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Estado:", wx.DefaultPosition, (250, 23), 0 )
		self.m_staticText15.Wrap( -1 )
		gSizer5.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.m_textCtrl13 = wx.TextCtrl( self.m_panel5, 4, wx.EmptyString, wx.DefaultPosition, (250, 23), 0 )
		gSizer5.Add( self.m_textCtrl13, 0, wx.ALL, 5 )
		self.m_textCtrl13.Enable( False )

		self.m_staticText16 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Contrato Nº:", wx.DefaultPosition, (250, 23), 0 )
		self.m_staticText16.Wrap( -1 )
		gSizer5.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_textCtrl14 = wx.TextCtrl( self.m_panel5, 5, wx.EmptyString, wx.DefaultPosition, (250, 23), 0 )
		gSizer5.Add( self.m_textCtrl14, 0, wx.ALL, 5 )
		self.m_textCtrl14.Enable( False )
		
		self.m_panel5.SetSizer( gSizer5 )
		self.m_panel5.Layout()
		gSizer5.Fit( self.m_panel5 )
		bSizer4.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.Colour( 13, 88, 164 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 250, 111, 86 ) )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText131 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Direccion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText131.Wrap( -1 )
		gSizer3.Add( self.m_staticText131, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = []
		i = 0
		while i < len(registro):
			m_comboBox1Choices.append(registro[i][1])
			i = i + 1
		self.m_comboBox1 = wx.ComboBox( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetFont( wx.Font( 8, 74, 90, 90, False, "Arial" ) )
		
		gSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )
		
		
		gSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self.m_panel4, 6, u"BUSCAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( gSizer3 )
		self.m_panel4.Layout()
		gSizer3.Fit( self.m_panel4 )
		bSizer2.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self.m_panel2, 7, u"NUEVO", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.m_panel2, 8, u"MODIFICAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.Enable( False )
		
		bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self.m_panel2, 9, u"ELIMINAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.Enable( False )
		
		bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		self.m_staticText18 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"¿Desea Elminar el Registro?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		self.m_staticText18.Hide()
		
		self.m_panel51 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel51.SetBackgroundColour( wx.Colour( 250, 111, 86 ) )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button5 = wx.Button( self.m_panel51, 10, u"ACEPTAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.Enable( False )
		
		bSizer3.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel51, 11, u"CANCELAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.Enable( False )
		
		bSizer3.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
		self.m_panel51.SetSizer( bSizer3 )
		self.m_panel51.Layout()
		bSizer3.Fit( self.m_panel51 )
		bSizer2.Add( self.m_panel51, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer4.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.a=0
		self.filtro=""
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.buscar )
		self.m_button2.Bind( wx.EVT_BUTTON, self.nuevo )
		self.m_button3.Bind( wx.EVT_BUTTON, self.modificar )
		self.m_button4.Bind( wx.EVT_BUTTON, self.eliminar )
		self.m_button5.Bind( wx.EVT_BUTTON, self.aceptar )
		self.m_button6.Bind( wx.EVT_BUTTON, self.cancelar )
	
	def __del__( self ):
		pass
	
	def buscar( self, event ):
		self.m_staticText161.Hide()
		self.m_comboBox4.Hide()
		self.m_staticText17.Show()
		self.m_staticText17.Enable(True)
		self.m_textCtrl131.Show()
		self.m_textCtrl131.Enable(False)
		self.filtro=self.m_comboBox1.GetValue()
		casa1=Casa("",self.filtro,"","","")
		registro=casa1.consultar(con1)
		print registro[4]
		self.m_textCtrl11.SetValue(registro[1])
		self.m_textCtrl131.SetValue(registro[0])
		self.m_textCtrl12.SetValue(registro[2])
		self.m_textCtrl13.SetValue(registro[3])
		a=str(registro[4])
		self.m_textCtrl14.SetValue(a)
		self.m_button1.Enable(False)
		self.m_button2.Enable(False)
		self.m_button3.Enable(True)
		self.m_button4.Enable(True)
		self.m_button5.Enable(False)
		self.m_button6.Enable(False)
		self.m_comboBox1.Enable(False)
		event.Skip()
	
	def nuevo( self, event ):
		self.m_staticText17.Hide()
		self.m_textCtrl131.Hide()
		self.m_staticText161.Show()
		self.m_comboBox4.Show()
		self.m_comboBox4.Enable(True)
		self.m_textCtrl11.Enable(True)
		self.m_textCtrl131.Enable(True)
		self.m_textCtrl12.Enable(True)
		self.m_button1.Enable(True)
		self.m_button2.Enable(False)
		self.m_button3.Enable(False)
		self.m_button4.Enable(False)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)
		self.m_comboBox1.Enable(True)
		self.a=1
		event.Skip()
	
	def modificar( self, event ):
		self.a=2
		self.filtro=self.m_comboBox1.GetValue()
		self.m_comboBox1.Enable(False)
		self.m_staticText17.Show()
		self.m_textCtrl131.Show()
		self.m_textCtrl131.Enable(False)
		self.m_textCtrl11.Enable(True)
		self.m_textCtrl12.Enable(True)
		self.m_button1.Enable(False)
		self.m_button2.Enable(False)
		self.m_button3.Enable(False)
		self.m_button4.Enable(False)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)
		self.filtro
		
		event.Skip()
	
	def eliminar( self, event ):
		self.a=3
		self.filtro=self.m_comboBox1.GetValue()
		self.m_comboBox1.Enable(False)
		self.m_staticText17.Show()
		self.m_textCtrl131.Show()
		self.m_textCtrl131.Enable(False)
		self.m_button1.Enable(False)
		self.m_button2.Enable(False)
		self.m_button3.Enable(False)
		self.m_button4.Enable(False)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)

		event.Skip()
	
	def aceptar( self, event ):
		Casa1.propietario=self.m_comboBox4.GetValue()
		Casa1.direccion=self.m_textCtrl11.GetValue()
		Casa1.localidad=self.m_textCtrl12.GetValue()
		Casa1.estado=self.m_textCtrl13.GetValue()
		
		if self.a==1:
			Casa1.contrato=0
			Casa1.agregar(con1)
		elif self.a==2:
			Casa1.contrato=self.m_textCtrl14.GetValue()
			Casa1.update(con1,self.filtro)	
		elif self.a==3:
			if Casa1.estado=="LIBRE":
				Casa1.eliminar(con1,self.filtro)
			else:
				wx.MessageBox('Esta direccion se encuetra asociada a un contrato, por favor primero elimine el contrato', 'Casa Alquilada', wx.OK | wx.ICON_INFORMATION)
		self.Destroy()
   #................Terminar esta parte....................
		
		event.Skip()
		event.Skip()
	
	def cancelar( self, event ):
		self.m_staticText161.Hide()
		self.m_comboBox4.Hide()
		self.m_comboBox1.Enable(True)
		self.m_textCtrl11.Enable(False)
		self.m_textCtrl12.Enable(False)
		self.m_textCtrl131.Hide()
		self.m_button1.Enable(True)
		self.m_button2.Enable(True)
		self.m_button3.Enable(False)
		self.m_button4.Enable(False)
		self.m_button5.Enable(False)
		self.m_button6.Enable(False)
		self.m_textCtrl11.SetValue("")
		self.m_textCtrl12.SetValue("")
		self.m_textCtrl13.SetValue("")
		self.m_textCtrl14.SetValue("")
		self.m_textCtrl131.SetValue("")
		self.Destroy()
		event.Skip()

	
app = wx.App(False)
ventana = casas(None)
ventana.Show()
app.MainLoop()