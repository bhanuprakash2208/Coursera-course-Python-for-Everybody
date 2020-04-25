fname = input("Enter file name: ")
fh = open(fname)
filecontents = fh.read()
print(filecontents.rstrip().upper())
