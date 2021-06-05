command = ["d", "4","d", "4","d", "4","a", "1", "b", "2", "c", "3", "d", "4","g"]

pair = []
pair2 = []
def group_pars(arr):
    if len(arr) % 2 != 0:
        imp = len(arr) -1
        pair.append([arr[len(arr)-1]])
        pair2.append()
        arr.pop(imp)
        pair.append(group_pars(arr))
        return -1
    if len(arr) == 2:
        return arr
    if len(arr)/2 % 2 != 0:
        center_min = len(arr)//2 -1
        center_max = len(arr)//2 
        if center_min == 0:
            return -1
        pair.append(group_pars(arr[:center_min]))
        pair.append(group_pars([arr[center_min], arr[center_max]]))
        pair.append(group_pars(arr[center_max+1:]))
        return pair
    pair.append(group_pars(arr[:len(arr)//2]))
    pair.append(group_pars(arr[len(arr)//2:]))
    return pair
teste = group_pars(command)

print(teste)