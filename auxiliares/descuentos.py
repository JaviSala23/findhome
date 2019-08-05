# -*- coding: utf-8 -*- 

import wx
import wx.xrc
from lib.Coneccion import Coneccion
from lib.Descuentos import Descuentos
#BORRAR AL TERMINAR---------------------------------------- 
import psycopg2
con1=Coneccion('localhost','raices','postgres','Celeste14') #Eliminar esta Linea
descuento1=Descuentos('','')
registro=descuento1.consultartodos(con1)
#---------------------------------------------------------


class Descuento ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Actualizar Descuentos", pos = wx.DefaultPosition, size = wx.Size( 600,375 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.Colour( 245, 174, 10 ) )
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Descripcion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		gSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250, 23), 0 )
		self.m_textCtrl1.Enable( False )
		
		gSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Codigo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		gSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl2.Enable( False )
		
		gSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( gSizer1 )
		self.m_panel1.Layout()
		gSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.Colour( 245, 174, 10 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 247, 220, 166 ) )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Descripcion:", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.m_panel5.SetBackgroundColour( wx.Colour( 247, 220, 166 ) )
		
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
		descuento1.descuento=self.m_comboBox1.GetValue()
		registro=descuento1.consultar(con1)
		self.m_textCtrl1.SetValue(registro[0])
		a=str(registro[1])
		self.m_textCtrl2.SetValue(a)
		event.Skip()
	
	def nuevo( self, event ):
		self.m_textCtrl1.Enable(True)
		self.m_comboBox1.Enable(False)
		self.m_button1.Enable(False)
		registro=descuento1.consultartodos(con1)
		i=len(registro)+2
		i=str(i)
		self.m_textCtrl2.SetValue(i)
		self.m_button6.Enable(True)
		self.m_button5.Enable(True)
		self.a=1


		event.Skip()
	
	def modificar( self, event ):
		self.m_textCtrl1.Enable(True)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)
		self.m_button4.Enable(False)
		self.m_button3.Enable(False)
		self.a=2
		event.Skip()
	
	def eliminar( self, event ):
		self.a=3
		self.m_textCtrl1.Enable(True)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)
		self.m_button4.Enable(False)
		self.m_button3.Enable(False)
		event.Skip()
	
	def aceptar( self, event ):
		descuento1.descuento=self.m_textCtrl1.GetValue()
		descuento1.codigo=self.m_textCtrl2.GetValue()
		w=self.m_comboBox1.GetValue()
		if self.a==1:
			descuento1.agregar(con1)
		elif self.a==2:
			descuento1.update(con1,w)	
		elif self.a==3:
			descuento1.eliminar(con1,w)
		self.Destroy()
		event.Skip()
	
	def cancelar( self, event ):
		self.Destroy()
		event.Skip()

app = wx.App(False)
ventana = Descuentos(None)
ventana.Show()
app.MainLoop()