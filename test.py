class A:
    def __init__(self,a):
        self.a = a
    def __repr__(self):
        return "hello"
alex = A(5)
nik = A(3)

array= []
array.append(nik)
array.append(alex)

del array[1]
del alex
print(alex)
print(array[1])