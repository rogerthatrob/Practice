magicNumber = 26

for n in range(101):
    if n is magicNumber:
        print("found number that is magic" , n)
        break 
    else:
        if n % 4 == 0:
            print("num guessed", n, "is divis by 4")
        print(n, "is not the magic number, try again")