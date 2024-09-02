while True:

    a = float(input("Enter number: "))

    if int(a) == 0:
        print("The number is 0 which is neither positive nor negative.")

    elif "-" in str(a):
        print(f"{a} is a negative number.")

    else:
        print(f"{a} is a positive number.")