favorites = ["chuchu","Akilandeswari",'amma','sakthi','priya']

for item in favorites:
    print("My fav item is : "+item)
count = 0
while count <len(favorites):
    print(" My fav item is : "+favorites[count])
    count += 1
    
for idx,item in enumerate(favorites,22):
    print(idx,item)