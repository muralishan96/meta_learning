def reverse(str):
    if len(str)==0:
        return str
    else:
        print(reverse(str[1:]))
        print('str[0] ',str[0])
        return reverse(str[1:]) + str[0]
str = 'reverse'
reverse_str = reverse(str)
print(reverse_str)