# Multiple inheritance
print("Multiple inheritance")
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

#Multi-level inheritance
print('Multi-level inheritance')
class A1:
   a = 1

class B1(A1):
   a = 2

class C1(B1):
   pass

c = C1()
print(c.a)