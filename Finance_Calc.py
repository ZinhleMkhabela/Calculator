#The outputs are clear and informative, showing the results in a user-friendly format.
#Good work


import math

print("/////////////////////////////////////////////////////////////////////////////////////")
print("****Choose either ‘Investment’ or ‘Bond’ from the menu below to proceed:****")
print("****Investment- to calculate the amount of interest you'll earn on interest****")
print("****Bond- to calculate the amount you'll have to pay on a home loan****")
print("/////////////////////////////////////////////////////////////////////////////////////")

#input for the type 

choice = input()

#case 1 investment

if  choice == 'investment' or choice == "INVESTMENT" or choice == 'Investment':

    #input for values

    P = float(input("Enter the deposit amount: "))

    r = float(input("Enter the rate of interest: "))

    t = int(input("Enter the number of years: "))

    type_interest = input("****Enter the type of interest.\ncompound\nsimple\n*************************")

    #select the type of interest

    if type_interest == "simple":

        A = P * (1 + r*t)

    elif type_interest == "compound":

         A = P * math.pow((1 + r), t)

    else:

        print("****Invalid type for interest selected!!!****")

    print("****The amount after", t, "years is", round(A,2))




#case 2 bond or house loan

elif choice == 'bond' or choice == "BOND" or choice == 'Bond':

    #input for values

    P = float(input("Enter the present value of the house: "))

    r = float(input("Enter the rate of interest: "))

    n = int(input("Enter the number of months for the bond: "))

    i = n/12

    repayment = (i * P)/(1 - (1 + i)**(-n))

    print("****The repayment after", n, "months is", round(repayment,2))




#invalid case

else:

    print("****EXIT SYSTEM!!****")
