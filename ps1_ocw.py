# Write a program to calculate how many months it will take you to 
#   save up enough money for a down payment.
# a) Your program should ask the user to enter the following variables: 
#   1.The starting annual salary (annual_salary) 
#   2.The portion of salary to be saved (portion_saved) 
#   3.The cost of your dream home (total_cost)
# b) Modify your program to include the following 
#   1.Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage) 
#   2.After the 6 th month, increase your salary by that percentage. 
#       Do the same after the 12th th month, the 18 month, and so on.
# c) 


annualSalary = float(input("enter salary: "))
portionSaved = float(input("enter percent of salary to save, as a decimal: "))
totalCost = float(input("enter the cost of your dream house: "))
semiAnnualRaise = float(input("enter the semi-annual raise, as a decimal: "))


portionDownPayment = totalCost * 0.25
currentSavings = 0
r = 0.04
months = 0

while currentSavings < portionDownPayment: #want to run loop during a condition 
    currentSavings += annualSalary/12 #divide salary up by month
    currentSavings += currentSavings*portionSaved #
    #r = r/12 #r keeps changing values
    currentSavings += currentSavings*(r/12) 
    months += 1 #months is a counter
    # can be done in one line ⬇⬇⬇
    # currentSavings += (annualSalary/12)*portionSaved + currentSavings*(r/12)
    
    months += 1

print("number of months to save: ", months)
