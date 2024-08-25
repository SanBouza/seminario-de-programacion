from threading import *

def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        list_izq = mergeSort(lista[:mid])
        list_der = mergeSort(lista[mid:])

        thread_izq = Thread(target=mergeSort, args=(list_izq,))
        thread_der = Thread(target=mergeSort, args=(list_der,))
        
        thread_izq.start()
        thread_der.start()
        thread_izq.join()
        thread_der.join()

        return merge(list_izq, list_der)
    else:
        return lista
      
        

def merge(left,right): 
    merged = []
    i=j=0

    while i <len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

# Implementación

l = [1,6,4,9,3,333,2,10,40,2]

p = mergeSort(l)

print(p)