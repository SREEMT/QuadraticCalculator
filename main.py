import cmath
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d)/(2*a))
sol2 = (-b+cmath.sqrt(d)/(2*a))
print(sol1)
print(sol2)