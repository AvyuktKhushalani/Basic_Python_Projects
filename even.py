while True:

    a = float(input("Enter the number: "))

    yesorno = (a/2)

    if '.5' in str(yesorno):
        print("odd number")

    elif '.0' in str(yesorno):
        print("even number")

    else:
        print("invalid number") 