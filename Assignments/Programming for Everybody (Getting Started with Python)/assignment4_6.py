
hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
	h = float(hrs)
	r = float(rate)
except:
    print("please,enter valid number")
    quit()
def computepay(h,r):
	if(h<=40):
		return h * r
	else:
		return r * 40 + ( r * 1.5) * ( h - 40 )
p = computepay(h,r)
print(p)
