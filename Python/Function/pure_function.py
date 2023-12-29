#cannot change the global varible value

list = [2,3,4,5]

def addList(lst,val):
    nl = lst.copy()
    nl.append(val)
    return nl

print('new list ',addList(list,8))
print('Old list',list)