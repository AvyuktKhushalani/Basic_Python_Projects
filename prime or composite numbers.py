print(".0 is not accepted")

while True:
    number = int(input("Enter the number: "))
    def main():
        
        value = (number/2)
        print(value)
        if '.5' in str(value):
            newvalue = int(value + 0.5)
            for i in range(1, newvalue):
                b = float(number/i)
                if '.0' in str(b):
                    return True
                    break

            else:
                return False
                pass

            

        else:
            cvalue = int(value)
            for y in range(2, cvalue):
                c = float(number/y)
                if '.0' in str(c):
                    print(str(c))
                    return True
                    


                else:
                    return False
                pass
                    
    if number == 1:
        print("1 is neither prime nor composite")

    else:

        statement =  main()
        if statement == True:
            print(f"{number} is a prime number")

        elif statement == False:
            print(f"{number} is a composite number")