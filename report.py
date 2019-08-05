
#-------------------modulos necesarios -----------------------------------------------

import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import mm
from reportlab.platypus import Image
import time
from lib.Coneccion import Coneccion
from lib.Contratos import Contrato
import modulos

#------------------comienzo de funcion -----------------------------------------------
def pdf(periodo,registro,con1):

    recibos="C:/findhome 3/recibos/recibo_mes_de_"+periodo+".pdf"
    c=canvas.Canvas(recibos,pagesize=landscape(A4))
    reg=0
    l=0

    r2 = registro
    reg=reg+1
    # ----------formato line de margen (arx,ary,mux,muy) -----------------------------
    c.setDash(1,1)
    c.line(285,827,285,0)
    c.line(570,827,570,0)
    c.line(0,400,950,400)
    c.line(0,450,950,450)
    salto=0
    for i in range(3):
        #-----------formato cuerpo plantilla -----------------------------------------
        c.drawImage('img/Raices_Logo.jpg',10+salto,550,width=80, height=50) # logo de reices
        c.setFont('Helvetica-Bold',8) #parametro para string helvelica negrita 8
        c.drawString(15+salto,550,'B.Lopez 1564 - AREQUITO')
        c.drawString(20+salto,540,'Servicios Inmobiliarios')
        c.setFont('Helvetica', 8)#cambio parametro para string
        c.drawString(200+salto,570,'Fecha:')
        c.drawString(200+salto,560,'Contrato N: ')
        c.drawString(20+salto,530,'N Matricula: 0839')
        c.drawString(15+salto,520,'Tel: 03464-471683/471528')
        c.drawString(10+salto,510,'Email: raices@godata.com.ar')
        c.drawString(10+salto,490,'RECIBI DE: ')
        c.drawString(10+salto,480,'PERIODO: ')
        c.drawString(10+salto,470,'LA SUMA DE: ')
        c.drawString(10+salto,460,'POR CASA UBICADA EN: ')
        c.setFont('Helvetica-Bold', 10)
        c.drawString(15+salto,40,'INI. CONTR:')
        c.drawString(15+salto,30,'FIN CONTR.:')
        c.setDash(1,1)#Cambio de lineas a punto
        c.setFont('Helvetica-Bold', 8)
        c.drawString(20+salto,425,'DESCRIPCION')
        c.drawString(200+salto,425,'MONTO')
        c.drawString(100+salto,80,'NETO A PAGAR $')
        c.line(10+salto,60,125+salto,60)#cuadrado
        c.line(10+salto,20,125+salto,20)#cuadrado
        c.line(10+salto,60,10+salto,20)#cuadrado
        c.line(125+salto,60,125+salto,20)#cuadrado
        c.line(130+salto,40,240+salto,40)
        c.drawString(150+salto,30,'RECIBI CONFORME')
        # -------relleno de plantilla-------------------------------------------------
        c.drawString(230+salto,570,time.strftime("%d/%m/%y"))#Ref. Fecha
        #relleno por tabla.----------------------------------------------------------
        c.drawString(250+salto,560,r2[0][0])
        c.drawString(80+salto,40,r2[0][4])
        c.drawString(80+salto,30,r2[0][5])
        comision=str(r2[0][11])
        c.drawString(55+salto,480,periodo)
        c.drawString(110+salto,460,r2[0][2])
        control=modulos.seleccion(r2[0][5])
        if control == "VENCIDO":
            c.setFont('Helvetica-Bold', 15)
            c.drawString(20+salto,300,'VENCIDO')
        else:
            print control
        salto=salto+285
    c.drawString(60,490,r2[0][3])
    c.drawString(80,50,comision)
    c.drawString(650,50,comision)
    c.drawString(15,50,'COMISION: $')
    c.drawString(585,50,'COMISION: $')
    c.drawString(345,490,'RAICES SERVICIOS INMOBILIARIOS')
    c.drawString(630,490,'RAICES SERVICIOS INMOBILIARIOS')
    c.drawString(720,20,r2[0][6])
    suma=0
    b=0
    k=0
    for a in r2:
        if r2[k][9]=="SI":
            s=r2[k][10]
            suma=suma+s

            s=str(s)
            mont1=len(s)
            if mont1<6:
                space=" "
                acc=6-mont1
                relleno=acc*space
                s=relleno+s

            c.drawString(305,370-b,r2[k][1])
            c.drawString(485,370-b,'$')
            c.drawString(495,370-b,s)
            b=b+10
        k=k+1
    neto=str(suma)
    c.drawString(485,80,neto)
    c.drawString(385,470,"$ "+neto)
    b=0
    k=0
    suma=0
    s=0
    for a in r2:
        if r2[k][8]=="SI":
            s=r2[k][10]
            suma=suma+s

            s=str(s)
            mont1=len(s)
            if mont1<6:
                space=" "
                acc=6-mont1
                relleno=acc*space
                s=relleno+s
            c.drawString(20,370-b,r2[k][1])
            c.drawString(200,370-b,'$')
            c.drawString(210,370-b,s)
            b=b+10
        k=k+1
    neto=str(suma)
    c.drawString(100,470,"$ "+neto)
    c.drawString(200,80,neto)
    b=0
    k=0
    suma=0
    s=0
    for a in r2:
        if r2[k][7]=="SI":
            s=r2[k][10]
            suma=suma+s

            s=str(s)
            mont1=len(s)
            if mont1<6:
                space=" "
                acc=6-mont1
                relleno=acc*space
                s=relleno+s
            c.drawString(590,370-b,r2[k][1])
            c.drawString(770,370-b,'$')
            c.drawString(780,370-b,s)
            b=b+10
        k=k+1
    neto=str(suma)
    c.drawString(670,470,"$ "+neto)
    c.drawString(770,80,neto)




    c.showPage()



    c.save()


    import os
    os.startfile(recibos)


def pdft(periodo,registro,con1):

    recibos="C:/findhome 3/recibos/recibo_mes_de_"+periodo+".pdf"
    c=canvas.Canvas(recibos,pagesize=landscape(A4))
    reg=0
    l=0
    for l in range(len(registro)):
        r2 = registro[l]
        print r2
        reg=reg+1
    # ----------formato line de margen (arx,ary,mux,muy) -----------------------------
        c.setDash(1,1)
        c.line(285,827,285,0)
        c.line(570,827,570,0)
        c.line(0,400,950,400)
        c.line(0,450,950,450)
        salto=0
        for i in range(3):
            #-----------formato cuerpo plantilla -----------------------------------------
            c.drawImage('img/Raices_Logo.jpg',10+salto,550,width=80, height=50) # logo de reices
            c.setFont('Helvetica-Bold',8) #parametro para string helvelica negrita 8
            c.drawString(15+salto,550,'B.Lopez 1564 - AREQUITO')
            c.drawString(20+salto,540,'Servicios Inmobiliarios')
            c.setFont('Helvetica', 8)#cambio parametro para string
            c.drawString(200+salto,570,'Fecha:')
            c.drawString(200+salto,560,'Contrato N: ')
            c.drawString(20+salto,530,'N Matricula: 0839')
            c.drawString(15+salto,520,'Tel: 03464-471683/471528')
            c.drawString(10+salto,510,'Email: raices@godata.com.ar')
            c.drawString(10+salto,490,'RECIBI DE: ')
            c.drawString(10+salto,480,'PERIODO: ')
            c.drawString(10+salto,470,'LA SUMA DE: ')
            c.drawString(10+salto,460,'POR CASA UBICADA EN: ')
            c.setFont('Helvetica-Bold', 10)
            c.drawString(15+salto,40,'INI. CONTR:')
            c.drawString(15+salto,30,'FIN CONTR.:')
            c.setDash(1,1)#Cambio de lineas a punto
            c.setFont('Helvetica-Bold', 8)
            c.drawString(20+salto,425,'DESCRIPCION')
            c.drawString(200+salto,425,'MONTO')
            c.drawString(100+salto,80,'NETO A PAGAR $')
            c.line(10+salto,60,125+salto,60)#cuadrado
            c.line(10+salto,20,125+salto,20)#cuadrado
            c.line(10+salto,60,10+salto,20)#cuadrado
            c.line(125+salto,60,125+salto,20)#cuadrado
            c.line(130+salto,40,240+salto,40)
            c.drawString(150+salto,30,'RECIBI CONFORME')
            # -------relleno de plantilla-------------------------------------------------
            c.drawString(230+salto,570,time.strftime("%d/%m/%y"))#Ref. Fecha
            #relleno por tabla.----------------------------------------------------------
            c.drawString(250+salto,560,r2[0][0])
            c.drawString(80+salto,40,r2[0][4])
            c.drawString(80+salto,30,r2[0][5])
            comision=str(r2[0][11])
            c.drawString(55+salto,480,periodo)
            c.drawString(110+salto,460,r2[0][2])
            control=modulos.seleccion(r2[0][5])
            if control == "VENCIDO":
                c.setFont('Helvetica-Bold', 15)
                c.drawString(20+salto,300,'VENCIDO')
            else:
                print control
            salto=salto+285
        c.drawString(60,490,r2[0][3])
        c.drawString(80,50,comision)
        c.drawString(650,50,comision)
        c.drawString(15,50,'COMISION: $')
        c.drawString(585,50,'COMISION: $')
        c.drawString(345,490,'RAICES SERVICIOS INMOBILIARIOS')
        c.drawString(630,490,'RAICES SERVICIOS INMOBILIARIOS')
        c.drawString(720,20,r2[0][6])
        suma=0
        b=0
        k=0
        for a in r2:
            if r2[k][9]=="SI":
                s=r2[k][10]
                suma=suma+s

                s=str(s)
                mont1=len(s)
                if mont1<6:
                    space=" "
                    acc=6-mont1
                    relleno=acc*space
                    s=relleno+s

                c.drawString(305,370-b,r2[k][1])
                c.drawString(485,370-b,'$')
                c.drawString(495,370-b,s)
                b=b+10
            k=k+1
        neto=str(suma)
        c.drawString(485,80,neto)
        c.drawString(385,470,"$ "+neto)
        b=0
        k=0
        suma=0
        s=0
        for a in r2:
            if r2[k][8]=="SI":
                s=r2[k][10]
                suma=suma+s

                s=str(s)
                mont1=len(s)
                if mont1<6:
                    space=" "
                    acc=6-mont1
                    relleno=acc*space
                    s=relleno+s
                c.drawString(20,370-b,r2[k][1])
                c.drawString(200,370-b,'$')
                c.drawString(210,370-b,s)
                b=b+10
            k=k+1
        neto=str(suma)
        c.drawString(100,470,"$ "+neto)
        c.drawString(200,80,neto)
        b=0
        k=0
        suma=0
        s=0
        for a in r2:
            if r2[k][7]=="SI":
                s=r2[k][10]
                suma=suma+s

                s=str(s)
                mont1=len(s)
                if mont1<6:
                    space=" "
                    acc=6-mont1
                    relleno=acc*space
                    s=relleno+s
                c.drawString(590,370-b,r2[k][1])
                c.drawString(770,370-b,'$')
                c.drawString(780,370-b,s)
                b=b+10
            k=k+1
        neto=str(suma)
        c.drawString(670,470,"$ "+neto)
        c.drawString(770,80,neto)




        c.showPage()



    c.save()


    import os
    os.startfile(recibos)






