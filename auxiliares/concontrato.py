# -*- coding: utf-8 -*- 
from datetime import datetime
import wx
import wx.xrc
from lib.Casas import Casa
from lib.Coneccion import Coneccion
from lib.Inquilinos import Inquilino
from lib.Propietario import Propietario
from lib.Descuentos import Descuentos
from lib.Contratos import Contrato
from wx.lib.masked import NumCtrl

#BORRAR AL TERMINAR---------------------------------------- 
import psycopg2
import psycopg2
con1=Coneccion('localhost','raices','postgres','Celeste14') #Eliminar esta Linea
cont1=Contrato('','','','','','','')
des1=Descuentos('','')
rdes1=des1.consultartodos(con1)
Casa1=Casa('','','','','')
class concam ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Consulta de Cotrantos", pos = wx.DefaultPosition, size = wx.Size( 580,548 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWFRAME ) )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel15.SetBackgroundColour( wx.Colour( 181, 249, 162 ) )
		
		gSizer11 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText26 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Contrato N° : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		gSizer11.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.NumCtrlc  = NumCtrl(self.m_panel15,-1,style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
		gSizer11.Add( self.NumCtrlc, 0, wx.ALL, 5 )
		
		self.m_button21 = wx.Button( self.m_panel15, wx.ID_ANY, u"BUSCAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button21, 0, wx.ALL, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText27 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Direccion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gSizer11.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.m_textCtrl32 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250, 23), 0 )
		self.m_textCtrl32.Enable( False )
		
		gSizer11.Add( self.m_textCtrl32, 0, wx.ALL, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText28 = wx.StaticText( self.m_panel15, 3, u"Propietario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		gSizer11.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_textCtrl20 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250, 23), 0 )
		self.m_textCtrl20.Enable( False )
		
		gSizer11.Add( self.m_textCtrl20, 0, wx.ALL, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText29 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Inquilino:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		gSizer11.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.m_textCtrl33 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250, 23), 0 )
		gSizer11.Add( self.m_textCtrl33, 0, wx.ALL, 5 )
		self.m_textCtrl33.Enable(False)
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Fecha Inicio:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer11.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_textCtrl26 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_textCtrl26, 0, wx.ALL, 5 )
		self.m_textCtrl26.Enable(False)
		self.m_staticText32 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Fecha de Vencimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer11.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_textCtrl27 = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_textCtrl27, 0, wx.ALL, 5 )
		self.m_textCtrl27.Enable(False)
		self.m_staticText34 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Comision:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer11.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
	
		self.NumCtrl3 = NumCtrl(self.m_panel15,-1,style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
		self.NumCtrl3.Enable( False )
		self.NumCtrl3.SetParameters( integerWidth = 9) 
		self.NumCtrl3.SetParameters( fractionWidth = 2) 
		self.NumCtrl3.SetGroupChar(';')
		self.NumCtrl3.SetDecimalChar(',') 
		self.NumCtrl3.SetGroupChar('.') 
		self.NumCtrl3.SetMin(0) 
		self.NumCtrl3.SetMax(-1) 
		self.NumCtrl3.SetAllowNegative(False) 
		self.NumCtrl3.SetSelectOnEntry(False) 
		self.NumCtrl3.Enable( False )
		
		gSizer11.Add( self.NumCtrl3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT|wx.ALL, 5 )
		
		
		self.m_panel15.SetSizer( gSizer11 )
		self.m_panel15.Layout()
		gSizer11.Fit( self.m_panel15 )
		bSizer12.Add( self.m_panel15, 1, wx.ALIGN_TOP|wx.ALL, 5 )
		
		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel16.SetBackgroundColour( wx.Colour( 181, 249, 162 ) )
		
		gSizer12 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_staticText36 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Descuentos:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gSizer12.Add( self.m_staticText36, 0, wx.ALL, 5 )
		a=0
		m_comboBox7Choices = []
		while a < len(rdes1):
			m_comboBox7Choices.append(rdes1[a][0])
			a = a + 1
		self.m_comboBox7 = wx.ComboBox( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox7Choices, 0 )
		self.m_comboBox7.Enable( False )
		
		gSizer12.Add( self.m_comboBox7, 0, wx.ALL, 5 )
		
		self.NumCtrl2 = NumCtrl(self.m_panel16,-1,style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
		self.NumCtrl2.Enable( False )
		self.NumCtrl2.SetParameters( integerWidth = 9) 
		self.NumCtrl2.SetParameters( fractionWidth = 2) 
		self.NumCtrl2.SetGroupChar(';')
		self.NumCtrl2.SetDecimalChar(',') 
		self.NumCtrl2.SetGroupChar('.') 
		self.NumCtrl2.SetMin(0) 
		self.NumCtrl2.SetMax(-1) 
		self.NumCtrl2.SetAllowNegative(False) 
		self.NumCtrl2.SetSelectOnEntry(False) 
		self.NumCtrl2.Enable( False )
		
		gSizer12.Add( self.NumCtrl2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_LEFT|wx.ALL, 5 )
		self.m_checkBox1 = wx.CheckBox( self.m_panel16, wx.ID_ANY, u"Imprime en Propietario", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox1.Enable( False )
		
		gSizer12.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( self.m_panel16, wx.ID_ANY, u"Imprime en Inmobiliaria", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox2.Enable( False )
		
		gSizer12.Add( self.m_checkBox2, 0, wx.ALL, 5 )
		
		self.m_checkBox3 = wx.CheckBox( self.m_panel16, wx.ID_ANY, u"Imprime en Inquilino", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox3.Enable( False )
		
		gSizer12.Add( self.m_checkBox3, 0, wx.ALL, 5 )
		
		
		self.m_panel16.SetSizer( gSizer12 )
		self.m_panel16.Layout()
		gSizer12.Fit( self.m_panel16 )
		bSizer12.Add( self.m_panel16, 1, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel17 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel17.SetBackgroundColour( wx.Colour( 184, 249, 162 ) )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button24 = wx.Button( self.m_panel17, wx.ID_ANY, u"AGREGAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button24.Enable( False )
		
		bSizer14.Add( self.m_button24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel17.SetSizer( bSizer14 )
		self.m_panel17.Layout()
		bSizer14.Fit( self.m_panel17 )
		bSizer12.Add( self.m_panel17, 1, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel18.SetBackgroundColour( wx.Colour( 191, 255, 162 ) )
		
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		m_listBox1Choices = []
		self.m_listBox1 = wx.ListBox( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		self.m_listBox1.Enable( False )
		
		bSizer15.Add( self.m_listBox1, 0, wx.ALIGN_TOP|wx.ALL|wx.EXPAND|wx.TOP, 5 )
		
		
		self.m_panel18.SetSizer( bSizer15 )
		self.m_panel18.Layout()
		bSizer15.Fit( self.m_panel18 )
		bSizer12.Add( self.m_panel18, 1, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel19 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel19.SetBackgroundColour( wx.Colour( 181, 255, 162 ) )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button25 = wx.Button( self.m_panel19, wx.ID_ANY, u"ELIMINAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button25.Enable( False )
		
		bSizer17.Add( self.m_button25, 0, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel19.SetSizer( bSizer17 )
		self.m_panel19.Layout()
		bSizer17.Fit( self.m_panel19 )
		bSizer12.Add( self.m_panel19, 1, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel20 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel20.SetBackgroundColour( wx.Colour( 181, 255, 162 ) )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button53 = wx.Button( self.m_panel20, wx.ID_ANY, u"EDITAR CONTRATO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button53.Enable( False )
		
		bSizer18.Add( self.m_button53, 0, wx.ALL, 5 )
		
		self.m_button54 = wx.Button( self.m_panel20, wx.ID_ANY, u"ELIMINAR CONTRATO", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button54.Enable( False )
		
		bSizer18.Add( self.m_button54, 0, wx.ALL, 5 )
		
		self.m_button26 = wx.Button( self.m_panel20, wx.ID_ANY, u"GUARDAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button26.Enable( False )
		self.m_button26.Hide()
		
		bSizer18.Add( self.m_button26, 0, wx.ALL, 5 )
		
		self.m_button27 = wx.Button( self.m_panel20, wx.ID_ANY, u"CANCELAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button27.Enable( False )
		self.m_button27.Hide()
		
		bSizer18.Add( self.m_button27, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.m_panel20.SetSizer( bSizer18 )
		self.m_panel20.Layout()
		bSizer18.Fit( self.m_panel20 )
		bSizer12.Add( self.m_panel20, 1, wx.ALIGN_CENTER|wx.ALIGN_TOP|wx.ALL, 5 )
		
		
		self.SetSizer( bSizer12 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button21.Bind( wx.EVT_BUTTON, self.buscar )
		self.m_button24.Bind( wx.EVT_BUTTON, self.agregar )
		self.m_button25.Bind( wx.EVT_BUTTON, self.eliminar )
		self.m_button53.Bind( wx.EVT_BUTTON, self.edcontrato )
		self.m_button54.Bind( wx.EVT_BUTTON, self.eliminarcontrato )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buscar( self, event ):
		cont1.numero=str(self.NumCtrlc.GetValue())

		a=cont1.consultar(con1)
		if len(a)==0:
			wx.MessageBox('Este contrato no existe', 'Info', wx.OK | wx.ICON_INFORMATION)
		else:	
			self.NumCtrlc.Enable(False)
			self.m_button21.Enable(False)
			self.m_button53.Enable(True)
			self.m_button54.Enable(True)
			for i in range (len(a)):
				descuento=a[i][1]
				monto=str(a[i][10])
				imprimep=a[i][7]
				imprimei=a[i][8] 
				imprimeinq=a[i][9] 
				self.m_listBox1.Append(descuento  + " ,"+monto + "," + imprimep + ","+ imprimei + ","+ imprimeinq )

			self.m_textCtrl26.Enable(True)
			self.m_textCtrl27.Enable(True)
			self.NumCtrl3.Enable(True)
			self.m_comboBox7.Enable(True)
			self.NumCtrl2.Enable(True)
			self.m_checkBox1.Enable(True)
			self.m_checkBox2.Enable(True)
			self.m_checkBox3.Enable(True)
			self.m_button24.Enable(True)
			self.m_listBox1.Enable(True)
			self.m_button25.Enable(True)
			self.m_textCtrl32.SetValue(a[0][2])
			self.m_textCtrl20.SetValue(a[0][6])
			self.m_textCtrl33.SetValue(a[0][3])
			self.m_textCtrl26.SetValue(a[0][4])
			self.m_textCtrl27.SetValue(a[0][5])
			self.NumCtrl3.SetValue(a[0][11])
		event.Skip()
	
	def agregar( self, event ):
		desc=self.m_comboBox7.GetValue()
		monto=self.NumCtrl2.GetValue()
		monto=str(monto)
		if self.m_checkBox1.GetValue()==True:
			chek1="SI"
		else:
			chek1="NO"
		if self.m_checkBox2.GetValue()==True:
			chek2="SI"
		else:
			chek2="NO"
		if self.m_checkBox3.GetValue()==True:
			chek3="SI"
		else:
			chek3="NO"
		self.m_listBox1.Append(desc  + " ,"+monto + "," + chek1 + ","+ chek2 + ","+ chek3 )
		event.Skip()
	
	def eliminar( self, event ):
		sel = self.m_listBox1.GetSelection()
		if sel != -1:
			self.m_listBox1.Delete(sel)
		event.Skip()
	
	def edcontrato( self, event ):
		cont1.direccion=self.m_textCtrl32.GetValue()
		cont1.inquilinos=self.m_textCtrl33.GetValue()
		cont1.fechain=self.m_textCtrl26.GetValue()
		cont1.fechavto=self.m_textCtrl27.GetValue()
		cont1.propietario=self.m_textCtrl20.GetValue()
		cont1.comision=self.NumCtrl3.GetValue()
		cont1.eliminar(con1)
		for i in range(self.m_listBox1.GetCount()):
			a = self.m_listBox1.GetString(i)
			lista=a.split(',')
			descripcion=lista[0]
			des1.descuento=lista[0]
			rd=des1.consultar(con1)
			monto=lista[1]
			monto=monto[0:len(monto)]
			impripro=lista[2]
			impripro=impripro[0:len(impripro)]
			imprinmo=lista[3]
			imprinmo=imprinmo[0:len(imprinmo)]
			imprinq=lista[4]
			imprinq=imprinq[0:len(imprinq)]
	
			cont1.agregar(con1,descripcion,monto,impripro,imprinmo,imprinq,rd[1])
		self.Destroy()
		event.Skip()
	
	def eliminarcontrato( self, event ):
		Casa1.contrato='0'
		Casa1.direccion=self.m_textCtrl32.GetValue()
		Casa1.desalquilar(con1)
		cont1.eliminar(con1)
		self.Destroy()
		event.Skip()

	
app = wx.App(False)
ventana = concam(None)
ventana.Show()
app.MainLoop()
