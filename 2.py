a = 12
def abcd():
  global a
  while True:

    def hi():
        number = int(a - 1)
        p = ""
        while True:
            
            if number == 1:
                    break

            else:
                
                for i in range(1,number):
                    z = str(i)
                    final = (f"{p} {z}") 
                    p = final.replace("1","*")
                    p = p.replace("2","*")
                    p = p.replace("3","*")
                    p = p.replace("4","*")
                    p = p.replace("5","*")
                    p = p.replace("6","*")
                    p = p.replace("7","*")
                    p = p.replace("8","*")
                    p = p.replace("9","*")
                    p = p.replace("0","")
                    if number == 2:
                      print(p)

                    else: pass

                    nnumber = number - 1
                    number = nnumber  
                    
                        
              
    hi()
    b = a-1
    a = b
    if a == 1:
        break
    



    
abcd()