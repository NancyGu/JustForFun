# coding=utf-8
# 1- 快排
# 2- 堆排


# 1- 快排-------------------------------------------------
def QuickSorted(arr):
    QuickSort(arr,0,len(arr)-1)

def partition(arr,begin,end):
    key = arr[end]
    i = begin - 1
    for j in range(begin,end+1):
        if arr[j] < key:
            i = i + 1;
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[end] = arr[end],arr[i+1]
    return i+1


def QuickSort(arr,begin,end):
    if begin < end:
        i = partition(arr,begin,end)
        QuickSort(arr,begin,i-1)
        QuickSort(arr,i+1,end)
# 2- 堆排-------------------------------------------------
def heapSort(arr):
    

arr = [6,4,2,3,10];
#QuickSorted(arr)

print(arr)