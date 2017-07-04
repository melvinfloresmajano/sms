# -*- coding: utf-8 -*-
__author__ = "SENIC"
__copyright__ = "Copyright 2017, SENIC"

#importando librerias
import pymysql
import os
from subprocess import Popen
import time

final = int(time.strftime("%M"))
while True:
    # conexion al servidor mysql
    conn = pymysql.connect(host="45.33.62.62", port=3306, user="admin", passwd="Senic2009**", db="portal_sms")
    tblgenerales = conn.cursor()
    query_tblgenerales = "SELECT enviando, min_enviar_supervisor FROM generales"
    tblgenerales.execute(query_tblgenerales)
    enviado = tblgenerales.fetchone()
    if enviado[0] == 1:
        path = "C:\\Users\\trasend\PycharmProjects\system_senic\\backup_envios\\"
        # Lista vacia para incluir los ficheros
        lstFiles = []
        # Lista con todos los ficheros del directorio:
        lstDir = os.walk(path)  # os.walk()Lista directorios y ficheros
        # Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.
        for root, dirs, files in lstDir:
            for fichero in files:
                (nombreFichero, extension) = os.path.splitext(fichero)
                var = int(nombreFichero[9:])
                lstFiles.append(var)
        ordenarlist = sorted(lstFiles)
        index = len(ordenarlist)
        suma = ordenarlist[index - 1] + 1
        nomb_csv = time.strftime("%Y%m%d") + "#" + str(suma)
        fecha_hora = time.strftime("%Y-%m-%d") + " " + time.strftime("%I:%M:%S")
        puente = open('C:\\Users\\trasend\PycharmProjects\system_senic\\backup_envios\\' + nomb_csv + '.csv', 'a')

        inicio = time.strftime("%M")
        print("Inicio: " + inicio)
        print("Final: " + str(final))
        if int(inicio) == int(final):
            tblsupervisor = conn.cursor()
            query_tblsupervisor = "SELECT * FROM supervisor WHERE activo = 1"
            tblsupervisor.execute(query_tblsupervisor)
            for id_supervisor, nombre, numero, activo in tblsupervisor.fetchall():
                mensaje_supervisor = nombre + " SYSTEM SENIC MSJ ESTA ACTIVO " + fecha_hora
                puente.write(str(numero) + ',' + mensaje_supervisor + '\n')
            final = int(time.strftime("%M")) + int(enviado[1])
        tblchip = conn.cursor()
        query_tblchip = "SELECT sum(enviando) FROM chip where  enviando = 1"
        tblchip.execute(query_tblchip)
        num_modem = tblchip.fetchone()
        num = num_modem[0]
        limite = (int(15 / 2) * int(num))
        tblenvio_detalle = conn.cursor()
        query_tblenvio_detalle = "SELECT id_envio_detalle, numero, mensaje, estado_envio FROM envio_detalle where estado_envio = 0 LIMIT 0, " + str(
            limite)
        tblenvio_detalle.execute(query_tblenvio_detalle)
        for id_envio_detalle, numero, mensaje, estado_envio in tblenvio_detalle.fetchall():
            puente.write(str(numero) + ',' + mensaje + '\n')
            tblenvio_detalle.execute(
                "UPDATE envio_detalle SET  estado_envio = 0, fecha_envio=fecha_hora WHERE id_envio_detalle =" + str(
                    id_envio_detalle))
            # Guardar cambios.
            conn.commit()
        puente.close()
        conn.close()
        inyeccion = 'C:\SMSCaster\smscaster.exe -ImportOutbox C:\\Users\\trasend\PycharmProjects\system_senic\\backup_envios\\' + nomb_csv + '.csv -Start'
        Popen(inyeccion)
        time.sleep(15)
        print("pasos")
    else:
        print("SYSTEM SENIC MSJ DESACTIVADO.")