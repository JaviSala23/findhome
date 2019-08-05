# -*- coding: utf-8 -*- 
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
con1=Coneccion('localhost','raices','','') #Eliminar esta Linea

#Read configuration and assign to global variables



#Read configuration and assign to global variables
cfg = ConfigParser.ConfigParser()
cfg.read('style/config1.ini')
shapefile = cfg.get('splash', 'shape')
transparentcolor = cfg.get('splash', 'transparentcolor')
backgroundfile = cfg.get('splash', 'background')
backgroundx = cfg.getint('splash', 'backgroundx')
backgroundy = cfg.getint('splash', 'backgroundy')



class login ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Ingreso", pos = wx.DefaultPosition, size = wx.Size( 538,179 ), style = wx.CAPTION|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 175, 210, 231 ) )
		
		gSizer9 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_bitmap2 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"img/login2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_bitmap2, 0, wx.ALL, 5 )
		
		self.m_staticText19 = wx.StaticText( self, wx.ID_ANY, u"Usuario:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )
		self.m_staticText19.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial Black" ) )
		
		gSizer9.Add( self.m_staticText19, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl14, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		gSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Contraseña:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		self.m_staticText20.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial Black" ) )
		
		gSizer9.Add( self.m_staticText20, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		self.m_textCtrl15 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer9.Add( self.m_textCtrl15, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )
		
		
		gSizer9.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Aceptar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_button20, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.SetSizer( gSizer9 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.SetIcon(wx.Icon("img/login.png"))
		
		# Connect Events
		self.m_button19.Bind( wx.EVT_BUTTON, self.aceptar )
		self.m_button20.Bind( wx.EVT_BUTTON, self.cancelar )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def aceptar( self, event ):
		con1.user=self.m_textCtrl14.GetValue()
		con1.passw=self.m_textCtrl15.GetValue()
		a=con1.conectar()
		if a==False:
			wx.MessageBox('Error de Usuario o Pass', 'Info', wx.OK | wx.ICON_INFORMATION)
		else:
			self.Destroy()
			ventana = principal(None)
			ventana.Show()
		event.Skip()
	
	def cancelar( self, event ):
		self.Destroy()
		event.Skip()
	



class principal ( wx.Frame ):
	
        def __init__( self, parent ):
                wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bienvenido a FindHome 3", pos = wx.DefaultPosition, size = wx.Size( 383,537 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )

                self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
                self.SetBackgroundColour( wx.Colour( 7, 27, 114 ) )

                bSizer15 = wx.BoxSizer( wx.VERTICAL )

                self.m_panel28 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
                bSizer15.Add( self.m_panel28, 1, wx.EXPAND |wx.ALL, 5 )

                self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"img/logo.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
                bSizer15.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP|wx.ALL, 5 )

                self.m_panel31 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
                self.m_panel31.SetBackgroundColour( wx.Colour( 255, 138, 138 ) )

                bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

                bSizer22 = wx.BoxSizer( wx.VERTICAL )

                self.m_bpButton3 = wx.BitmapButton( self.m_panel31, wx.ID_ANY, wx.Bitmap( u"img/safe.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
                bSizer22.Add( self.m_bpButton3, 0, wx.ALL, 5 )

                self.m_staticText37 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Propietario", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText37.Wrap( -1 )
                bSizer22.Add( self.m_staticText37, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


                bSizer26.Add( bSizer22, 1, wx.EXPAND, 5 )

                bSizer23 = wx.BoxSizer( wx.VERTICAL )

                self.m_bpButton2 = wx.BitmapButton( self.m_panel31, wx.ID_ANY, wx.Bitmap( u"img/house-outline.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
                bSizer23.Add( self.m_bpButton2, 0, wx.ALL, 5 )

                self.m_staticText38 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Casas", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText38.Wrap( -1 )
                bSizer23.Add( self.m_staticText38, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


                bSizer26.Add( bSizer23, 1, wx.EXPAND, 5 )

                bSizer25 = wx.BoxSizer( wx.VERTICAL )

                self.m_bpButton31 = wx.BitmapButton( self.m_panel31, wx.ID_ANY, wx.Bitmap( u"img/man.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
                bSizer25.Add( self.m_bpButton31, 0, wx.ALL, 5 )

                self.m_staticText39 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Inquilinos", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText39.Wrap( -1 )
                bSizer25.Add( self.m_staticText39, 0, wx.ALL, 5 )


                bSizer26.Add( bSizer25, 1, wx.EXPAND, 5 )

                bSizer261 = wx.BoxSizer( wx.VERTICAL )

                self.m_bpButton4 = wx.BitmapButton( self.m_panel31, wx.ID_ANY, wx.Bitmap( u"img/choices.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
                bSizer261.Add( self.m_bpButton4, 0, wx.ALL, 5 )

                self.m_staticText40 = wx.StaticText( self.m_panel31, wx.ID_ANY, u"Descuentos/\nBonificaciones", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText40.Wrap( -1 )
                bSizer261.Add( self.m_staticText40, 0, wx.ALL, 5 )


                bSizer26.Add( bSizer261, 1, wx.EXPAND, 5 )


                self.m_panel31.SetSizer( bSizer26 )
                self.m_panel31.Layout()
                bSizer26.Fit( self.m_panel31 )
                bSizer15.Add( self.m_panel31, 1, wx.EXPAND |wx.ALL, 5 )

                self.m_panel32 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
                self.m_panel32.SetBackgroundColour( wx.Colour( 184, 245, 193 ) )

                bSizer31 = wx.BoxSizer( wx.HORIZONTAL )

                bSizer32 = wx.BoxSizer( wx.VERTICAL )

                self.m_bpButton7 = wx.BitmapButton( self.m_panel32, wx.ID_ANY, wx.Bitmap( u"img/house-contract.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )

                self.m_bpButton7.SetBitmapDisabled( wx.Bitmap( u"img/house-contract.png", wx.BITMAP_TYPE_ANY ) )
                bSizer32.Add( self.m_bpButton7, 0, wx.ALL, 5 )

                self.m_staticText43 = wx.StaticText( self.m_panel32, wx.ID_ANY, u"Nuevo \nContrato", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText43.Wrap( -1 )
                bSizer32.Add( self.m_staticText43, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


                bSizer31.Add( bSizer32, 1, wx.EXPAND, 5 )

                bSizer33 = wx.BoxSizer( wx.VERTICAL )

                self.m_bpButton8 = wx.BitmapButton( self.m_panel32, wx.ID_ANY, wx.Bitmap( u"img/find.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
                bSizer33.Add( self.m_bpButton8, 0, wx.ALL, 5 )

                self.m_staticText44 = wx.StaticText( self.m_panel32, wx.ID_ANY, u"Actualizar\nContratos\n", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText44.Wrap( -1 )
                bSizer33.Add( self.m_staticText44, 0, wx.ALL, 5 )


                bSizer31.Add( bSizer33, 1, wx.EXPAND, 5 )

                bSizer34 = wx.BoxSizer( wx.VERTICAL )

                self.m_bpButton9 = wx.BitmapButton( self.m_panel32, wx.ID_ANY, wx.Bitmap( u"img/icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
                bSizer34.Add( self.m_bpButton9, 0, wx.ALL, 5 )

                self.m_staticText45 = wx.StaticText( self.m_panel32, wx.ID_ANY, u"Recibos\n", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText45.Wrap( -1 )
                bSizer34.Add( self.m_staticText45, 0, wx.ALL, 5 )


                bSizer31.Add( bSizer34, 1, wx.EXPAND, 5 )

                bSizer35 = wx.BoxSizer( wx.VERTICAL )

                self.m_bpButton10 = wx.BitmapButton( self.m_panel32, wx.ID_ANY, wx.Bitmap( u"img/backup.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW )
                bSizer35.Add( self.m_bpButton10, 0, wx.ALL, 5 )

                self.m_staticText46 = wx.StaticText( self.m_panel32, wx.ID_ANY, u"Copia de \nSeguridad/\nRestauraciones\n\n", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText46.Wrap( -1 )
                bSizer35.Add( self.m_staticText46, 0, wx.ALL, 5 )


                bSizer31.Add( bSizer35, 1, wx.EXPAND, 5 )


                self.m_panel32.SetSizer( bSizer31 )
                self.m_panel32.Layout()
                bSizer31.Fit( self.m_panel32 )
                bSizer15.Add( self.m_panel32, 1, wx.EXPAND |wx.ALL, 5 )

                self.m_panel27 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
                self.m_panel27.SetBackgroundColour( wx.Colour( 250, 232, 197 ) )

                bSizer36 = wx.BoxSizer( wx.VERTICAL )

                self.m_staticText47 = wx.StaticText( self.m_panel27, wx.ID_ANY, u"Contratos Vencidos", wx.DefaultPosition, wx.DefaultSize, 0 )
                self.m_staticText47.Wrap( -1 )
                bSizer36.Add( self.m_staticText47, 0, wx.ALL, 5 )

                self.cont1=Contrato('','','','','','','')
                self.casa1=Casa('','','','','')
                reg=self.casa1.consultarAlq(con1)

                i=0
                vencidos=[]
                for i in range(len(reg)):
                        cst=str(reg[i][4])
                        print (reg[i][1])
                        ven=self.cont1.consultarVencidos(con1,cst)
                        if ven!="null":
                                if ven=='VENCIDO':
                                        vencidos.append(reg[i])
                                        i=i+1
                        
                        else:
                             i=i+1   
                e=0
                m_listBox3Choices = ["Numero ---       Direccion                                                             "]
                for e in range(len(vencidos)):
                        m_listBox3Choices.append(str(vencidos[e][4])+"                        "+vencidos[e][1])
                        e=e+1

                self.m_listBox3 = wx.ListBox( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox3Choices, 0 )
                bSizer36.Add( self.m_listBox3, 0, wx.ALL, 5 )
                
                
                self.m_panel27.SetSizer( bSizer36 )
                self.m_panel27.Layout()
                bSizer36.Fit( self.m_panel27 )
                bSizer15.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )
                
                
                self.SetSizer( bSizer15 )
                self.Layout()
                
                self.Centre( wx.BOTH )
                self.SetIcon(wx.Icon("img/home.png"))
                
                # Connect Events
                self.m_bpButton3.Bind( wx.EVT_BUTTON, self.propietarios )
                self.m_bpButton2.Bind( wx.EVT_BUTTON, self.casas )
                self.m_bpButton31.Bind( wx.EVT_BUTTON, self.inquilinos )
                self.m_bpButton4.Bind( wx.EVT_BUTTON, self.descuentos )
                self.m_bpButton7.Bind( wx.EVT_BUTTON, self.contratos )
                self.m_bpButton8.Bind( wx.EVT_BUTTON, self.ccontratos )
                self.m_bpButton9.Bind( wx.EVT_BUTTON, self.recibos )
                self.m_bpButton10.Bind( wx.EVT_BUTTON, self.buckup )
	
        def __del__( self ):
                pass


        # Virtual event handlers, overide them in your derived class
        def propietarios( self, event ):
                ventana1 = propietario(None)
                ventana1.Show()
                event.Skip()

        def casas( self, event ):
                ventana1 = casas(None)
                ventana1.Show()
                event.Skip()

        def inquilinos( self, event ):
                ventana1 = Inquilinos(None)
                ventana1.Show()
                event.Skip()

        def descuentos( self, event ):
                ventana1 = Descuento(None)
                ventana1.Show()
                event.Skip()

        def contratos( self, event ):
                ventana = contratos(None)
                ventana.Show()
                event.Skip()

        def ccontratos( self, event ):
                ventana = concam(None)
                ventana.Show()
                event.Skip()

        def recibos( self, event ):
                ventana = recibos(None)
                ventana.Show()
                event.Skip()

        def buckup( self, event ):
                event.Skip()
#----------------------------------------------------------------------------------------------------
#--------------- Gui de Actualizacion de Propietarios -----------------------------------------------
#----------------------------------------------------------------------------------------------------

class propietario ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Actualizar Propietario", pos = wx.DefaultPosition, size = wx.Size( 800,295 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN|wx.NO_BORDER )
		self.propietario1= Propietario('','','','','','')
		self.registro=self.propietario1.consultartodos(con1)
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 254, 251, 107 ) )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.Colour( 74, 193, 134 ) )
		
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
		self.m_panel2.SetBackgroundColour( wx.Colour( 74, 193, 134 ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 196, 251, 162 ) )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Nombre:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		gSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = []
		i = 0
		while i < len(self.registro):
			m_comboBox1Choices.append(self.registro[i][0])
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
		self.m_panel5.SetBackgroundColour( wx.Colour( 74, 193, 134 ) )
		
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
		self.SetIcon(wx.Icon("img/safe.png"))
		self.Centre( wx.BOTH )
		self.filtro=""
		self.a=0
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
		self.filtro=self.m_comboBox1.GetValue()
		self.propietario1=Propietario(self.filtro,"","","","","")
		self.registro=self.propietario1.consultar(con1)
		self.m_textCtrl1.SetValue(self.registro[0])
		self.m_textCtrl2.SetValue(self.registro[1])
		self.m_textCtrl3.SetValue(self.registro[2])
		self.m_textCtrl4.SetValue(self.registro[3])
		self.m_textCtrl5.SetValue(self.registro[4])
		self.m_textCtrl6.SetValue(self.registro[5])
		self.m_button1.Enable(False)
		self.m_button2.Enable(False)
		self.m_button3.Enable(True)
		self.m_button4.Enable(True)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)
		self.m_comboBox1.Enable(False)
		event.Skip()
	
	def nuevo( self, event ):
		self.m_textCtrl1.Enable(True)
		self.m_textCtrl2.Enable(True)
		self.m_textCtrl3.Enable(True)
		self.m_textCtrl4.Enable(True)
		self.m_textCtrl5.Enable(True)
		self.m_textCtrl6.Enable(True)
		self.m_button2.Enable(False)
		self.m_button1.Enable(False)
		self.m_comboBox1.Enable(False)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)
		self.a=1

		event.Skip()
	
	def modificar( self, event ):
		self.a=2
		self.m_textCtrl1.Enable(True)
		self.m_textCtrl2.Enable(True)
		self.m_textCtrl3.Enable(True)
		self.m_textCtrl4.Enable(True)
		self.m_textCtrl5.Enable(True)
		self.m_textCtrl6.Enable(True)
		self.m_button2.Enable(False)
		self.m_button1.Enable(False)
		self.m_comboBox1.Enable(False)
		self.m_button5.Enable(True)
		self.m_button6.Enable(True)
		self.m_button3.Enable(False)
		self.m_button4.Enable(False)
		event.Skip()
	
	def eliminar( self, event ):
		self.filtro=self.m_comboBox1.GetValue()
		self.m_button3.Enable(False)

		self.a=3
		event.Skip()
	
	def aceptar( self, event ):
		self.propietario1.nombre=self.m_textCtrl1.GetValue()
		self.propietario1.direccion=self.m_textCtrl2.GetValue()
		self.propietario1.localidad=self.m_textCtrl3.GetValue()
		self.propietario1.telefono=self.m_textCtrl4.GetValue()
		self.propietario1.celular=self.m_textCtrl5.GetValue()
		self.propietario1.email=self.m_textCtrl6.GetValue()
		if self.a==1:
			self.propietario1.agregar(con1)
		elif self.a==2:
                        
			self.propietario1.update(con1,self.filtro)
			casa=Casa(self.filtro,"","","","")
			casa.updateprop(con1,self.m_textCtrl1.GetValue(),)
			
		if self.a==3:
			self.propietario1.eliminar(con1,self.filtro)

		self.m_textCtrl1.Enable(False)
		self.m_textCtrl1.SetValue("")
		self.m_textCtrl2.Enable(False)
		self.m_textCtrl2.SetValue("")
		self.m_textCtrl3.Enable(False)
		self.m_textCtrl3.SetValue("")
		self.m_textCtrl4.Enable(False)
		self.m_textCtrl4.SetValue("")
		self.m_textCtrl5.Enable(False)
		self.m_textCtrl5.SetValue("")
		self.m_textCtrl6.Enable(False)
		self.m_textCtrl6.SetValue("")
		self.m_button2.Enable(True)
		self.m_button1.Enable(True)
		self.m_comboBox1.Enable(True)
		self.m_button5.Enable(False)
		self.m_button6.Enable(False)
		self.Close()

		
		event.Skip()
	
	def cancelar( self, event ):
		self.m_textCtrl1.Enable(False)
		self.m_textCtrl1.SetValue("")
		self.m_textCtrl2.Enable(False)
		self.m_textCtrl2.SetValue("")
		self.m_textCtrl3.Enable(False)
		self.m_textCtrl3.SetValue("")
		self.m_textCtrl4.Enable(False)
		self.m_textCtrl4.SetValue("")
		self.m_textCtrl5.Enable(False)
		self.m_textCtrl5.SetValue("")
		self.m_textCtrl6.Enable(False)
		self.m_textCtrl6.SetValue("")
		self.m_button2.Enable(True)
		self.m_button1.Enable(True)
		self.m_comboBox1.Enable(True)
		self.m_button5.Enable(False)
		self.m_button6.Enable(False)
		event.Skip()
#----------------------------------------------------------------------------------------------------
#--------------- Gui de Actualizacion de Casas -----------------------------------------------
#----------------------------------------------------------------------------------------------------

class casas ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = 1, title = u"Actualizar Propiedades", pos = wx.DefaultPosition, size = wx.Size( 1115,280 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
		self.Casa1=Casa('','','','','')
		self.registro=self.Casa1.consultartodos(con1)
		self.propietario1=Propietario('','','','','','')
		self.registro1=self.propietario1.consultartodos(con1)
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
		while i < len(self.registro1):
			m_comboBox4Choices1.append(self.registro1[i][0])
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
		while i < len(self.registro):
			m_comboBox1Choices.append(self.registro[i][1])
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
		self.casa1=Casa("",self.filtro,"","","")
		self.registro=self.casa1.consultar(con1)
		self.m_textCtrl11.SetValue(self.registro[1])
		self.m_textCtrl131.SetValue(self.registro[0])
		self.m_textCtrl12.SetValue(self.registro[2])
		self.m_textCtrl13.SetValue(self.registro[3])
		a=str(self.registro[4])
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
		self.Casa1.propietario=self.m_comboBox4.GetValue()
		self.Casa1.direccion=self.m_textCtrl11.GetValue()
		self.Casa1.localidad=self.m_textCtrl12.GetValue()
		self.Casa1.estado=self.m_textCtrl13.GetValue()
		
		if self.a==1:
			self.Casa1.contrato=0
			self.Casa1.agregar(con1)
		elif self.a==2:
			self.Casa1.contrato=self.m_textCtrl14.GetValue()
			self.Casa1.update(con1,self.filtro)	
		elif self.a==3:
			if self.Casa1.estado=="LIBRE":
				self.Casa1.eliminar(con1,self.filtro)
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
#----------------------------------------------------------------------------------------------------
#--------------- Gui de Actualizacion de Inquilinos -----------------------------------------------
#----------------------------------------------------------------------------------------------------

class Inquilinos ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Actualizar Inquilinos", pos = wx.DefaultPosition, size = wx.Size( 800,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
		self.Inquilino=Inquilino('','','','','','')
		self.registro=self.Inquilino.consultartodos(con1)
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
		while i < len(self.registro):
			m_comboBox1Choices.append(self.registro[i][0])
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
		self.Inquilino.nombre=nombre
		rg1=self.Inquilino.consultar(con1)
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
		self.Inquilino.nombre=self.m_textCtrl1.GetValue()
		self.Inquilino.direccion=self.m_textCtrl2.GetValue()
		self.Inquilino.localidad=self.m_textCtrl3.GetValue()
		self.Inquilino.telefono=self.m_textCtrl4.GetValue()
		self.Inquilino.celular=self.m_textCtrl5.GetValue()
		self.Inquilino.email=self.m_textCtrl6.GetValue()
		self.filtro=self.m_comboBox1.GetValue()
		if self.ac==1:
			self.Inquilino.agregar(con1)
		if self.ac==2:
			self.Inquilino.update(con1,self.filtro)
		if self.ac==3:
			self.Inquilino.eliminar(con1,self.filtro)
		self.Destroy()
		event.Skip()
	
	def cancelar( self, event ):
		self.Destroy()
		event.Skip()

#----------------------------------------------------------------------------------------------------
#--------------- Gui de Actualizacion de Descuentos -----------------------------------------------
#----------------------------------------------------------------------------------------------------


class Descuento ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Actualizar Descuentos", pos = wx.DefaultPosition, size = wx.Size( 600,375 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.descuento1=Descuentos('','')
		self.registro=self.descuento1.consultartodos(con1)
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
		while i < len(self.registro):
			m_comboBox1Choices.append(self.registro[i][0])
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
		self.descuento1.descuento=self.m_comboBox1.GetValue()
		self.registro=self.descuento1.consultar(con1)
		self.m_textCtrl1.SetValue(self.registro[0])
		a=str(self.registro[1])
		self.m_textCtrl2.SetValue(a)
		event.Skip()
	
	def nuevo( self, event ):
		self.m_textCtrl1.Enable(True)
		self.m_comboBox1.Enable(False)
		self.m_button1.Enable(False)
		self.registro=self.descuento1.consultartodos(con1)
		i=len(self.registro)+2
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
		self.descuento1.descuento=self.m_textCtrl1.GetValue()
		self.descuento1.codigo=self.m_textCtrl2.GetValue()
		w=self.m_comboBox1.GetValue()
		if self.a==1:
			self.descuento1.agregar(con1)
		elif self.a==2:
			self.descuento1.update(con1,w)	
		elif self.a==3:
			self.descuento1.eliminar(con1,w)
		self.Destroy()
		event.Skip()
	
	def cancelar( self, event ):
		self.Destroy()
		event.Skip()

#----------------------------------------------------------------------------------------------------
#--------------- Gui de Actualizacion de Nuevo Contrato -----------------------------------------------
#----------------------------------------------------------------------------------------------------


class contratos ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Contratos", pos = wx.DefaultPosition, size = wx.Size( 640,542 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.Casa1=Casa('','','','','')
		self.rcasas=self.Casa1.consultarLibres(con1)
		self.inq1=Inquilino('','','','','','')
		self.rinq1=self.inq1.consultartodos(con1)
		self.des1=Descuentos('','')
		self.rdes1=self.des1.consultartodos(con1)

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
		while i < len(self.rcasas):
			m_comboBox5Choices.append(self.rcasas[i][1])
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
		while i < len(self.rinq1):
			m_comboBox6Choices.append(self.rinq1[i][0])
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
		self.NumCtrl1.SetAllowNegative(True) 
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
		while i < len(self.rdes1):
			m_comboBox7Choices.append(self.rdes1[i][0])
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
		self.NumCtrl2.SetAllowNegative(True) 
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
		self.Casa2=Casa('',direccion,'','','')
		self.regp=self.Casa2.consultar(con1)
		self.m_textCtrl20.SetValue(self.regp[0])
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
			self.descuento1=Descuentos('',descripcion)
			rd=self.descuento1.consultar(con1)
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
			self.cont1=Contrato(ncontrato,direccion,inquilinos,fechain,fechavto,propietario,comision)
			self.cont1.agregar(con1,descripcion,monto,impripro,imprinmo,imprinq,rd[1])
			self.Casa1.direccion=self.m_comboBox5.GetValue()
			self.Casa1.contrato=self.NumCtrlc.GetValue()
			self.Casa1.alquilar(con1)
		self.Destroy()
	def cancelar( self, event ):
		self.Destroy()
		event.Skip()
#----------------------------------------------------------------------------------------------------
#--------------- Gui de Actualizacion de Editar Contrato -----------------------------------------------
#----------------------------------------------------------------------------------------------------

class concam ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Consulta de Cotrantos", pos = wx.DefaultPosition, size = wx.Size( 580,548 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.cont1=Contrato('','','','','','','')
		self.des1=Descuentos('','')
		self.rdes1=self.des1.consultartodos(con1)
		self.Casa1=Casa('','','','','')
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
		self.NumCtrl3.SetAllowNegative(True) 
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
		while a < len(self.rdes1):
			m_comboBox7Choices.append(self.rdes1[a][0])
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
		self.NumCtrl2.SetAllowNegative(True) 
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
		self.cont1.numero=str(self.NumCtrlc.GetValue())
		a=self.cont1.consultar(con1)
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
		self.cont1.direccion=self.m_textCtrl32.GetValue()
		self.cont1.inquilino=self.m_textCtrl33.GetValue()
		self.cont1.fechain=self.m_textCtrl26.GetValue()
		self.cont1.fechavto=self.m_textCtrl27.GetValue()
		self.cont1.propietario=self.m_textCtrl20.GetValue()
		self.cont1.comision=self.NumCtrl3.GetValue()
		self.cont1.eliminar(con1)
		for i in range(self.m_listBox1.GetCount()):
			a = self.m_listBox1.GetString(i)
			lista=a.split(',')
			descripcion=lista[0]
			self.des1.descuento=lista[0]
			rd=self.des1.consultar(con1)
			monto=lista[1]
			monto=monto[0:len(monto)]
			impripro=lista[2]
			impripro=impripro[0:len(impripro)]
			imprinmo=lista[3]
			imprinmo=imprinmo[0:len(imprinmo)]
			imprinq=lista[4]
			imprinq=imprinq[0:len(imprinq)]
	
			self.cont1.agregar(con1,descripcion,monto,impripro,imprinmo,imprinq,rd[1])
		self.Destroy()
		event.Skip()
	
	def eliminarcontrato( self, event ):
		self.Casa1.contrato=0
		self.Casa1.direccion=self.m_textCtrl32.GetValue()
		print self.Casa1.direccion
		self.Casa1.desalquilar(con1)
		self.cont1.eliminar(con1)
		self.Destroy()
		event.Skip()



#--------------------------------------------------------------
#--Generar Recibos
#-------------------------------------------------------------


class recibos ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Generar Recibos", pos = wx.DefaultPosition, size = wx.Size( 569,214 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )
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
ventana = login(None)
ventana.Show()
app.MainLoop()
