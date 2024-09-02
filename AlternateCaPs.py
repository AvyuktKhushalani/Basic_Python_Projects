


def Letter_Seperater(User_input):

    global word
    global number

    for letter in User_input:
        newnumber = int(number + 1)

        if newnumber % 2 == 0:
            newletter = letter.lower()

        else:
            newletter = letter.upper()

        number = newnumber
        if newletter == " ":
            newletter == "  "
            space_number = number + 1
            number = space_number

        else:
            pass    

        neword = word + newletter
        word = neword

    print(word)   

while True:

    word = ""

    number = 0

    userInput = str(input("Enter: "))
    Letter_Seperater(userInput)