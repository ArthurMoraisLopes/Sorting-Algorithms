# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 20:27:01 2020

@author: Arthur Lopes
"""

'''This program aims to calculate
    which algorithm is the most 
    efficient in the sorting function'''


from random import randrange
import timeit


#Sorting Function



def Bubble_Sort (vector,vector_size):
    aux = 0
    for var1 in range (1,vector_size):
        for var2 in range (0,vector_size-1):
            if (vector[var2] > vector[var2 + 1]):
                aux = vector[var2]
                vector[var2] = vector[var2 + 1]
                vector[var2 + 1] = aux
    return vector



def Insertion_Sort (vector,vector_size):
   
    aux = 0
    for var1 in range (1,vector_size ):
        aux = vector[var1]
        var2 = var1 - 1
        while (aux < vector[var2] and var2 >= 0):
            vector[var2 + 1] = vector[var2]
            var2 = var2 - 1
        vector[var2 + 1] = aux
    return vector



def Selection_Sort (vector,vector_size):
    aux = 0; var1 = 0
    for var1 in range (vector_size):
        pos = var1
        for var2 in range (var1 + 1, vector_size):
            if vector[var2] < vector[pos]:
                pos = var2
    
        if (var1 != pos):
            aux = vector[var1]
            vector[var1] = vector[pos]
            vector[pos] = aux
    return vector



def Merge_Sort(vector, vector_size):

    if (vector_size > 1):
        
        middle =  (vector_size//2)
        
        ##Separação das listas
        left_vector = vector[:middle]
        right_vector = vector[middle:]
        len_left_vector = len(left_vector)
        len_right_vector = len(right_vector)

        #chama recursivo
        Merge_Sort(left_vector,len_left_vector)
        Merge_Sort(right_vector, len_right_vector)

        var1 = 0; var2 = 0; index_ord = 0

        while (var1 < len_left_vector and var2 < len_right_vector):

            if (left_vector[var1] < right_vector[var2]):
                vector[index_ord] = left_vector[var1]
                var1 = var1 + 1
                
            else:
                vector[index_ord] = right_vector[var2]
                var2 = var2 + 1
            index_ord = index_ord + 1

        while (var1 < len_left_vector):
            vector[index_ord] = left_vector[var1]
            var1 =var1 + 1
            index_ord = index_ord + 1

        while (var2  < len_right_vector):
            vector[index_ord] = right_vector[var2]
            var2 = var2 + 1
            index_ord = index_ord + 1
            
    return vector

        

def Partition(vector , start, end):
    
        
    left = start + 1 
    pivo = vector[start]
    right = end
    operator = False
    while not operator:
        while (left <= right and vector[left] <= pivo):
            left = left + 1
        while (right >=left and vector[right] >= pivo):
            right = right -1
        if right < left:
            operator = True
            
        else:
            ##FORM 1: Exchange of elements in vector
            vector[left], vector[right] = vector[right],vector[left]
    
     ##FORM 2: Exchange of elements in vector
    temporario=vector[start]
    vector[start]=vector[right]
    vector[right]=temporario
    return right

        
def Quick_Sort(vector, start, end):
    if (start<end):
         reparticaovetor = Partition (vector,start,end)
         Quick_Sort(vector, start, reparticaovetor-1)
         Quick_Sort(vector, reparticaovetor+1, end)
    return vector



    
    
    
#Criação de Vetores
    
lista_De_Tempos = []
vector0 = []
vector1 = []
vector2 = []
vector3 = []
vector4 = []
copy_vector = []

vector_size = 10000


for i in range(vector_size):
    a = randrange(0,10000)
    vector0.append(a)
    vector1.append(a)
    vector2.append(a)
    vector3.append(a)
    vector4.append(a)

print ('\nNormal Vector: {}'.format(vector0))
print ('----------Sorting Vectors----------\n')


timeini1 = timeit.default_timer()
a = ((Bubble_Sort(vector0, vector_size)))
timefin1 = timeit.default_timer()
time1 = timefin1 - timeini1 
print ('Bubble_Sort: {}'.format(a))
print ('Tempo: {}'.format(time1))


timeini2 = timeit.default_timer()
a = (Insertion_Sort(vector1, vector_size))
timefin2 = timeit.default_timer()
time2 = timefin2 - timeini2
print ('Insertion_Sort: {}'.format(a))
print ('Tempo: {}\n'.format(time2))


print ('Selection_Sort: {}'.format(a))
timeini3 = timeit.default_timer()
a = (Selection_Sort(vector2, vector_size))
timefin3 = timeit.default_timer()
time3 = timefin3 - timeini3
print ('Selection_Sort: {}'.format(a))
print ('Tempo: {}\n'.format(time3))



timeini4 = timeit.default_timer()
a = (Merge_Sort(vector3, vector_size))
timefin4 = timeit.default_timer()
time4 = timefin4 - timeini4
print ('Merge_Sort:: {}'.format(a))
print ('Tempo: {}\n'.format(time4))



timeini5 = timeit.default_timer()
a = (Quick_Sort(vector3, 0 , vector_size - 1))
timefin5 = timeit.default_timer()
time5 = timefin5 - timeini5
print ('Quick_Sort: {}'.format(a))
print ('Tempo: {}\n'.format(time5))
