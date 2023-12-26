def divided(a,b):
    return a/b
try:
    ans =print(divided(40,0))
except ZeroDivisionError:
    print("Something Wrong ")
except Exception as e:
    print('SOmething went wrong!')
