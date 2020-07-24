#write a program that asks the user to input 10 integers, 
# and then prints the largest odd number that was entered. 
# if no odd number was entereed, it should print a message to that effect
#will need to test if not divisble by 2 to tell if the number is odd

a_list = []
i = 0
while i<10:
    a_list = int(input("enter a digit: "))
    i = i+1

print('left while loop')

