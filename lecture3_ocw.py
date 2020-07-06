## going to practice some python 
#mit ocw python lecture 3
s = "6.00 is 6.0001 and 6.0002"
new_str = ""
new_str += s[-1]
new_str += s[0]
new_str += s[4::30]    
new_str += s[13:10:-1]
print(new_str)

print('----'*10)

s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter")
                break

print('----'*10)

s="abcdefgh"
print(s[::-1]) #reverses the string

print('----'*10)

####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
####################
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")#
times = int(input("Enthusiasm level (1-10): "))

# i = 0
# while i < len(word):
#     char = word[i]
for char in word:
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a  " + char + "! " + char)
    #i += 1
print("What does that spell?")
for i in range(times):
    print(word, "!!!")

print('----'*10)

####################
## EXAMPLE: approximate cube root 
####################
cube = 27
#cube = 8120601
#cube = 10000
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0
# look for close enough answer and make sure
# didn't accidentally skip the close enough bound
while abs(guess**3 - cube) >= epsilon and guess <= cube:
   guess += increment
   num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
   print('Failed on cube root of', cube, "with these parameters.")
else:
   print(guess, 'is close to the cube root of', cube)

print('----'*10)

####################
## EXAMPLE: bisection cube root (only positive cubes!)
####################
cube = 27
#cube = 8120601
# won't work with x < 1 because initial upper bound is less than ans
#cube = 0.25
epsilon = 0.01
num_guesses = 0
low = 0
high = cube
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
   if guess**3 < cube:
       # look only in upper half search space
       low = guess
   else:
       # look only in lower half search space
       high = guess
   # next guess is halfway in search space
   guess = (high + low)/2.0
   num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube) 


   