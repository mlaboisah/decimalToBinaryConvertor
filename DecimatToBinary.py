#Name: Isah Maikaita Labo 
#Reg. No: H20CS078
#Title: Decimal to Binary


while True:
    
    # input variable
    
    decimal_number= int(input("Enter a Decimal Number: "))
                  
    binary = bin(decimal_number)
    
    print("The Binary Number of "+str(decimal_number)+" is "+str(binary)[2:])
    
    #Asking a user to convert another number or to exit the program
    option = input("Do you want to convert another Number? Type Y/N\n")
    
    if(option.upper()=="N"):
        print("Thank You Good Bye...\n")
        break
    else:
        continue
              
