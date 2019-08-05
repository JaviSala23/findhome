# -*- coding: utf-8 -*- 

import wx
import wx.xrc
from lib.Coneccion import Coneccion
from casas import casas

class login ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ingreso", pos = wx.DefaultPosition, size = wx.Size( 248,140 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 181, 225, 203 ) )
		
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Usuario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		gSizer9.Add( self.m_staticText19, 0, wx.ALL, 5 )
		
		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl14, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Contraseña:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gSizer9.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer9.Add( self.m_textCtrl15, 0, wx.ALL, 5 )
		
		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button19, 0, wx.ALL, 5 )
		
		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button20, 0, wx.ALL, 5 )
		
		
		self.SetSizer( gSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button19.Bind( wx.EVT_BUTTON, self.aceptar )
		self.m_button20.Bind( wx.EVT_BUTTON, self.cancelar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def aceptar( self, event ):
		usuario=self.m_textCtrl14.GetValue()
		contra=self.m_textCtrl15.GetValue()
		con1=Coneccion('localhost','raices',usuario,contra)
		ap=con1.conectar()
		if ap!=None:
			self.Destroy()
			principal = casas(None)
			principal.Show()
			app.MainLoop()
		event.Skip()
	
	def cancelar( self, event ):
		self.Destroy()
		event.Skip()
	

app = wx.App(False)
ventana = login(None)
ventana.Show()
app.MainLoop()