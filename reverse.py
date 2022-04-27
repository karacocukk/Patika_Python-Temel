new_list = []

def reverse(normal_list,reverse):
    for i in normal_list:
        i.reverse()
        new_list.append(i)
    new_list.reverse()
    return reverse

a = [[1, 2], [3, 4], [5, 6, 7]]
print(reverse(a,new_list))


