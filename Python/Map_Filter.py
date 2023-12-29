lis = ['coffee','tea','leamon tea','kattan','chai']

def find_c(coffe):
    if coffe[0]=='c':
        return coffe

# map_coffe = map(find_c,lis)
# print(type(map_coffe))
# for x in map_coffe:
#     print(x)


filter_coffe = filter(find_c,lis)
print(filter_coffe)
for i in filter_coffe:
    print(i)


a = [[96], [69]]

print(''.join(list(map(str, a))))