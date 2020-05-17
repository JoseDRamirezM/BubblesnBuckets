import sys
sys.setrecursionlimit(1500)

def burbuja(arr):
	intercambio = 0
	inicio = False
	for i in arr:
		if(not inicio or intercambio > 0):
			
			for j in range (0, len(arr)-1,1):
				if(arr[j] > arr[j+1]):
					arr[j], arr[j+1] = arr[j+1], arr[j]
					intercambio += 1
				inicio = True
	print(intercambio)		
	return arr

counter = 0

arr1 = [5,1,3,4,2] #Carlos
arr2 = [1,2,3,4,5] #Carlos
arr = [1,5,3,4,2] #Marcelo
arr3 = [6,5,4,3,2,1] #Marcelo
#arr = [1,2,3,4,5,6,7]

def tipo(num):
	if(num%2 == 0):
		return True
	else: return False

def ganador():
	if(tipo(counter)):
		print("Carlos")
	else: print("Marcelo")

def quickSort(arreglo):
	global counter

	if(len(arreglo) < 1):
		return []

	derecha = []
	izquierda = []
	pivote = arreglo[0]		
	for elemento in arreglo[1:]:		
		if(elemento < pivote):
			counter += 1
			izquierda.append(elemento)
		else:
			counter+= 1
			derecha.append(elemento)

	return quickSort(izquierda) + [pivote] + quickSort(derecha) 


print(quickSort(arr))
ganador()
counter = 0
print(quickSort(arr1))
ganador()
counter = 0
print(quickSort(arr2))
ganador()
counter = 0
print(quickSort(arr3))
ganador()
