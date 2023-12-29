class Reciepe():
    def __init__(self,dish,item,time) -> None:
        self.dish = dish
        self.item = item
        self.time = time
    
    def content(self):
        print('The '+self.dish + ' has ' + str(self.item) +\
            ' Preparing '+ str(self.time))
pizza = Reciepe('Pizza',['Cheese','seed','Vegitables'],45)
pasta = Reciepe('Pasta',['pasta','cheese'],55)

print(pizza.item)
print(pizza.dish)
print(pasta.dish)
print(pizza.content())