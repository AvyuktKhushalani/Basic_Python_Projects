while True:
        
    print("")
    month = input("Month name: ")
    m = month.lower()
    print("")
        
    if "february" in m:
        year = int(input("What is the year: "))
        yesorno = float((year/4))
        if '.0' in str(yesorno):
                print("leap year , 29 days")

        else:
               print("non leap year , 28 days")

              
    elif "january" in m or "march" in m or "may" in m or "july" in m or "august" in m or "october" in m or "december" in m:
            print("31 days")


    elif "april" in m or "june" in m or "september" in m or "november" in m:
            print("30 days")

    else:
            print("Kindly check month spelling.")