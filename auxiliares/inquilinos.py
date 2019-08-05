# -*- coding: utf-8 -*- 



import wx
import wx.xrc
from lib.Inquilinos import Inquilino
from lib.Coneccion import Coneccion

#BORRAR AL TERMINAR ----------------------------------
import psycopg2
con1=Coneccion('localhost','raices','postgres','Celeste14') #Eliminar esta Linea
Inquilino=Inquilino('','','','','','')
registro=Inquilino.consultartodos(con1)
#------------------------------------------------------------


class Inquilinos ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Actualizar Inquilinos", pos = wx.DefaultPosition, size = wx.Size( 800,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 249, 204, 245 ) )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.Colour( 214, 154, 175 ) )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl1.Enable( False )
		
		gSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Direccion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.Enable( False )
		
		gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Localidad:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		gSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl3.Enable( False )
		
		gSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Telefono:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl4.Enable( False )
		
		gSizer1.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Celular:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl5.Enable( False )
		
		gSizer1.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Email:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl6.Enable( False )
		
		gSizer1.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( gSizer1 )
		self.m_panel1.Layout()
		gSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.Colour( 214, 154, 175 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 204, 36, 141 ) )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = []
		i = 0
		while i < len(registro):
			m_comboBox1Choices.append(registro[i][0])
			i = i + 1
		self.m_comboBox1 = wx.ComboBox( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetFont( wx.Font( 8, 74, 90, 90, False, "Arial" ) )
		
		gSizer3.Add( self.m_comboBox1, 0, wx.ALL, 5 )
		
		
		gSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button1 = wx.Button( self.m_panel4, wx.ID_ANY, u"BUSCAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( gSizer3 )
		self.m_panel4.Layout()
		gSizer3.Fit( self.m_panel4 )
		bSizer2.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"NUEVO", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self.m_panel2, wx.ID_ANY, u"MODIFICAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button3.Enable( False )
		
		bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self.m_panel2, wx.ID_ANY, u"ELIMINAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button4.Enable( False )
		
		bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_panel5 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.Colour( 204, 36, 141 ) )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button5 = wx.Button( self.m_panel5, wx.ID_ANY, u"ACEPTAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.Enable( False )
		
		bSizer3.Add( self.m_button5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel5, wx.ID_ANY, u"CANCELAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.Enable( False )
		
		bSizer3.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( bSizer3 )
		self.m_panel5.Layout()
		bSizer3.Fit( self.m_panel5 )
		bSizer2.Add( self.m_panel5, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.ac=0
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
	
	
	# Virtual event handlers, overide them in your derived class
	def buscar( self, event ):
		self.m_comboBox1.Enable(False)
		self.m_button1.Enable(False)
		self.m_button2.Enable(False)
		self.m_button3.Enable(True)
		self.m_button4.Enable(True)
		nombre=self.m_comboBox1.GetValue()
		Inquilino.nombre=nombre
		rg1=Inquilino.consultar(con1)
		self.m_textCtrl1.SetValue(rg1[0])
		self.m_textCtrl2.SetValue(rg1[1])
		self.m_textCtrl3.SetValue(rg1[2])
		self.m_textCtrl4.SetValue(rg1[3])
		self.m_textCtrl5.SetValue(rg1[4])
		self.m_textCtrl6.SetValue(rg1[5])
		event.Skip()
	
	def nuevo( self, event ):
		self.ac=1
		self.m_textCtrl1.Enable(True)
		self.m_textCtrl2.Enable(True)
		self.m_textCtrl3.Enable(True)
		self.m_textCtrl4.Enable(True)
		self.m_textCtrl5.Enable(True)
		self.m_textCtrl6.Enable(True)
		self.m_button1.Enable(False)
		self.m_button2.Enable(False)
		self.m_button3.Enable(False)
		self.m_button4.Enable(False)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)

		event.Skip()
	
	def modificar( self, event ):
		self.ac=2
		self.m_textCtrl1.Enable(True)
		self.m_textCtrl2.Enable(True)
		self.m_textCtrl3.Enable(True)
		self.m_textCtrl4.Enable(True)
		self.m_textCtrl5.Enable(True)
		self.m_textCtrl6.Enable(True)
		self.m_button3.Enable(False)
		self.m_button4.Enable(False)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)

		event.Skip()
	
	def eliminar( self, event ):
		self.ac=3
		self.m_button3.Enable(False)
		self.m_button4.Enable(False)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)
		event.Skip()
	
	def aceptar( self, event ):
		Inquilino.nombre=self.m_textCtrl1.GetValue()
		Inquilino.direccion=self.m_textCtrl2.GetValue()
		Inquilino.localidad=self.m_textCtrl3.GetValue()
		Inquilino.telefono=self.m_textCtrl4.GetValue()
		Inquilino.celular=self.m_textCtrl5.GetValue()
		Inquilino.email=self.m_textCtrl6.GetValue()
		self.filtro=self.m_comboBox1.GetValue()
		if self.ac==1:
			Inquilino.agregar(con1)
		if self.ac==2:
			Inquilino.update(con1,self.filtro)
		if self.ac==3:
			Inquilino.eliminar(con1,self.filtro)
		self.Destroy()
		event.Skip()
	
	def cancelar( self, event ):
		self.Destroy()
		event.Skip()

app = wx.App(False)
ventana = Inquilinos(None)
ventana.Show()
app.MainLoop()