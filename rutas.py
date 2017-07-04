#!/usr/bin/env python
# -*- coding: utf-8
 
# import os

# path ="C:\\Users\\trasend\PycharmProjects\system_senic\\backup_envios\\" 
# #Lista vacia para incluir los ficheros
# lstFiles = [] 
# #Lista con todos los ficheros del directorio:
# lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros 
# #Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista. 
# for root, dirs, files in lstDir:
#     for fichero in files:
#         (nombreFichero, extension) = os.path.splitext(fichero)
#         if(extension == ".csv"):
#             lstFiles.append(nombreFichero+extension)

# index = len(lstFiles) - 1
# nombtem = lstFiles[index]
# recorte = nombtem[9:-4]
# nombrecsv = int(recorte) + 1
# print(lstFiles[index] )
# print(recorte)
# print(nombrecsv)
# #nombre = lstFiles[:-1]            
# print ('LISTADO FINALIZADO')
# print ("longitud de la lista = " + str(len(lstFiles)))

list = ['20170623#10', '20170624#9']
if len(list) > 1 and list[0] > list[1]:
	print (list)


