#Laboratorio 1 realizado por Juan Reyna 10-10883 y Nilson Estrada 11-10303
import os
from insertion import * #Importación del módulo insertion
vector1 = []			#En este vector se guardarán los elementos del .txt desde la primera línea hasta la última
archivo_revisar = open("numeros.txt","r") #Abre en modo de lectura el archivo donde se encuentran los enteros
for linea_vista in archivo_revisar:	#lee cada línea del .txt
	if len(linea_vista) == 1:		#Si la línea esta vacía no es tomada en cuenta
		pass
	elif len(linea_vista) > 1 :	#Si la línea no esta vacía, se toma en cuenta la información que ella contiene
		vector1.append(int(linea_vista)) 	  #Convierte cada línea que es tomada como string a entero(int) y guarda en vector1 la información en el orden leído
archivo_revisar.close()			#Cerramos el archivo
longitud_vector1 = len(vector1) #Calculamos la longitud de vector1
print("Los elementos del archivo de texto dado originalmente son: ")
for x in range(0,longitud_vector1):
	print(vector1[x])				#Imprime el contenido original del archivo
insertion_sort(vector1,longitud_vector1) #Invoca la función perteneciente al módulo insertion que realiza el algoritmo de ordenamiento Insertion Sort 