# Merge-sort

def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        list_izq = lista[:mid]
        list_der = lista[mid:]
      
        # izq_ordenada = mergeSort(list_izq)    # Aca se pueden usar threads, uno cada mergeSort()
        # der_ordenada = mergeSort(list_der)

        merge(izq_ordenada,der_ordenada)
      
        

def merge(left,right): # Une las dos listas ¡¡¡YA!!! ordenadas. 
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

l = [1,6,4,9,3,2]

p = mergeSort(l)

print(l)
print(p)