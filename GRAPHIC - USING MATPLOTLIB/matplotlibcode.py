# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 10:31:17 2020

@author: Arthur Lopes Morais
"""

## Instead of creating this point system, 
##you could create a dataframe and order a plot of the graphic

import matplotlib.pyplot as plt

plt.xlabel('VECTOR SIZE')
plt.ylabel('ALGORITHM EXECUTION TIME')
plt.title('SORTING ALGORITHMS')

x = [6,1000,10000]
BUBBLESORT = [2.5800000003073364*(10**-5), 0.2943885999999907, 31.9783572999999 ]
INSERTIONSORT = [1.2399999945955642*(10**-5), 0.08758840000001555, 9.4652789 ]
SELECTIONSORT = [1.3699999954042141*(10**-5),0.05599760000001197, 7.9527646 ]
MERGESORT = [2.949999998236308*(10**-5),0.003754700000001776, 0.1520442 ]
QUICKSORT = [2.0700000050055678*(10**-5), 0.004962400000067646, 0.0755325  ]

plt.plot(x, BUBBLESORT, color = "blue", label = "Bubble Sort", linewidth=1.0)
plt.plot(x, INSERTIONSORT, color = "red", label = "Insertion Sort", linewidth=1.0)
plt.plot(x, SELECTIONSORT, color = "green",label = "Selection Sort", linewidth=1.0) 
plt.plot(x, QUICKSORT, color = "yellow", label = "Quick Sort", linewidth=1.0)
plt.plot(x, MERGESORT, color = "grey", label = "Merge Sort", linewidth=1.0)

plt.legend()
plt.show()