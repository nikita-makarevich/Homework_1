import math
π = 3.14
a = float(input(">>> Value 'a'= "))
b = float(input(">>> Value 'b'= "))
c = float(input(">>> Value 'c'= "))
A = float(input(">>> Value 'A'= "))
p = (a+b+c)/2
A = (π*A)/180
S = π*((p-a)*math.tan(A/2))**2
print("Answer: S =", round(S,2))