#estescrípt tem tempo de compilação, diferença entre fim ao inicio(fim - inicio), 0.00107574462890625 neste array de 1335 elementos

import time
inicio = time.time()
command = ["d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s","d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","s"]

pair = []
def group_pars(arr):
    if len(arr) % 2 != 0:
        imp = len(arr) -1
        pair.append([arr[len(arr)-1]])
        arr.pop(imp)
        group_pars(arr)
        return -1
    if len(arr) == 2:
        pair.append(arr)
        return arr
    if len(arr)/2 % 2 != 0:
        center_min = len(arr)//2 -1
        center_max = len(arr)//2 
        group_pars(arr[:center_min])
        group_pars([arr[center_min], arr[center_max]])
        group_pars(arr[center_max+1:])
        return pair
    group_pars(arr[:len(arr)//2])
    group_pars(arr[len(arr)//2:])
    return pair
group_pars(command)
fim = time.time()
print(pair)

print(fim - inicio)


