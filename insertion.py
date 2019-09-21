#Laboratorio 1 realizado por Juan Reyna 10-10883 y Nilson Estrada 11-10303
#En este moódulo se encuentra el algoritmo de ordenamiento Insertion Sort
def insertion_sort(vector,n):
	for i in range(1,n):
		x = vector[i]
		j = i-1
		while (j>=0) and (x<vector[j]):
			vector[j+1] = vector[j]
			j = j-1
		vector[j+1] = x
	
	print("\n\nLos elementos del archivos ordenados son:")
	for y in range(0,n):
		print(vector[y])