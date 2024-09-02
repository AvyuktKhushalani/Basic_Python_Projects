a = float(input("First number: "))
print("")
b = float(input("Second number: "))
print("")
c = float(input("Third number : "))
print("")
d = float(input("Fourth number: "))
print("")
e = float(input("Fifth number: "))
print("")


if a > b and a > c and a > d and a > e:
    print(f"{a} is the largest number.")


elif b > a and b > c and b > d and b > e:
    print(f"{b} is the largest number.")


elif c > a and c > b and c > d and c > e:
    print(f"{c} is the largest number.")


elif d > a and d > b and d > c and d > e:
    print(f"{d} is the largest number.")


elif e > a and e > b and e > c and e > d:
    print(f"{e} is the largest number.")