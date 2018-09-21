print("Slope Calculator:")

#Input

x1 = input("Input x1: ")
x1 = int(x1)#casting

y1 = input("Input y1: ")
y1 = int(y1)

x2 = input("Input x2: ")
x2 = int(x2)

y2 = input("Input y2: ")
y2 = int(y2)


#Process
rise = x2 - x1
run = y2 - y1

fSlope = rise/run

#Output
print("Your Slope is m="+str(rise)+"/"+str(run))
print("Yours slope as a decimal is " +str(fSlope))

