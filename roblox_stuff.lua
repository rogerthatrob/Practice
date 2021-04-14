# roblox stuff

### stopped on video 15


print("Hello world!")
-- commet

-- local declares variable
local myString = "hi name"
print(myString)
print(typeof(myString))

local myInt = 32
print(myInt)

-- boolean can only be lowercase `true` or `false`
local myBoolean = true

-- if else statements
if myBoolean == true then
	print("yes it is true")
end

if (1+1 == 3) then
	print("what wait")
end

-- more if

local age = 15
local movieRating = "M"

if age >= 15 then
	print("yes")
else
	print("no")
end

-- if condintinal statements
if age >= 15 or movieRating == "M" then
	print("yes")
else
	print("no")
end


-- Functions

local myName = "Rob"

local function sayMyName()
	print("My name is "..myName) -- the `..` will concatenate strings
end

sayMyName()
myName = "Bill"
sayMyName()



-- passing variables with functions

local function sayMyName(myName, age)
	print("My name is "..myName) -- the `..` will concatenate strings
	print("i am "..age.."years old") --the `..` goes before and after the variable
end

sayMyName("Rob", 10)

-- function to add two numbers
local function addNums(n1, n2)
	return n1.." + "..n2.." = "..(n1 + n2) -- this will return print out "n1 + n2 = " then add n1 to n2 and print it out.
end

local answer = addNums(5,6)
print(answer)

