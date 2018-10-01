#A loop structure is a structure that allows us to run
#a section of code a number of times. It is great for 
#when we need to repeat a process. It is also great 
#when we need to run a pattern

#There are two broad catagories of looops
# Conditional Loop: This loop as long as something is true
# Counted Loops: This loops a set number of times

print("0")
print("1")
print("2")
print("3")
print("4")
print("5")

print("*********************************************************")
#The general structure of a counted loop is 
#Count: This is the variable we use to track the number
#     of times a loop runs
#Check: This the boolean (true or false) statement we evaluate 
#      to decide if we keep going
#Change: This is the change in the count that happens after each 
#     loop.each




#We use a i in range loop
for i in range (0, 6, 1):
	print(i)

#How would the above loop run
#We would reach line 27
# i = 0, 0 < 6, True RUN LOOP
# i = 1, 1 < 6, True RUN LOOP
# i = 2, 2 < 6, True RUN LOOP
# i = 3, 3 < 6, True RUN LOOP
# i = 4, 4 < 6, True RUN LOOP
# i = 5, 5 < 6, True RUN LOOP
# i = 6, 6 < 6, False EXIT LOOP AND MOVE ON 


print("**************************************************************")
print("Write a loop that will print out 7 to 104 inclusive")
for i in range(7,105,1):
	print(i)

print("**************************************************************")
print("Write a loop that will print out even number from -22 to 134 inclusive")
for i in range(-22,135,2):
	print(i)

print("**************************************************************")
print("We can count backwards as well. Python3 will assume the check base on")
print("relative value of the count and the check")

for i in range(3,0,-1):
   print(i)


print("**************************************************************")
print("Print out all numbers from 101 to 0 inclusive")

for i in range(101,-1,-1):
	print("I COULD WRITE THIS!!")
	print(i)

#Anything that is tabbed is the loop code block

s = "Fish food"
#BEST PRACTICE YOU MUST DO THIS : NEVER NEVER NEVER TYPE IN THE LENGTH AS 
#A NUMBER. ALWAYS HAVE THE COMPUTER FIND IT
#len(s) finds the length of the string s 
for i in range(0,len(s),1):
	print(s[i])
#Can you print out s in reverse?

for i in range(len(s) -1, -1, -1):
	print(s[i])

print("**************************************************************")

for i in range(0,len[s],2):
	print(s[i])












