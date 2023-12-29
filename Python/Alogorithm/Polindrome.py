def poly(str):
    stratIndex = 0
    endIndex = len(str)-1
    
    for i in str:
        if str[stratIndex] != str[endIndex]:
            print(str[stratIndex] , str[endIndex])
            return False
        print(i)
    return True
print(poly('racecar'))