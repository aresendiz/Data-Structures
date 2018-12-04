# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 19:01:53 2018

@author: rm_an
"""

def mergeSort(alist,sortedlist, start, end):
#    print("Splitting ",alist[start:end])
    if end-start>1:
        mid =start + (end-start)//2


        mergeSort(alist,sortedlist, start, mid)
        mergeSort(alist,sortedlist, mid, end)

        i=start
        j=mid
        k=start
        alist=sortedlist[:]
        while i < mid and j < end:
            if alist[i] < alist[j]:
                sortedlist[k]=alist[i]
                i=i+1
            else:
                sortedlist[k]=alist[j]
                j=j+1
            k=k+1

        while i < mid:
            sortedlist[k]=alist[i]
            i=i+1
            k=k+1

        while j < end:
            sortedlist[k]=alist[j]
            j=j+1
            k=k+1
        #print(sortedlist)
        return sortedlist
    
alist = [54,26,93,17]
#alist = [54,26,93,17,77,31,44,55,20]
print(mergeSort(alist,alist[:],0,len(alist)))
