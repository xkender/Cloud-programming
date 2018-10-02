#print an introduction
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    #Input the amount of the principal
    principal = eval(input("Enter the amount of the principal: "))
    #Input the annual percentage rate
    apr = eval(input("Enter the annual interest rate: "))
    #Repeat 10 times: (counted loop)

    for i in range(10):
        #Calculate principal = principal * (1 + apr)
        principal = principal * (1 + apr)

    #Output the value of the principal
    print ("The value in 10 years is", principal)

main()
