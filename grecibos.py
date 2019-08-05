# -*- coding: utf-8 -*- 

import wx
import wx.xrc
from wx.lib.masked import NumCtrl
from lib.Casas import Casa
from lib.Contratos import Contrato
from lib.Coneccion import Coneccion
import report
import psycopg2
con1=Coneccion('localhost','raices','postgres','Celeste14')

class recibos ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generar Recibos", pos = wx.DefaultPosition, size = wx.Size( 569,214 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.Cont1=Contrato('','','','','','','')
		self.casa1=Casa('','','','','')
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 207, 69, 241 ) )
		
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel29 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel29.SetBackgroundColour( wx.Colour( 252, 152, 215 ) )
		
		gSizer12 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.m_radioBtn5 = wx.RadioButton( self.m_panel29, wx.ID_ANY, u"Imprimir un Recibo", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_radioBtn5, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_radioBtn6 = wx.RadioButton( self.m_panel29, wx.ID_ANY, u"Impresion Masiva de Recibos", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_radioBtn6, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self.m_panel29, wx.ID_ANY, u"Numero de Contrato:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		gSizer12.Add( self.m_staticText46, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_textCtrl28 = wx.TextCtrl( self.m_panel29, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer12.Add( self.m_textCtrl28, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		self.m_panel29.SetSizer( gSizer12 )
		self.m_panel29.Layout()
		gSizer12.Fit( self.m_panel29 )
		bSizer32.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel32 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel32.SetBackgroundColour( wx.Colour( 248, 179, 253 ) )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText47 = wx.StaticText( self.m_panel32, wx.ID_ANY, u"Periodo:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		bSizer33.Add( self.m_staticText47, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_textCtrl29 = wx.TextCtrl( self.m_panel32, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_textCtrl29, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_button35 = wx.Button( self.m_panel32, wx.ID_ANY, u"Generar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_button35, 0, wx.ALIGN_BOTTOM|wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.m_panel32.SetSizer( bSizer33 )
		self.m_panel32.Layout()
		bSizer33.Fit( self.m_panel32 )
		bSizer32.Add( self.m_panel32, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer32 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.a='uno'
		
		# Connect Events
		self.m_radioBtn5.Bind( wx.EVT_RADIOBUTTON, self.Uno )
		self.m_radioBtn6.Bind( wx.EVT_RADIOBUTTON, self.Todos )
		self.m_button35.Bind( wx.EVT_BUTTON, self.Generar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def Uno( self, event ):
		self.a='uno'
		event.Skip()
	
	def Todos( self, event ):
		self.a='todos'
		self.m_textCtrl28.Enable(False)

		event.Skip()
	
	def Generar( self, event ):
		periodo=self.m_textCtrl29.GetValue()
		if self.a=='uno':
			self.Cont1.numero=self.m_textCtrl28.GetValue()
			reg=self.Cont1.consultar(con1)
			if reg==[]:
				wx.MessageBox('Este contrato no existe', 'Info', wx.OK | wx.ICON_INFORMATION)
			else:
				vencido=self.Cont1.consultarVencidos(con1,str(self.m_textCtrl28.GetValue()))
				print vencido
				if vencido=="en orden":
					report.pdf(periodo,reg,con1)
				else:
					wx.MessageBox('Este contrato esta vencido', 'Info', wx.OK | wx.ICON_INFORMATION)
		else:
			reg=self.casa1.consultarAlq(con1)
			print reg
			i=0
			imp=[]
			for i in range(len(reg)):
					cst=str(reg[i][4])
					ven=self.Cont1.consultarVencidos(con1,cst)
					print ven
					if ven=='VENCIDO':	
						i=i+1
					else:
						self.Cont1.numero=str(reg[i][4])
						reg1=self.Cont1.consultar(con1)
						imp.append(reg1)
			report.pdft(periodo,imp,con1)

		event.Skip()
	
app = wx.App(False)
ventana = recibos(None)
ventana.Show()
app.MainLoop()
