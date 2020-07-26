#introduction to computaion and programming using python 2nd edition
#   ch. 2 finger exercise
#write a program that asks the user to input 10 integers, 
#   and then prints the largest odd number that was entered. 
#   if no odd number was entereed, it should print a message to that effect
#   will need to test if not divisble by 2 to tell if the number is odd

big = 0
i = 0
odd = 0
while i < 10:
    i += 1
    print("guess number:", i, "out of ten")
    a_list = int(input("input an integer: "))

    if a_list > big and a_list % 2 != 0:
        big = a_list
        odd = 1
        print("biggest odd num is: ", big)
    elif odd ==0:
        print("will need to test if odd, enter an odd number")
    else:    
        print("not the biggest number ")