Number = 0
Maximum = None
Minimum = None
while True:
    Number = input("Enter a Number: ")
    if (Number=="done"):
        break
    try:
        Number = int(Number)
    except:
        print("Invalid input")
        continue
    if(Maximum is None):
            Maximum = Number
    elif(Number > Maximum):
            Maximum = Number

    if(Minimum is None):
            Minimum = Number
    elif(Number < Minimum):
        	Minimum = Number
print("Maximum is",Maximum)
print("Minimum is",Minimum)
