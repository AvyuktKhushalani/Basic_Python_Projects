number = int(input("Enter which number's table do you want: "))

for i in range(1, 13):
    product = i * number
    print(f"{i} * {number} = {product}")