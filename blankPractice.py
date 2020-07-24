#write a program that asks the user to input 10 integers, 
# and then prints the largest odd number that was entered. 
# if no odd number was entereed, it should print a message to that effect
# will need to test if not divisble by 2 to tell if the number is odd

big = 0
i = 0

while i < 10:
    i += 1
    a_list = int(input("input an integer: "))

    if a_list > big:# & a_list % 2 == 0:
        print("a_list is bigger than big")
        big = a_list
        
        if big % 2 != 0:
            print("num is odd", big)

        print("biggest num is: ", big, "\n")
    else:
        print("num ins't the biggest \n")