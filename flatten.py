
new_list = []

def flat_function(a,liste):
    for i in a:
        if type(i) != list:
            new_list.append(i)
        elif type(i) == list:
            flat_function(i,new_list)
                        
    return liste

nested_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
print(flat_function(nested_list,new_list))
