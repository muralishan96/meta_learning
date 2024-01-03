# Example 1
class A:
   def a(self):
       return "Function inside A"

class B:
    def a(self):
        return "Function inside B"

class C(A,B):
    pass

# Driver code
c = C()
print(c.a())
print(C.mro())

"""Class C inherits from classes B and A. When I don't find any function a() inside class C, 
I should search for classes B and A and its important that I do it in that order."""

class A1:
    def b(self):
        return "Function inside A"

class B1:
    def b(self):
        return "Function inside B"

class C1(A1, B1):
    def b(self):
        return "Function inside C"
    pass

class D(C1):
    pass

d = D()
print(d.b())
print(D.mro())




value = 7
class A:
    value = 5

a = A()
a.value = 3
print(a.value)