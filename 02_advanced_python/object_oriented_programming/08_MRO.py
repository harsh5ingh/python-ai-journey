class A:
  label = "A: Base Class"

class B:
  label = "B: Masala Blend"

class C(A):
  label = "C: Herbal blend"

class D(C, B):
  pass

cup = D()
print(D) 