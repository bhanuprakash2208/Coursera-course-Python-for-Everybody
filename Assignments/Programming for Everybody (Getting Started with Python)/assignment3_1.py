hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
	h = float(hrs)
	r = float(rate)
except:
    print("please,enter valid number")
    quit()
if ( h <= 40 ):
    print( h * r)
else:
    print(r * 40 + (r * 1.5) * (h - 40))
