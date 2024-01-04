class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())



print("hello worlg");
a =2
print(type(a))

b=2.3
print(type(b))

c='helloo'
print(type(c))

d=[2,3.3,'sss']
print(type(d))

ed={'a':22,'d':33}
print(type(ed))

sets = {2,3,3,'eed',3.3}
print(type(sets))