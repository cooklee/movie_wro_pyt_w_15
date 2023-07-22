class A:

    def __init__(self):
        self.a = 15
        print("jestem sobie klasa A")

cebula = A
print(A)
print(cebula)
j = cebula() # A()
print(j.a)