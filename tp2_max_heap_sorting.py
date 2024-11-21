def heapify(tab,i,length):
    maxim=i
    if i*2+2<length and tab[i*2+2]>tab[i*2+1]:       # if right child exists, then surely the left child exist too
        maxim=i*2+2
    if i*2+1<length and tab[i*2+1]>tab[maxim]:
        maxim=i*2+1
    if maxim != i:
        temp=tab[maxim]
        tab[maxim]=tab[i]
        tab[i]=temp
        heapify(tab,maxim,length)

def construct_max_heap(tab,length):
    for i in range(length//2 -1,-1,-1):
       heapify(tab,i,length)

   

def max_heap_sorting(tab):
    n=len(tab)
    res=[]
    construct_max_heap(tab,n)
    for i in range(n - 1, -1, -1):
        res.append(tab[0])
        k= tab[0]
        tab[0] = tab[i]
        tab[i]=k
        heapify(tab, 0, i)    
    return res

tab=[10 ,22, 5 ,18 ,20 ,25 ,40 ,30 ,35, 12]
res=max_heap_sorting(tab)
print("sorted tab:", res)