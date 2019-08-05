# -*- coding: utf-8 -*- 

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
con1=Coneccion('localhost','raices','postgres','Celeste14') #Eliminar esta Linea
Casa1=Casa('','','','','')
rcasas=Casa1.consultarLibres(con1)
print rcasas
inq1=Inquilino('','','','','','')
rinq1=inq1.consultartodos(con1)
des1=Descuentos('','')
rdes1=des1.consultartodos(con1)


class contratos ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Contratos", pos = wx.DefaultPosition, size = wx.Size( 640,542 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 58, 5, 19 ) )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel15.SetBackgroundColour( wx.Colour( 251, 203, 159 ) )
		
		gSizer11 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.m_staticText26 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Contrato N° : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		gSizer11.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.NumCtrlc = NumCtrl(self.m_panel15,-1,style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
		gSizer11.Add( self.NumCtrlc, 0, wx.ALL, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText27 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Direccion:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gSizer11.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		m_comboBox5Choices = []
		i = 0
		while i < len(rcasas):
			m_comboBox5Choices.append(rcasas[i][1])
			i = i + 1
		self.m_comboBox5 = wx.ComboBox( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250, 23), m_comboBox5Choices, 0 )
		gSizer11.Add( self.m_comboBox5, 0, wx.ALL, 5 )

		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button21 = wx.Button( self.m_panel15, wx.ID_ANY, u"BUSCAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_button21, 0, wx.ALL, 5 )
		
		
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
		
		m_comboBox6Choices = []
		i = 0
		while i < len(rinq1):
			m_comboBox6Choices.append(rinq1[i][0])
			i = i + 1
		self.m_comboBox6 = wx.ComboBox( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250, 23), m_comboBox6Choices, 0 )
		self.m_comboBox6.Enable( False )
		
		gSizer11.Add( self.m_comboBox6, 0, wx.ALL, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		gSizer11.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Fecha Inicio:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer11.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_datePicker2 = wx.DatePickerCtrl( self.m_panel15, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DEFAULT|wx.DP_DROPDOWN )
		self.m_datePicker2.Enable( False )
		
		gSizer11.Add( self.m_datePicker2, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Fecha de Vencimiento", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer11.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_datePicker3 = wx.DatePickerCtrl( self.m_panel15, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.DP_DROPDOWN )
		self.m_datePicker3.Enable( False )
		
		gSizer11.Add( self.m_datePicker3, 0, wx.ALL, 5 )
		
		self.m_staticText34 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Comision:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		gSizer11.Add( self.m_staticText34, 0, wx.ALL, 5 )
		
		self.NumCtrl1 = NumCtrl(self.m_panel15,-1,style=wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB)
		self.NumCtrl1.SetParameters( integerWidth = 9) 
		self.NumCtrl1.SetParameters( fractionWidth = 2) 
		self.NumCtrl1.SetGroupChar(';')
		self.NumCtrl1.SetDecimalChar(',') 
		self.NumCtrl1.SetGroupChar('.') 
		self.NumCtrl1.SetMin(0) 
		self.NumCtrl1.SetMax(-1) 
		self.NumCtrl1.SetAllowNegative(False) 
		self.NumCtrl1.SetSelectOnEntry(False) 
		self.NumCtrl1.Enable( False )

		
		gSizer11.Add( self.NumCtrl1, 0, wx.ALL, 5 )
		
		
		self.m_panel15.SetSizer( gSizer11 )
		self.m_panel15.Layout()
		gSizer11.Fit( self.m_panel15 )
		bSizer12.Add( self.m_panel15, 1, wx.ALIGN_TOP|wx.ALL, 5 )
		
		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel16.SetBackgroundColour( wx.Colour( 251, 203, 159 ) )
		
		gSizer12 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_staticText36 = wx.StaticText( self.m_panel16, wx.ID_ANY, u"Descuentos:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gSizer12.Add( self.m_staticText36, 0, wx.ALL, 5 )
		i=0
		m_comboBox7Choices = []
		while i < len(rdes1):
			m_comboBox7Choices.append(rdes1[i][0])
			i = i + 1
		self.m_comboBox7 = wx.ComboBox( self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, (250,23), m_comboBox7Choices, 0 )
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
		self.m_panel17.SetBackgroundColour( wx.Colour( 251, 203, 159 ) )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button24 = wx.Button( self.m_panel17, wx.ID_ANY, u"AGREGAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button24.Enable( False )
		
		bSizer14.Add( self.m_button24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel17.SetSizer( bSizer14 )
		self.m_panel17.Layout()
		bSizer14.Fit( self.m_panel17 )
		bSizer12.Add( self.m_panel17, 1, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel18.SetBackgroundColour( wx.Colour( 251, 203, 159 ) )
		
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
		self.m_panel19.SetBackgroundColour( wx.Colour( 251, 203, 159 ) )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button25 = wx.Button( self.m_panel19, wx.ID_ANY, u"ELIMINAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button25.Enable( False )
		
		bSizer17.Add( self.m_button25, 0, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel19.SetSizer( bSizer17 )
		self.m_panel19.Layout()
		bSizer17.Fit( self.m_panel19 )
		bSizer12.Add( self.m_panel19, 1, wx.ALIGN_TOP|wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel20 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel20.SetBackgroundColour( wx.Colour( 251, 203, 159 ) )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button26 = wx.Button( self.m_panel20, wx.ID_ANY, u"GUARDAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button26.Enable( False )
		
		bSizer18.Add( self.m_button26, 0, wx.ALL, 5 )
		
		self.m_button27 = wx.Button( self.m_panel20, wx.ID_ANY, u"CANCELAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button27.Enable( False )
		
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
		self.m_button26.Bind( wx.EVT_BUTTON, self.guardar )
		self.m_button27.Bind( wx.EVT_BUTTON, self.cancelar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def buscar( self, event ):
		self.m_comboBox6.Enable(True)
		self.m_datePicker2.Enable(True)
		self.m_datePicker3.Enable(True)
		self.NumCtrl1.Enable(True)
		self.m_comboBox7.Enable(True)
		self.NumCtrl2.Enable(True)
		self.m_checkBox1.Enable(True)
		self.m_checkBox2.Enable(True)
		self.m_checkBox3.Enable(True)
		self.m_listBox1.Enable(True)
		self.m_button24.Enable(True) 
		self.m_button25.Enable(True) 
		self.m_button26.Enable(True)
		self.m_button27.Enable(True)
		direccion=self.m_comboBox5.GetValue()
		Casa2=Casa('',direccion,'','','')
		regp=Casa2.consultar(con1)
		self.m_textCtrl20.SetValue(regp[0])
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

	
	def guardar( self, event ):
		for i in range(self.m_listBox1.GetCount()):
			a = self.m_listBox1.GetString(i)
			lista=a.split(',')
			descripcion=lista[0]
			descuento1=Descuentos('',descripcion)
			rd=descuento1.consultar(con1)
			monto=lista[1]
			monto=monto[0:len(monto)]
			impripro=lista[2]
			impripro=impripro[0:len(impripro)]
			imprinmo=lista[3]
			imprinmo=imprinmo[0:len(imprinmo)]
			imprinq=lista[4]
			imprinq=imprinq[0:len(imprinq)]
			ncontrato=self.NumCtrlc.GetValue()
			comision=self.NumCtrl1.GetValue()
			direccion=self.m_comboBox5.GetValue()
			propietario=self.m_textCtrl20.GetValue()
			inquilinos=self.m_comboBox6.GetValue()
			seleccion1=self.m_datePicker2 .GetValue()
			mes1=1+seleccion1.Month
			mes=str(mes1)
			dia=str(seleccion1.Day)
			ano=str(seleccion1.Year)
			fechain=dia+"/"+mes+"/"+ano
			fechain=str(fechain)
			seleccion2=self.m_datePicker3.GetValue()
			mes1=seleccion2.Month+1
			mes=str(mes1)
			dia=str(seleccion2.Day)
			ano=str(seleccion2.Year)
			fechavto=dia+"/"+mes+"/"+ano
			fechavto=str(fechavto)
			cont1=Contrato(ncontrato,direccion,inquilinos,fechain,fechavto,propietario,comision)
			cont1.agregar(con1,descripcion,monto,impripro,imprinmo,imprinq,rd[1])
			Casa1.direccion=self.m_comboBox5.GetValue()
			Casa1.contrato=self.NumCtrlc.GetValue()
			Casa1.alquilar(con1)
		self.Destroy()
	def cancelar( self, event ):
		self.Destroy()
		event.Skip()

app = wx.App(False)
ventana = contratos(None)
ventana.Show()
app.MainLoop()
